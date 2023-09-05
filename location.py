from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class ProductLocation(Base):
    __tablename__ = 'product_locations'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
