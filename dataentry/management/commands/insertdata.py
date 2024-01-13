from django.core.management.base import BaseCommand
from dataentry.models import Student
# ^ =======================================================|

# todo -> I want to add some data to the database using the custom command

class Command(BaseCommand):
    help = "it will insert data to the database"

    def handle(self, *args, **kwargs):
        # logic goes here
        # add 1 data:
        Student.objects.create(roll_no=1001, name='Diego', age=39)
        self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))

