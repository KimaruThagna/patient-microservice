import uuid

import django
from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone


class BaseQueryset(QuerySet):
    """
    define custom queryset methods that can be chained for desired effect
    """

    def not_deleted(self) -> QuerySet:
        """
        :return:  A filtered queryset where the is_deleted flag is False
        """
        return self.filter(is_deleted=False)


class BaseManager(models.Manager):
    """
    override the get_queryset functions to return our custom queryset.
    """

    def get_queryset(self) -> BaseQueryset:
        """
        :return: custom queryset BaseQueryset
        """
        return BaseQueryset(self.model)

class BaseModel(models.Model):

    objects = BaseManager()

    indexing_id = models.AutoField(primary_key=True)

    # uuid4 field for retrieval, this field should also be indexed
    uid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)


    class Meta:
        abstract = True

    def soft_delete(self):

        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def activate(self):
        self.is_active = True
        self.save()

    def deactivate(self):
        self.is_active = False
        self.save()

