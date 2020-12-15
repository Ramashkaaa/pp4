from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata


class Note(Base):
    __tablename__ = 'Note'

    id = Column(Integer)
    tag = Column(String, primary_key=True)
    text = Column(String, primary_key=True)
    numberofEditors = Column(Integer)


class Edit(Base):
    __tablename__ = 'Edit'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    article_id = Column(Integer)
    user_id = Column(Integer)
    TimeOfEditing = Column(String)


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    phone = Column(String)


class NoteStatistic(Base):
    __tablename__ = 'NoteStatictic'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, primary_key=True)
    note_id = Column(Integer, primary_key=True)
    time = Column(String, primary_key=True)


class Allow(Base):
    __tablename__ = 'Allow'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    id_note = Column(Integer)


engine = create_engine("postgres://postgres:postgres@localhost/obeme")
Base.metadata.create_all(engine)

"""Session = sessionmaker(engine)
session = Session()
session.add(User(username="username",
                 firstName="fName",
                 lastName="lName",
                 email="email@lpnu",
                 password="228b1337",
                 phone="88005553535",))
session.commit()"""

print(User.__table__)
