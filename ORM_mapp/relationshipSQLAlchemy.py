from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

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

    invoiceID = Column(Integer, primary_key=True)
    customerID = Column(Integer, ForeignKey('customers.id'))
    invoiceNum = Column(Integer)
    amount = Column(Integer)
    customer = relationship('Customer', back_populates = 'invoices')

Customer.invoices = relationship('Invoice', order_by = Invoice.invoiceID, back_populates = 'customer')
Base.metadata.create_all(engine)