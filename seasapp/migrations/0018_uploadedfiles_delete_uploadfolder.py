# Generated by Django 4.0 on 2021-12-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0017_uploadfolder'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadedfiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_to_upload', models.FileField(upload_to='Resources/')),
            ],
        ),
        migrations.DeleteModel(
            name='uploadfolder',
        ),
    ]
