from django.db import migrations
from crm.models import CrimeCategory, Crime

def initialize_data(apps, schema_editor):
    # Initialize crime categories
    CrimeCategory.initialize_categories()

    # Initialize crimes
    Crime.initialize_crimes()

class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_remove_reportingofficer_office_location_and_more'),  # Replace with the last migration file's name
    ]

    operations = [
        migrations.RunPython(initialize_data),
    ]
