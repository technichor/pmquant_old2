from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.EmailField()
    elo_score = models.SmallIntegerField(default=1500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    release = models.CharField(max_length=10, blank=True)
    s_in_review = 0
    s_open = 1
    s_rejected = 2
    s_completed = 3
    s_choices = (
        (s_in_review, _('In Review')),
        (s_open, _('Open')),
        (s_rejected, _('Rejected')),
        (s_completed, _('Completed')),
    )
    status = models.PositiveSmallIntegerField(
        choices=s_choices,
        default=s_in_review,
    )
    def __str__(self):
        return self.title