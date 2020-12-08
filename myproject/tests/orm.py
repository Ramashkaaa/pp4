from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.dialects.mssql import BIT,DATETIME

Base = declarative_base()
metadata = Base.metadata
class User(Base):
   __tablename__ = 'User'

   id = Column(Integer,primary_key=True)
   username = Column(String)
   firstName = Column(String)
   lastName = Column(String)
   email = Column(String)
   password = Column(String)
   phone = Column(String)
   userRole=Column(Integer)
##   karma = Column(Integer)
class Note(Base):
   __tablename__ = 'Note'

   id = Column(Integer,primary_key=True)
   tag = Column(String)
   text = Column(String)
   numbofEditors = Column(Integer)

   def __init__(self,tag,text,url):
      self.tag = tag
      self.text = text
      self.photoUrl = url
class Edit(Base):
   __tablename__ = 'Edit'

   id = Column(Integer,primary_key=True)
   text  = Column(String)
   noteId  = Column(Integer,ForeignKey("Note.id"))
   userId  = Column(Integer,ForeignKey("User.id"))
   timeOfEdit = Column(DATETIME)

class NoteStatistic(Base):
   __tablename__ = 'NoteStatistic'

   id = Column(Integer,primary_key=True)
   noteId  = Column(Integer,ForeignKey("Note.id"))
   userId  = Column(Integer,ForeignKey("User.id"))
   timeOfEdit = Column(DATETIME)

class Allow(Base):
   __tablename__ = 'Allow'

   id = Column(Integer,primary_key=True)
   noteId  = Column(Integer,ForeignKey("Note.id"))
   userId  = Column(Integer,ForeignKey("User.id"))
   
engine = create_engine('mssql+pyodbc://PC0007/lab-2?driver=SQL+Server+Native+Client+11.0')

Base.metadata.create_all(engine)
##
##session.add(User(username="yurko",
##                 firstName="yuri",
##                 lastName="kryvenchuk",
##                 email="yurkO@lpnu",
##                 password="14881488",
##                 phone="15621562",
##                 userRole=3))
##session.commit()
