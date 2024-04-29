# Generated by Django 4.2 on 2024-04-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('quali', models.CharField(max_length=50)),
                ('spec', models.CharField(max_length=50)),
                ('hname', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=50)),
                ('pass1', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=50)),
                ('rname', models.CharField(max_length=50)),
                ('addr', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('bgroup', models.CharField(max_length=50)),
                ('organ', models.CharField(max_length=50)),
                ('occ', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('ddate', models.CharField(max_length=50)),
                ('st', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('dob', models.CharField(max_length=50)),
                ('place', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('pcode', models.CharField(max_length=50)),
                ('cno', models.CharField(max_length=50)),
                ('bgroup', models.CharField(max_length=50)),
                ('organ', models.CharField(max_length=50)),
                ('dname', models.CharField(max_length=50)),
                ('demail', models.CharField(max_length=50)),
                ('hname', models.CharField(max_length=50)),
                ('st', models.CharField(max_length=50)),
                ('hash', models.CharField(max_length=500)),
            ],
        ),
    ]