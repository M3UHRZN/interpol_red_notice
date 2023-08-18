from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os


DATABASE_URL = "sqlite:///" + os.path.join(os.path.abspath(os.path.dirname(__file__)), "app.db")


Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    content = Column(String)

class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def save_message(self, timestamp, content):
        session = self.Session()
        message = Message(timestamp=timestamp, content=content)
        session.add(message)
        session.commit()
        session.close()

    def get_messages(self):
        session = self.Session()
        messages = session.query(Message).all()
        session.close()
        return messages
