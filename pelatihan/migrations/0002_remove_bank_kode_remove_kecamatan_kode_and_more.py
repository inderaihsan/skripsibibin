# Generated by Django 4.2.6 on 2023-10-29 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelatihan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='kode',
        ),
        migrations.RemoveField(
            model_name='kecamatan',
            name='kode',
        ),
        migrations.RemoveField(
            model_name='kelurahan',
            name='kode',
        ),
        migrations.AlterModelTable(
            name='bank',
            table='bank',
        ),
        migrations.AlterModelTable(
            name='kecamatan',
            table='kecamatan',
        ),
        migrations.AlterModelTable(
            name='kelurahan',
            table='kelurahan',
        ),
        migrations.AlterModelTable(
            name='pelatihan',
            table='pelatihan',
        ),
        migrations.AlterModelTable(
            name='pendaftaran',
            table='pendaftaran',
        ),
        migrations.AlterModelTable(
            name='peserta',
            table='peserta',
        ),
        migrations.AlterModelTable(
            name='rekening',
            table='rekening',
        ),
        migrations.AlterModelTable(
            name='status_pendaftaran',
            table='status_pendaftaran',
        ),
    ]
