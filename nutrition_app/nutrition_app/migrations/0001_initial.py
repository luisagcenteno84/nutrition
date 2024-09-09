# Generated by Django 5.1.1 on 2024-09-09 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patientId', models.IntegerField()),
                ('doctorId', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patientId', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('weight_uom', models.CharField(max_length=20)),
                ('bmi', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fat_pct', models.DecimalField(decimal_places=1, max_digits=4)),
                ('muscle_pct', models.DecimalField(decimal_places=1, max_digits=4)),
                ('v_fat', models.DecimalField(decimal_places=1, max_digits=4)),
                ('waist', models.DecimalField(decimal_places=1, max_digits=5)),
                ('hip', models.DecimalField(decimal_places=1, max_digits=5)),
                ('length_uom', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('measurementId', models.IntegerField()),
                ('appointmentId', models.IntegerField()),
                ('plan_detail', models.CharField(max_length=200)),
            ],
        ),
    ]