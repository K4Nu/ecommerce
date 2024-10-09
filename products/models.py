from django.db import models

class Product(models.Model):
    """Text choices can only have 2 values"""
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        CHILD_BOY = "B", "Child Boy"
        CHILD_GIRL = "G", "Child Girl"
        OTHER = "O", "Other"

    ADULT_SIZES = [
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "2X Large"),
    ]

    KID_SIZES = [
        ("XS", "Extra Small(4-5 years)"),
        ("S", "Small(6-7 years)"),
        ("M", "Medium(8-9 years)"),
        ("L", "Large(10-11 years)"),
        ("XL", "Extra Large(12-13 years)")
    ]
    name=models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=1, choices=Gender.choices, default=Gender.OTHER)
    size = models.CharField(max_length=3, blank=True)
    color = models.CharField(max_length=80)
    description = models.CharField(max_length=500)
    images = models.ImageField(upload_to="items")

    def get_size_choices(self):
        """Return size choices based on gender"""
        if self.gender in [self.Gender.CHILD_BOY, self.Gender.CHILD_GIRL]:
            return self.KID_SIZES
        else:
            return self.ADULT_SIZES

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
