#!/usr/bin/python3
"""script that lists all State objects that contain the letter a"""
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
        for state in session.query(State).filter(State.name.ilike('%a%'))\
                                         .order_by(State.id).all():
            session.delete(state)
        session.commit()
        session.close()
