# Generated by Django 2.2.6 on 2020-11-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201103_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Refrigerante', 'Refrigerante'), ('Frenos', 'Frenos'), ('Baterías', 'Baterías'), ('Sellador', 'Sellador')], max_length=200, null=True),
        ),
    ]
