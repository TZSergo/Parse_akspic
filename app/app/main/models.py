from django.db import models


class Images(models.Model):
    link = models.TextField('Link')
    desk = models.TextField('Desk')
    category = models.TextField('Category')

    def __str__(self):
        return self.link
