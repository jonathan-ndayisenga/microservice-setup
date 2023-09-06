from sqlalchemy  import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add other customer-related fields

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    # Add other product-related fields
    
    
    from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy session
engine = create_engine('database_connection_string')
Session = sessionmaker(bind=engine)
session = Session()

# Create a new order
new_order = Order(customer_id=1, product_id=2, quantity=3)
session.add(new_order)
session.commit()
