import sqlalchemy
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Sequence, ForeignKey, Table

engine = create_engine('postgresql://localhost/sqlalchemy_pets', echo=True)
Base = declarative_base()

pet_toys = Table('pet_toys', Base.metadata, 
    Column('toy_id', ForeignKey('toys.id'), primary_key=True),
    Column('pet_id', ForeignKey('pets.id'), primary_key=True)
)

class User(Base):
  __tablename__= 'users'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String, unique=True)
  nickname = Column(String(50))

  pets = relationship('Pet', back_populates='user', cascade='all, delete, delete-orphan')

  def __repr__(self):
    return f'🌝<User(id={self.id}, name={self.name}, email={self.email}, nickname={self.nickname})>'

class Pet(Base):
  __tablename__ = 'pets'

  id = Column(Integer, Sequence('pet_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  species = Column(String, nullable=False)
  age = Column(Integer)
  user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

  user = relationship('User', back_populates='pets')
  toys = relationship('Toy', secondary=pet_toys, back_populates='pets')

  def __repr__(self):
    return f'🦚<Pet(id={self.id}, name={self.name}, species={self.species}, age={self.age}, user_id={self.user_id})>'

class Toy(Base):
  __tablename__ = 'toys'

  id = Column(Integer, Sequence('toy_id_seq'), primary_key=True)
  item = Column(String, nullable=False, unique=True)

  pets = relationship('Pet', secondary=pet_toys, back_populates='toys')

  def __repr__(self):
    return f'🧳<Toy(id={self.id}, item={self.item})>'

# Migrates everything
Base.metadata.create_all(engine)