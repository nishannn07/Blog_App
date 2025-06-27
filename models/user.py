from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, DateTime, String
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    _email = Column('email', String, nullable=False)
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, value):
        """
        Validate email format and normalize.
        """
        cleaned = value.strip().lower()
        if '@' not in cleaned:
            raise ValueError("Invalid email address")
        self._email = cleaned
    def __repr__(self):
        return f"{self.id}, {self.username}, {self._email}"