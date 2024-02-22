# Generated by Django 5.0.2 on 2024-02-22 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KudaGo', '0002_alter_company_fri_end_alter_company_fri_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='mon_end',
            field=models.TimeField(blank=True, null=True, verbose_name='Понедельник, время закрытия'),
        ),
        migrations.AlterField(
            model_name='company',
            name='mon_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Понедельник, время открытия'),
        ),
    ]