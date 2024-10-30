from django.db import models
import uuid

class Formulir(models.Model):
    JENIS_USAHA = [
        ('fnb', 'Makanan dan Minuman'),
        ('material', 'Material'),
        ('raw', 'Bahan Makanan'),
        ('pakaian', "Pakaian"),
        ('craft', "Kerajinan"),
        ('lainnya', "Lainnya, Jelaskan di deskripsi")
    ]
    OMZET = [
        ('mikro', 'Mikro : (Omzet bulanan hingga Rp 10 Juta )'),
        ('kecil', 'Kecil : (Omzet bulanan Rp 10 Juta - Rp 100 Juta )'),
        ('menengah', 'Menengah : (Omzet bulanan Rp 100 Juta - Rp 500 Juta )'),
        ('besar', 'Besar : (Omzet bulanan lebih dari Rp 500 Juta )'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=50)
    nomor = models.IntegerField()
    jenis_usaha = models.CharField(max_length=20, choices=JENIS_USAHA)
    omzet = models.CharField(max_length=20, choices=OMZET)
    deskripsi = models.TextField()
    
