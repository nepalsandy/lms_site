# Generated by Django 3.2.7 on 2021-09-22 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='pdf',
            field=models.FileField(null=True, upload_to='books/pdf'),
        ),
    ]