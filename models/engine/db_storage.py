#!/usr/bin/python3
"""Defines the DBStorage class."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.base_model import Base
from models.city import City
from models.state import State

class DBStorage:
    """Represents a database storage engine."""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new DBStorage instance."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os
