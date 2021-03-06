# Generated by Django 3.2.9 on 2021-12-01 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seasapp', '0003_alter_department_t_deptid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_t',
            name='DeptID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seasapp.department_t'),
        ),
        migrations.AlterField(
            model_name='faculty_t',
            name='DeptID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seasapp.department_t'),
        ),
    ]
