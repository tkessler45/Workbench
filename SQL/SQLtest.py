__author__ = 'tkessler'

from sqlalchemy import create_engine
from sqlalchemy import Sequence  # foolproof...
engine = create_engine('sqlite:///testsqlite.db', echo=False)

# declare object relational mapping
    # 1. Create database tables...delcare base

from sqlalchemy.ext.declarative import declarative_base # describe tables and map classes...?

Base = declarative_base()  # base class defined...can map data classes using it

from sqlalchemy import Column, Integer, String

class User(Base):  # map new table class to sqlalchemy base class:
    __tablename__= "users"  # required for a declarative base class --> values assigned to this table in engine...

    # __init__() method supplied by declarative_base()

    # at least one column required...
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True) # Sequence = foolproof...
    name = Column(String(20))
    fullname = Column(String(50))
    password = Column(String(15))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

# get info on objects...
# User.__table__
Base.metadata.create_all(engine)

# Instance of data class...in memory only
a_user = User(name="Topher", fullname="Christopher Kessler",password="asdfasdfasdf")
b_user = User(name="Topher", fullname="Topher Grace", password="qwerwerqwerqwer")
print(a_user.fullname)
print(b_user.fullname)

# Create a session --> talk to the DB
from sqlalchemy.orm import sessionmaker

newSession = sessionmaker(bind=engine)()  # declare class maker instance, and instantiate it.
# or...
# theSession = sessionmaker(bind=engine) #create class instance...
# theSession = sessionmaker()
# theSession.configure(bind=engine)
# newSession = theSession()

# print("THESESSION")
# print(theSession)
# print("NEWSESSION")
# print(newSession)

newSession.add(a_user)
# retrievedUser = newSession.query(User).filter_by(name='Topher').first()
# print(retrievedUser)
# retrievedUser.password = 'wahoo'
# print(newSession.dirty)

newSession.commit()