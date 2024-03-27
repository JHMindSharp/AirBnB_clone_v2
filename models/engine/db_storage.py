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
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)

        # Drop all tables if the environment is set to 'test'
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Recreate all tables in the database and establish the session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Query on the current database session all objects of a given class.
        If cls=None, query all types of objects."""
        all_objs = {}
        if cls is None:
            classes = [State, City]  # List all classes to query here
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f'{obj.__class__.__name__}.{obj.id}'
                    all_objs[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f'{cls.__name__}.{obj.id}'
                all_objs[key] = obj
        return all_objs

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """Dispose the session."""
        self.__session.close()