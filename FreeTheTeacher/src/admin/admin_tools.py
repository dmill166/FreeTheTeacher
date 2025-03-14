from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Association table for many-to-many relationship between Users and Roles
user_roles_table = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('role_id', Integer, ForeignKey('roles.id'), primary_key=True)
)

class User(Base):
    """User model."""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    roles = relationship('Role', secondary=user_roles_table, back_populates='users')

class Role(Base):
    """Role model."""
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    permissions = Column(String)  # Comma-separated permissions
    users = relationship('User', secondary=user_roles_table, back_populates='roles')

class Setting(Base):
    """Setting model."""
    __tablename__ = 'settings'

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, nullable=False)
    value = Column(String)

class AdminTools:
    """AdminTools provides administrative functions for IT maintenance."""

    def __init__(self, db_url='sqlite:///admin_tools.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_user(self, username, role_name):
        """Add a new user to the system with a specific role."""
        session = self.Session()
        role = session.query(Role).filter_by(name=role_name).first()
        if not role:
            raise ValueError(f"Invalid role: {role_name}")
        user = User(username=username)
        user.roles.append(role)
        session.add(user)
        session.commit()
        session.close()

    def remove_user(self, username):
        """Remove a user from the system."""
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def update_settings(self, key, value):
        """Update application settings."""
        session = self.Session()
        setting = session.query(Setting).filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            setting = Setting(key=key, value=value)
            session.add(setting)
        session.commit()
        session.close()

    def get_users(self):
        """Retrieve the list of users."""
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return [user.username for user in users]

    def get_settings(self):
        """Retrieve the application settings."""
        session = self.Session()
        settings = session.query(Setting).all()
        session.close()
        return {setting.key: setting.value for setting in settings}

    def get_user_role(self, username):
        """Retrieve the roles of a specific user."""
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        return [role.name for role in user.roles] if user else None

    def get_permissions(self, username):
        """Retrieve the permissions for a specific user."""
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        if user:
            permissions = []
            for role in user.roles:
                permissions.extend(role.permissions.split(','))
            session.close()
            return permissions
        session.close()
        return []

    def has_permission(self, username, permission):
        """Check if a user has a specific permission."""
        return permission in self.get_permissions(username)