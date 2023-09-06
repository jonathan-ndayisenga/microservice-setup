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