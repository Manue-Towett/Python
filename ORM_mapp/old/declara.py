from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sales.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    name = Column(String)

Base.metadata.create_all(engine)

cus1 = Customer(name = 'Emmanuel Towett')
session.add(cus1)

session.commit()