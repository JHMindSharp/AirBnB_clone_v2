#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Amenity(BaseModel, Base):
    """Represents an amenity for a MySQL database."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
