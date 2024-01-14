from django.core.management.base import BaseCommand, CommandParser
from dataentry.models import Student
import csv
# ^ ==============================================================================|

# * proposed command - python manage.py importdata <file_path>


class Command(BaseCommand):
    help = "Import data from CSV file"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the CSV file")
        

    def handle(self, *args, **kwargs):
        # logic goes here
        file_path = kwargs['file_path']
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # print(reader)

            for row in reader:
                # print(row)
                
                Student.objects.create(**row)


        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully! '))