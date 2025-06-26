from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username  = Column(String)
    _email = Column(String)

    @property
    def getEmail(self):
        return self._email
    
    @getEmail.setter
    def setEmail(self, email):
        if '@' not in email:
            raise ValueError("Wrong Email format")
        
        self._email = email
    
    def __repr__(self):
        return f"{self.id}, {self.username}, {self._email}"