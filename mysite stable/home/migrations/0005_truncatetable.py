# Generated by Django 4.0.6 on 2023-04-12 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_values'),
    ]

    operations = [
        migrations.CreateModel(
            name='truncatetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'truncatetable',
            },
        ),
    ]