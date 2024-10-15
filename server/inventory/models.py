from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class NFC(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=50)
    created_at = models.DateField()

    def __str__(self):
        return f'{self.id}'


class ProductImage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='product_images/')
    upload_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.image}'
    

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.OneToOneField(
        ProductImage,
        on_delete=models.SET_NULL, null=True
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    stock = models.IntegerField()
    NFC = models.ForeignKey(NFC, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
