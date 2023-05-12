# Generated by Django 4.2 on 2023-05-12 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a country from where is the tank', max_length=50, unique=True, verbose_name='Country')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AlterField(
            model_name='serial',
            name='genres',
            field=models.ManyToManyField(help_text='Select a genre for this serial', to='myapp.country'),
        ),
    ]
