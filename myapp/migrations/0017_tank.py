# Generated by Django 4.2 on 2023-05-12 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_delete_companie_delete_crew_remove_tank_genres_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank', models.CharField(help_text='Enter a tank name', max_length=200, verbose_name='Tank')),
                ('history', models.TextField(blank=True, null=True, verbose_name='History')),
                ('creation_date', models.DateField(blank=True, help_text='Please use the following format: <em>YYYY\x02MM-DD</em>.', null=True, verbose_name='First tank made')),
                ('tank_type', models.CharField(blank=True, choices=[('light tank', 'Light tank'), ('medium tank', 'Medium tank'), ('heavy tank', 'Heavy tank'), ('tank destroyer', 'Tank destroyer'), ('anti air tank', 'Anti air tank')], help_text='Select allowed attachment type', max_length=15, verbose_name='Tank type')),
            ],
            options={
                'ordering': ['-creation_date', 'tank'],
            },
        ),
    ]
