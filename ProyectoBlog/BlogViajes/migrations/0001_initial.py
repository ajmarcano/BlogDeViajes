# Generated by Django 4.0.4 on 2022-05-26 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Destino', models.CharField(max_length=20)),
                ('Imagen', models.URLField()),
                ('Reseña', models.TextField(max_length=400)),
                ('Autor', models.CharField(max_length=20)),
            ],
        ),
    ]
