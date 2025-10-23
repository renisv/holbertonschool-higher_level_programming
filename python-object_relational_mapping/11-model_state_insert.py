#!/usr/bin/python3
"""
Start link class to table in database
"""


import sys
from model_state import Base, State
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
    results = session.query(State.id)\
                     .where(State.name == 'Louisiana')\
                     .all()

    if len(results) > 0:
        for row in results:
            print(row.id)
    else:
        print("Not found")
    session.close()
