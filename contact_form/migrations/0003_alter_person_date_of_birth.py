# Generated by Django 4.0.4 on 2022-05-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0002_emails_only_person_date_of_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(max_length=10),
        ),
    ]
