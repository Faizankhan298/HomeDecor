from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Furniture', 'Furniture'),
        ('Home Décor', 'Home Décor'),
        ('Textiles', 'Textiles & Soft Furnishings'),
        ('Bedding', 'Bedding'),
        ('Kitchen', 'Kitchen & Dining'),
        ('Bathroom', 'Bathroom Accessories'),
        ('Storage', 'Storage & Organization'),
        ('Lighting', 'Lighting'),
        ('Outdoor', 'Outdoor Furnishings'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    embedded_image = models.TextField()  # To store the embedded 3D image link

    def __str__(self):
        return self.title
