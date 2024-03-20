#!/usr/bin/python3
""" database storage module"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review

from sqlalchemy.orm import sessionmaker


class DBStorage:
    """database storage class """
    __engine = None
    __session = None

    def __init__(self):
        """ create engine """
        host = getenv("HBNB_MYSQL_HOST")
        usr = getenv("HBNB_MYSQL_USER")
        db = getenv("HBNB_MYSQL_DB")
        pswd = getenv("HBNB_MYSQL_PWD")
        url = "mysql+mysqldb://{}:{}@{}/{}".format(usr, pswd, host, db)
        self.__engine = create_engine(url, pool_pre_ping=True)

        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database for provided class or all classes"""
        all_classes = [State, City, User, Place, Review]
        obj_dict = {}
        if cls:
            result = self.__session.query(cls)
            for obj in result:
                key = type(obj).__name__ + "." + obj.id
                obj_dict[key] = obj
            return obj_dict
        for clss in all_classes:
            result = self.__session.query(clss)
            for obj in result:
                key = type(obj).__name__ + "." + obj.id
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ add new object to table"""
        self.__session.add(obj)

    def save(self):
        """ commit the changes to database """
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from table in current session"""
        self.__session.delete(obj)

    def reload(self):
        """ create all table in current session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = session()
