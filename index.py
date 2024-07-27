from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

my_engine = create_engine("sqltite://ex.db")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column (Integer)
    


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
Session = Session()

new_user = User(name='Bob', age= 30)
Session.add(new_user)
Session.commit()

user = session.query(User).all()
print(users.fetchall)