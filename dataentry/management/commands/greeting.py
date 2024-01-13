from django.core.management.base import BaseCommand
# ^ =======================================================|


# & proposed command = python manage.py greeting <Name>
# & proposed output = Hi {name}, good morning

class Command(BaseCommand):
    help = "Greets the user"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')
        

    def handle(self, *args, **kwargs):
        # we write the logic
        name = kwargs['name']
        greeting = f"Hi {name}, good morning !"
        # self.stdout.write(greeting)
        
        # ~ stderr -> print a error in red color:
        # self.stderr.write(greeting)

        # * success message:
        # self.stdout.write(self.style.SUCCESS(greeting))

        self.stdout.write(self.style.WARNING(greeting))
        # ^ warning message:
