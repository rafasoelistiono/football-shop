import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('boots', 'Boots'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
        ('merch', 'Merchandise'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='jersey')
    thumbnail = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    sales_count = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name

    @property
    def is_popular(self):
        """produk populer jika sudah terjual lebih dari 50 kali"""
        return self.sales_count > 50

    def increment_sales(self, amount=1):
        """Tambahkan jumlah penjualan"""
        self.sales_count += amount
        self.save()

