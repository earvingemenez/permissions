from django.db import models


class Vendor(models.Model):
    """ vendor info
    """
    company = models.OneToOneField('companies.Company',
        related_name="vendor", on_delete=models.CASCADE)
    vendor_type = models.ForeignKey('vendors.VendorType',
        related_name="vendors", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class VendorType(models.Model):
    """ vendor type
    """
    name = models.CharField(max_length=100)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"