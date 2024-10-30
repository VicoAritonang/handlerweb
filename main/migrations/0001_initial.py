# Generated by Django 5.1.2 on 2024-10-30 09:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulir',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('nomor', models.IntegerField()),
                ('jenis_usaha', models.CharField(choices=[('fnb', 'Makanan dan Minuman'), ('material', 'Material'), ('raw', 'Bahan Makanan'), ('pakaian', 'Pakaian'), ('craft', 'Kerajinan'), ('lainnya', 'Lainnya, Jelaskan di deskripsi')], max_length=20)),
                ('omzet', models.CharField(choices=[('mikro', 'Mikro : (Omzet bulanan hingga Rp 10 Juta )'), ('kecil', 'Kecil : (Omzet bulanan Rp 10 Juta - Rp 100 Juta )'), ('menengah', 'Menengah : (Omzet bulanan Rp 100 Juta - Rp 500 Juta )'), ('besar', 'Besar : (Omzet bulanan lebih dari Rp 500 Juta )')], max_length=20)),
                ('deskripsi', models.TextField()),
            ],
        ),
    ]
