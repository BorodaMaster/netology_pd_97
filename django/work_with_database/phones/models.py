from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, null=False)
    image = models.ImageField(max_length=255, null=False)
    release_date = models.DateField(max_length=10, null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=25, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
