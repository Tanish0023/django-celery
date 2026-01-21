from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
  help = "Description"
  
  def handle(self, *args, **options):
    self.stdout.write("This is my command")
    # return super().handle(*args, **options)