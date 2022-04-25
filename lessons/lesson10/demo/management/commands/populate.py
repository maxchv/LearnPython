from django.core.management import BaseCommand
from demo.models import Student
from faker import Faker
from random import randint


class Command(BaseCommand):
    help = 'Make fake students'

    def __init__(self):
        self.fake = Faker('uk_UA')

    def add_arguments(self, parser):
        parser.add_argument('count', nargs='+', type=int)

    def handle(self, *args, **options):
        counts = options['count']
        fake = self.fake
        for i in range(counts[0]):
            gender = Student.genders[randint(0, 2)]
            first_name = fake.first_name_female() if gender[0] == 'FEMALE' else fake.first_name_male()
            last_name = fake.last_name_female() if gender[0] == 'MALE' else fake.last_name_male()
            Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                birth_date=fake.date_between(start_date='-50y', end_date='-16y'),
                gender=gender[0]
            )
