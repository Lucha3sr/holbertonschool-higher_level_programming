#!/usr/bin/python3

"""script that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@MY_HOST/{}'
                           .format(MY_USER, MY_PASS, MY_DB))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for i in session.query(State).order_by(State.id):
        print('{}: {}'.format(i.id, i.name))
    session.close()
