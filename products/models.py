from django.db import models

class Product(models.Model):
    """Text choices can only have 2 values"""
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        CHILD_BOY = "B", "Child Boy"
        CHILD_GIRL = "G", "Child Girl"
        OTHER = "O", "Other"

    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    size = models.CharField(max_length=3, blank=True)
    color = models.CharField(max_length=80)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.gender} - {self.size}"

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="images")
    image=models.ImageField(upload_to="product_images/")

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)

    def get_full_category_path(self):
        categories = []
        category = self
        while category:
            categories.append(category.name)
            category = category.parent_category
        return "/".join(reversed(categories))

    def __str__(self):
        return f'{self.get_full_category_path()}'

class TestModel(models.Model):
    name=models.CharField(max_length=25)
    image=models.ImageField(upload_to="test")