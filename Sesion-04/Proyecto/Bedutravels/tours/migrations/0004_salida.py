# Generated by Django 2.2.2 on 2019-08-22 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('asientos', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salidas', to='tours.Tour')),
            ],
        ),
    ]
