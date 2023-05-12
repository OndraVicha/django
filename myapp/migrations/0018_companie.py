# Generated by Django 4.2 on 2023-05-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_tank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a company name', max_length=50, unique=True, verbose_name='Company')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Info')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
