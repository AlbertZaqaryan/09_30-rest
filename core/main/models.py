from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField('Phone name', max_length=30)
    price = models.IntegerField('Phone price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
