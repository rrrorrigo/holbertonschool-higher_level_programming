#!/usr/bin/python3
"""script that creates the state California with the
City San Francisco from the database hbtn_0e_100_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import State, Base
from relationship_city import City
from sys import argv


if __name__ == '__main__':
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        queryInsert = State(name="California",
                            cities=[City(name="San Francisco")])
        session.add(queryInsert)
        session.commit()
        session.close()
