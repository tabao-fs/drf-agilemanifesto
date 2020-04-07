from django.utils.translation import gettext_lazy as _

from django.db import models


class TextType(models.TextChoices):
    VALUES = 'VAL', _('Values')
    PRINCIPLES = 'PRN', _('Principles')


class Messages(models.Model):

    title = models.CharField(max_length=256)
    text_type = models.CharField(
        max_length=3,
        choices=TextType.choices,
        default=TextType.VALUES,
    )
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
