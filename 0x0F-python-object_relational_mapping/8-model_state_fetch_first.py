#!/usr/bin/python3
"""script that lists all State objects"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from sys import argv


if __name__ == '__main__':
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        for state in session.query(State).order_by(State.id).all():
                print("{}: {}".format(state.id, state.name))
                break
        else:
                print("Nothing")
        session.close()
