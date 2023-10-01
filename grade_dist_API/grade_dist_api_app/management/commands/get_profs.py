# myapp/management/commands/reset_db.py
from django.core.management.base import BaseCommand
from django.db import connection

from grade_dist_api_app.models import Section
import csv

class Command(BaseCommand):
    help = 'Reset the database (delete all data)'

    def handle(self, *args, **options):
        professor_names = Section.objects.values_list('professor_name', flat=True).distinct()
        with open('professors.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)


            for professor_name in professor_names:
                csv_writer.writerow([professor_name])

        
