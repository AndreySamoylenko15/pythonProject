from sqlalchemy import Date, create_engine, Column, Integer, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, backref
from db import Base, engine
from datetime import date



class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    birthday = Column(Date)
    extra_data = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=True)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user = relationship('User', backref= 'contacts', lazy='joined')


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



# Створення таблиці в базі даних
Base.metadata.create_all(bind=engine)