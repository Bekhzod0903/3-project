from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)



    class Meta:
        db_table = 'category'

    def __str__(self) -> str:
        return f'{self.name}'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    make = models.CharField(max_length=100)
    body = models.TextField()
    price = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/products', blank=True, null=True)

    class Meta:
        db_table = 'Product'

    def __str__(self) -> str:
        return f"{self.category.name} {self.model}"
