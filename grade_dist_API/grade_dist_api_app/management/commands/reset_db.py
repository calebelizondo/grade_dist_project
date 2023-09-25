# myapp/management/commands/reset_db.py
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the database (delete all data)'

    def handle(self, *args, **options):
        # Drop all tables in the SQLite database
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA writable_schema = 1;")
            cursor.execute("DELETE FROM sqlite_master WHERE type='table';")
            cursor.execute("PRAGMA writable_schema = 0;")
            cursor.execute("VACUUM;")
        self.stdout.write(self.style.SUCCESS('Database reset successfully'))
