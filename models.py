from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from main import db

class FakeData(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rand = db.Column(db.Integer)
    time = db.Column(db.DateTime)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'modified_at': self.time,
           'rand'  : self.rand
       }