# Generated by Django 3.2.9 on 2021-12-02 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_postarray'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postarray',
            old_name='content',
            new_name='text',
        ),
    ]
