#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(
                                sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True
                        )
    Base.metadata.create_all(eng)

    session = Session(bind=eng)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    results = session.query(State.name, City.id, City.name)\
                     .join(City)\
                     .order_by(City.id)\
                     .all()
    for row in results:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    session.close()
