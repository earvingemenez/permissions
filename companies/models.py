from django.db import models


class Company(models.Model):
    """ company info
    """
    INACTIVE, ACTIVE = "inactive", "active"
    STATUSES = (
        (INACTIVE, "Inactive"),
        (ACTIVE, "Active"),
    )

    COUNTRY_USA, COUNTRY_INDIA, COUNTRY_CANADA = "usa", "india", "canada"
    COUNTRIES = (
        (COUNTRY_USA, "USA"),
        (COUNTRY_INDIA, "India"),
        (COUNTRY_CANADA, "Canada"),
    )

    company_type = models.ForeignKey('companies.CompanyType',
        related_name="companies", on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=30, choices=COUNTRIES, default=COUNTRY_USA)
    status = models.CharField(max_length=8, choices=STATUSES, default=INACTIVE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name}"


class CompanyType(models.Model):
    """ company type
    """
    desc = models.CharField(max_length=100)
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.desc}"