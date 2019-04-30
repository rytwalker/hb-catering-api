from django.db import models
from uuid import uuid4
# Create your models here.


class MenuItem(models.Model):
    type_options = (('meat', 'meat'), ('side', 'side'), ('salad', 'salad'))

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    item_type = models.CharField(
        max_length=255, choices=type_options, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MeatItem(MenuItem):
    tier_options = (('1', 'Tier 1'), ('2', 'Tier 2'), ('3', 'Tier 3'))
    price_tier = models.CharField(
        max_length=1, choices=tier_options, null=True)
