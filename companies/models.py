from django.db import models


class Company(models.Model):
    """ company info
    """
    PARENT_COMPANY, SUBSIDIARY = "parent_company", "subsidiary"
    TYPES = (
        (PARENT_COMPANY, "Parent Company"),
        (SUBSIDIARY, "Subsidiary"),
    )

    INACTIVE, ACTIVE = "inactive", "active"
    STATUSES = (
        (INACTIVE, "Inactive"),
        (ACTIVE, "Active"),
    )

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=30, null=True, blank=True)
    type = models.CharField(max_length=15, choices=TYPES, default=SUBSIDIARY)
    status = models.CharField(max_length=8, choices=STATUSES, default=INACTIVE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"({self.get_type_display()}) {self.name}"