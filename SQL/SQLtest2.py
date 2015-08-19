__author__ = 'tkessler'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, Float
from sqlalchemy.orm import sessionmaker

theEngine = create_engine("sqlite:///:memory:", echo=False)

BaseClass = declarative_base()

class Person(BaseClass):
    __tablename__="people"

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    firstname = Column('First',String(20))
    lastname = Column('Last',String(20))
    age = Column('Age',Integer)
    height = Column('Height',Float)
    weight = Column('Weight',Float)

    def __repr__(self):
        return "<first=%s\tlast=%s\tage=%s\theight=%s\tweight=%s>" % (self.firstname, self.lastname, str(self.age), str(self.height), str(self.weight))

# establish tables...call after table classes declared...
BaseClass.metadata.create_all(theEngine)

# instances of Person table --> each instance is a "row"
asdf = Person(age=45, firstname="Johnny", lastname="Tremain", height=62, weight=1792)
qwer = Person(firstname="Matt", height=59)


sessionconfig = sessionmaker()  # creates session class!!!
sessionconfig.configure(bind=theEngine)  # configures class
oursession = sessionconfig()  # instantiates class

oursession.add(asdf)  # adds class instance to static class table by name...
                      # the instance is "pending"...not written yet...


# retrieved = oursession.query(Person).filter_by(firstname="Johnny").first()  # query commits records

# if retrieved is asdf:
#     print("They are the same")

oursession.add_all([
    Person(age=32, firstname="Mary"),
    Person(age=29, lastname="Smithers", firstname="Joy", height=61.1, weight=172.9)
])

print("NEW ITEMS:\n", oursession.new)  # list newly added records
#
print("MODIFIED ITEMS:\n", oursession.dirty)  # list altered records

# for instance in oursession.query(Person):
#     print(instance.firstname, instance.lastname)

print("Not committed: ", asdf.id)
oursession.commit()  # commit all modifications
print("Comitted: ", asdf.id)

# oursession.delete(asdf)
# oursession.commit()
theQuery = oursession.query(Person)
# theQuery.filter_by(firstname="Johnny")

print(theQuery)
