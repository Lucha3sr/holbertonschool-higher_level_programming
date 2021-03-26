#!/usr/bin/python3

"""python file that contains the class definition of a State
 and an instance Base = declarative_base()"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":

    MY_HOST = "localhost"
    MY_USER = argv[1]
    MY_PASS = argv[2]
    MY_DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@MY_HOST/{}'
                           .format(MY_USER, MY_PASS, MY_DB)
    Base.metadata.create_all(engine)
