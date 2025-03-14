from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Assuming students have names

class AttendanceRecord(Base):
    __tablename__ = 'attendance_records'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    date = Column(Date, nullable=False)
    present = Column(Boolean, default=True)
    student = relationship('Student', back_populates='attendance_records')

Student.attendance_records = relationship('AttendanceRecord', back_populates='student')

class AttendanceTracker:
    def __init__(self, db_url='sqlite:///attendance.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def mark_attendance(self, student_id, date, present=True):
        session = self.Session()
        record = AttendanceRecord(student_id=student_id, date=date, present=present)
        session.add(record)
        session.commit()
        session.close()

    def get_attendance(self, student_id):
        session = self.Session()
        records = session.query(AttendanceRecord).filter_by(student_id=student_id).all()
        attendance = {record.date: record.present for record in records}
        session.close()
        return attendance

    def generate_attendance_report(self):
        session = self.Session()
        report = {}
        students = session.query(Student).all()
        for student in students:
            records = session.query(AttendanceRecord).filter_by(student_id=student.id).all()
            total_days = len(records)
            days_present = sum(1 for record in records if record.present)
            days_absent = total_days - days_present
            report[student.id] = {
                'name': student.name,
                'total_days': total_days,
                'days_present': days_present,
                'days_absent': days_absent
            }
        session.close()
        return report