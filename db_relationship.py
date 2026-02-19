from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import and_

engine = create_engine('sqlite:///hr.db')
Base = declarative_base()

class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)

#new table

class Projects(Base):
    __tablename__ = 'projects'
    id = Column(Integer,primary_key=True)
    emp_id = Column(Integer,ForeignKey('employees.id'))
    name = Column(String)
    employees = relationship('Employees',back_populates='projects')

Employees.projects = relationship('Projects',back_populates='employees')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

emp1 = Employees(name='Sagar', position = 'Husband')
emp1.projects = [Projects(name = 'Wedding'),Projects(name = 'Evara')]

session.add(emp1)
session.commit()
query = session.query(Employees).all()  #getting all at once
for employee in query:
    print(f'Name: {employee.name}, Position: {employee.position}, Projects: {[i.name for i in employee.projects]}' )