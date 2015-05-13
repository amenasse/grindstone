from django.core.urlresolvers import reverse
from django.db import models


class Task(models.Model):

    NOT_STARTED = 'N'
    IN_PROGRESS = 'P'
    COMPLETE = 'C'

    STATUS_CHOICES = (
        (NOT_STARTED, 'Not started'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETE, 'Complete'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=4, choices=STATUS_CHOICES,
                              default=NOT_STARTED)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tasks:detail', args=[str(self.id)])
