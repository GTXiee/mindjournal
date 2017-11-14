from django.db import models
from django.utils import timezone

class JournalEntry(models.Model):
    author = models.ForeignKey('main.CustomUser')

    content = models.TextField(null=False, blank=False)
    image = models.ImageField(upload_to='img/journalentries', null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    actual_date = models.DateField(unique=True, null=False, blank=False)
    quote_author = models.CharField(max_length=30, null=True)
    quote_content = models.TextField(max_length=200, null=True)
    word_of_the_day = models.CharField(max_length=30, null=True)
    word_of_the_day_def = models.TextField(max_length=200, null=True)
    posture_changes = models.PositiveIntegerField(null=True)
