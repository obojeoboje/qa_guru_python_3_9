import datetime
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


obojealexander = User(
    first_name='Aleksandr',
    last_name='Privalov',
    email='obojealexander@gmail.com',
    phone='1234567890',
    address='Saint Petersburg',
    birthday=date(1999, 5, 27),
    gender='Male',
    subject='Computer Science',
    hobbies='Music',
    image='picture.jpg',
    state='NCR',
    city='Delhi')
