# Generated by Django 2.0.6 on 2018-10-04 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_quiz_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'permissions': (('can_create_new_quizz', 'Can create a new quizz'),)},
        ),
    ]
