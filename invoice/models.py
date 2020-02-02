from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=256, blank=False)
    gst = models.CharField(max_length=100, blank=False, unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    company = models.ForeignKey(to=Company, related_name='%(class)s_company', on_delete=models.PROTECT)
    cost = models.FloatField(blank=False, default=0)
    creation_date = models.DateTimeField(auto_now_add=True)


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=255, blank=False, unique=True)
    company = models.ForeignKey(to=Company, related_name='%(class)s_company', on_delete=models.PROTECT)
    product = models.ForeignKey(to=Product, related_name='%(class)s_product', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    total_price = models.FloatField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
