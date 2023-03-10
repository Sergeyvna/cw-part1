# Generated by Django 4.1.2 on 2023-01-15 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_rep_acc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('num_of_block_tickets', models.IntegerField(choices=[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=200, null=True)),
                ('adress_details', models.CharField(max_length=200, null=True)),
                ('contact_details', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_name', models.CharField(max_length=200, null=True)),
                ('film_length', models.CharField(max_length=200, null=True)),
                ('ticket_price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
