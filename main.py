from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker
engine=create_engine('sqlite:///hr.db')
Base = declarative_base
class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
Base.metadata.create.all(engine)
Session = sessionmaker(bind=engine)
session = Session()
#row1 = Employees(name='Divyanshi', position = 'Software Developer')
session.add_all[Employees(name='Divya', position = 'Software Developer'),
                Employees(name='Divi', position = 'Software Tester'),
                Employees(name='Divu', position = 'Software Trainee')]
session.commit()



