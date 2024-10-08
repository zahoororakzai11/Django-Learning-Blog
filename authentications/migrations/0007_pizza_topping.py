# Generated by Django 3.2 on 2024-09-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentications', '0006_alter_student_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('toppings', models.ManyToManyField(to='authentications.Topping')),
            ],
        ),
    ]
