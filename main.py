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


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

'''This part is about creating the first row and data (insert)'''
# emp1 = Employees(name= "Sagar", position= "Divu's Husband")
# session.add(emp1)
# session.commit()

# session.add_all([
#     Employees(name='Divya', position='Software Developer'),
#     Employees(name='Divi', position='Software Tester'),
#     Employees(name='Divu', position='Software Trainee')
# ])

# session.commit()/

'''This part is about reading the data'''
# query = session.query(Employees).all()
# for employee in query:
#     print(f"Name: {employee.name},Position: {employee.position}")

# query = session.get(Employees,2)
# print(query.name, query.position)

# query = session.query(Employees).filter(Employees.id != 3)
# for employee in query:
#     print(f"Name: {employee.name},Position: {employee.position}")

# query = session.query(Employees).filter(Employees.name.like('%a'))
# for employee in query:
#     print(f"Name: {employee.name},Position: {employee.position}")

# query = session.query(Employees).filter(Employees.id.in_([1,3]))
# for employee in query:
#     print(f"Name: {employee.name},Position: {employee.position}")

# query = session.query(Employees).filter(and_(Employees.id>1,Employees.id<=3, Employees.name.like("%Div%")))
# for employee in query:
#     print(f'Name: {employee.name}, Position: {employee.position}')
'''Select * from employees'''

'''This part is about updating the data'''
# print("update part\n")
# query = session.get(Employees, 2)
# print(query.name,query.position)
# query.name= "Divyanshi baby"
# query.position= "My wife"
# session.commit()
# query = session.get(Employees,2)
# print(query.name,query.position)

# query =session.query(Employees).filter(Employees.id == 2)
# query.update({Employees.name: "Diyanshi baby girl"})
# session.commit()
# query = session.get(Employees,2)
# print(query.name,query.position)

'''This part is about deleting the data'''

# query = session.get(Employees,1)
# session.delete(query)
# session.commit()

query = session.query(Employees).all()  #getting all at once
for employee in query:
    print(f'id: {employee.id}, Name: {employee.name}, Position: {employee.position}' )