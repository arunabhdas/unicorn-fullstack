from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.CharField(max_length=200, primary_key=True)
    name=models.CharField(max_length=200)
    sku=models.CharField(max_length=200)
    description=models.TextField()
    slug=models.SlugField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Entry #{}'.format(self.id)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ["name", "created_at"]
