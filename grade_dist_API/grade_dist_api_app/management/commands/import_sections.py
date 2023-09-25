# dataimport/management/commands/import_sections.py
import csv
from django.core.management.base import BaseCommand
from grade_dist_api_app.models import Section  # Import your Section model here

class Command(BaseCommand):
    help = 'Import sections from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                section = Section(
                    semester=row['semester'],
                    year=row['year'],
                    subject_code = row['subject_code'], 
                    course_code=row['course_number'],
                    section_code=row['section_number'],
                    professor_name=row['professor_name'],
                    a_count=row['a'],
                    b_count=row['b'],
                    c_count=row['c'],
                    d_count=row['d'],
                    f_count=row['f'],
                    q_count=row['q'],
                    i_count=row['i'],
                    s_count=row['s'],
                    u_count=row['u'],
                    x_count=row['x'],
                )
                section.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully imported section: {section}'))
