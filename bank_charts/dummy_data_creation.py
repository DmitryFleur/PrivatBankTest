from .models import DummyData
from faker import Faker
from random import randint


def load_dummy_data(records_number):
    fake = Faker()
    done = False
    for _ in range(records_number):
        DummyData(date=fake.date_this_year(before_today=True, after_today=False),
                  first_value=randint(1, 100),
                  second_value=randint(1, 100)).save()
        done = True
    return done
