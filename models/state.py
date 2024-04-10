#!/usr/bin/python3
"""State class"""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type
import models


class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Returns the list of City instances with state_id equals
            to the current State.id for FileStorage"""
            city_list = []
            all_cities = models.storage.all(models.City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
