from setuptools import setup, find_packages

setup(
    name='FreeTheTeacher',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A class roster management and communication system for teachers and parents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/FreeTheTeacher',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',  # or 'Django' depending on your choice of web framework
        'SQLAlchemy',  # for database interactions
        'requests',  # for making HTTP requests if needed
        # Add other dependencies as needed
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)