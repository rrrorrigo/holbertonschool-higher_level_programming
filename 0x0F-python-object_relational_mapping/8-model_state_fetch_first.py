#!/usr/bin/python3
"""script that lists all State objects"""
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
        state = session.query(State).order_by(State.id).first()
        if state:
                print("{}: {}".format(state.id, state.name))
        else:
                print("Nothing")
        session.close()
