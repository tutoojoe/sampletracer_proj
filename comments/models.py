from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import Style

# Create your models here.


class Comments(models.Model):
    class CommentType(models.TextChoices):
        INITIAL = 'INI', _('Initial Comments')
        GENERAL = 'GEN', _('General Comments')
        FITCOMMENTS = 'FIT', _('Fit Comments')
        SIZESETCOMMENTS = 'SSC', _('Size Set Comments')
        PPCOMMENTS = 'PPS', _('PP Sample Comments')

    style = models.ForeignKey(
        Style, related_name="comments", on_delete=models.CASCADE)
    comment_type = models.CharField(
        max_length=3, choices=CommentType.choices, default=CommentType.INITIAL)
    comments = models.TextField(_("Comments"), help_text=_(
        "Comments received from customer"))
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.style} | {self.comment_type}'

    class Meta:
        ordering = ["-created_at"]
