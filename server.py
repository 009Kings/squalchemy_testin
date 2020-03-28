import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import engine, User, Pet, Toy

Session = sessionmaker(bind=engine)

def user_crud():
  session = Session()

  # Create
  tosspot = User(name='Gavin Callander', 
    email='gavin.callander@generalassemb.ly',
    nickname='Gav')
  
  session.add(tosspot)
  session.add_all([
    User(name='Wendy Williams', email='windywendy@gmail.com', nickname='WW'),
    User(name='Steven Peters', email='stpets@bigdaddybezos.com', nickname='Stpets'),
    User(name='Michael Schull', email='vashonbum@gmail.com', nickname='Mike'),
    User(name='Madison Edmiston', email='madison.edmiston@ga.co', nickname='Mads')
  ])

  # Read
  go_to_gal = session.query(User).filter_by(nickname='Mads').first()
  go_to_gal.email = 'madison.edmiston@generalassemb.ly'

  # DESTROY
  session.delete(tosspot)
  session.query(User).filter_by(nickname="WW").delete()

  session.commit()

def pet_crud():
  session = Session()
  
  go_to_gal = session.query(User).filter_by(nickname='Mads').first()
  go_to_gal.pets = [Pet(name='Emmy', species='dog', age=2)]
  # emmy = session.query(Pet).filter_by(name='Emmy').first()
  go_to_gal.pets += [Pet(name='Blub', species='fish')]

  # print(go_to_gal.pets)
  # session.delete(go_to_gal)
  # print(session.query(Pet).filter_by(name='Emmy').count())

  session.commit()

def toy_crud():
  session = Session()

  a_user = session.query(User).first()
  print(a_user)
  emmy = session.query(Pet).filter_by(name='Emmy').first()
  emmy.toys = [Toy(item='ball')]
  emmy.toys.append(Toy(item='squeeky duck'))

  print(emmy.toys)
  session.commit()

def user_query(id):
  session = Session()

  user = session.query(User).filter_by(id=id).first()
  print("🥼")
  print(user)

if __name__ == '__main__':
  user_query(25)