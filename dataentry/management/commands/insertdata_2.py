from django.core.management.base import BaseCommand
from dataentry.models import Student
# ^ =======================================================|

# todo -> I want to add some data to the database using the custom command

class Command(BaseCommand):
    help = "it will insert data to the database"

    def handle(self, *args, **kwargs):
        # logic goes here
        dataset = [
            {'roll_no': 1002, 'name': 'Lala', 'age':21},
            {'roll_no': 1012, 'name': 'Asdasa', 'age':22},
            {'roll_no': 1302, 'name': 'Varba', 'age':23}
        ]
        
        for data in dataset:
            print(data['name'])

            # Student.objects.create(roll_no=1001, name='Diego', age=39)
            # self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))

