from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sales.db', echo = True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key = True)
    name = Column(String)

result = session.query(Customer).all()

for row in result:
    print(row.name)

id_2 = session.query(Customer).get(2)

print(id_2.name)

id_2.name = "Manue"
session.commit()

firstRow = session.query(Customer).first()
print(firstRow.id, firstRow.name)

session.query(Customer).filter(Customer.name!="Modester").update({Customer.name:"Mr."+Customer.name}, synchronize_session = False)
session.commit()

result = session.query(Customer).filter(Customer.name.like('Mod%'))
for row in result:
    print(row.name)

in_quer = session.query(Customer).filter(Customer.id.in_([1,3]))
for row in in_quer:
    print(row.id, row.name)