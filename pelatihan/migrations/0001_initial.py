# Generated by Django 4.2.6 on 2023-10-29 08:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=221)),
                ('nama', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=221)),
                ('nama', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=221)),
                ('nama', models.CharField(max_length=221)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.kecamatan')),
            ],
        ),
        migrations.CreateModel(
            name='Pelatihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=221)),
                ('kode_pelatihan', models.CharField(max_length=221)),
                ('keterangan', models.CharField(max_length=221)),
                ('lokasi', models.CharField(max_length=221)),
                ('tanggal_mulai', models.DateTimeField()),
                ('tanggal_selesai', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Peserta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=221)),
                ('no_kontak', models.CharField(max_length=221)),
                ('nik', models.CharField(max_length=221)),
                ('no_kk', models.CharField(max_length=221)),
                ('pendidikan', models.CharField(max_length=221)),
                ('tempat_lahir', models.CharField(max_length=221)),
                ('tanggal_lahir', models.CharField(max_length=221)),
                ('status', models.CharField(max_length=221)),
                ('pekerjaan', models.CharField(max_length=221)),
                ('alamat', models.CharField(max_length=221)),
                ('keterangan', models.CharField(max_length=221)),
                ('kelurahan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.kelurahan')),
            ],
        ),
        migrations.CreateModel(
            name='Status_pendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_status', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='Rekening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_rekening', models.CharField(max_length=221)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.bank')),
                ('peserta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.peserta')),
            ],
        ),
        migrations.CreateModel(
            name='Pendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registered_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('pelatihan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.pelatihan')),
                ('peserta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.peserta')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pelatihan.status_pendaftaran')),
            ],
        ),
    ]
