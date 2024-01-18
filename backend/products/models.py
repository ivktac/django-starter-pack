from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    objects = models.Manager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * self.get_discount())

    def get_discount(self):
        return 0.8