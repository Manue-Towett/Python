from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///sales.db', echo = True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    firstName = Column(String)
    lastName = Column(String)

class Invoice(Base):
    __tablename__ = 'invoices'

    invoiceID = Column(Integer, primary_key = True)
    customerID = Column(Integer, ForeignKey('customers.id'))
    