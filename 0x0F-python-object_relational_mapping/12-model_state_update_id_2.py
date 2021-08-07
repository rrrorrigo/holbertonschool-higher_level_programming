#!/usr/bin/python3
"""script that lists all State objects with the name passed as argument"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from sys import argv


if __name__ == '__main__':
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        up = session.query(State).filter_by(id=2)
        up.one().name = "New Mexico"
        session.commit()
        session.close()
