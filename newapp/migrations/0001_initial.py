# Generated by Django 4.2 on 2023-04-13 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('employee_DOB', models.DateField()),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('DOJ', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='leavetype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type_name', models.CharField(max_length=200)),
                ('no_of_days_allowed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_name', models.CharField(max_length=20)),
                ('shift_code', models.CharField(max_length=20)),
                ('check_in_time', models.TimeField()),
                ('check_out_time', models.TimeField()),
                ('grace_time', models.CharField(max_length=10)),
                ('total_hours', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='leave_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_application', models.DateField()),
                ('l_from', models.DateField()),
                ('l_to', models.DateField()),
                ('no_of_days', models.IntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('leave_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.leavetype')),
                ('lemployee_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='employee_shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('employee_name_shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.employee')),
                ('shift_allocated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.shift')),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=200)),
                ('Employee_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('Employee_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.employee')),
                ('shift_of_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.shift')),
            ],
        ),
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200)),
                ('IFSC', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('account_type', models.CharField(max_length=200)),
                ('acc_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.employee')),
            ],
        ),
    ]
