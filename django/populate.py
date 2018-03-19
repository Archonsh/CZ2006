import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTut.settings')  # TODO
import django
django.setup()

import random
from compare.models import CompareList, Result
from faker import Faker


fakegen = Faker()
lists = []


def addName():
    t = CompareList.objects.get_or_create(name=random.choice(lists))[0]
    t.save()
    return t


def populate(n=5): # see the faker fakegen utility here!
    for entry in range(n):
        top = addName()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage = Webpage.objects.get_or_create(name=addName, date=fake_date)

if __name__=='__main__':
    print('Populate fake entries.')
    populate(20)
    print('Population complete.')
