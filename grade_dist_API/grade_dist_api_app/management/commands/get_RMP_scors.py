# myapp/management/commands/reset_db.py
from django.core.management.base import BaseCommand
from django.db import connection

from grade_dist_api_app.models import Section
import csv

class Command(BaseCommand):
    help = 'Reset the database (delete all data)'

    def handle(self, *args, **options):
        with open('professors.csv', 'r', newline='') as csvfile:
            csv_writer = csv.reader(csvfile)



        
