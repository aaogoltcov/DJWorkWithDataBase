import uuid

from django.db import models
from django.db.models import BooleanField
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    release_date = models.DateField()
    lte_exists = BooleanField()
    slug = models.SlugField(default=name)


    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('product', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)