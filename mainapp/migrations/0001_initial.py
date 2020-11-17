# Generated by Django 3.1.3 on 2020-11-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.IntegerField()),
                ('status', models.CharField(choices=[('Applied', 'Admission applied'), ('Admit', 'Admitted')], default='Applied', max_length=10)),
                ('number', models.CharField(default='-', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Electronics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.IntegerField()),
                ('status', models.CharField(choices=[('Applied', 'Admission applied'), ('Admit', 'Admitted')], default='Applied', max_length=10)),
                ('number', models.CharField(default='-', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.IntegerField()),
                ('status', models.CharField(choices=[('Applied', 'Admission applied'), ('Admit', 'Admitted')], default='Applied', max_length=10)),
                ('number', models.CharField(default='-', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mechanical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('percentage', models.IntegerField()),
                ('status', models.CharField(choices=[('Applied', 'Admission applied'), ('Admit', 'Admitted')], default='Applied', max_length=10)),
                ('number', models.CharField(default='-', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
