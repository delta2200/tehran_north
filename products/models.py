from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    technical_desc = models.TextField()
    activate = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"id": self.id})
    




