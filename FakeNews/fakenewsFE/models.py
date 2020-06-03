from django.db import models

# Create your models here.


class Article(models.Model):

    article = models.CharField(max_length=1000)

    def __str__(self):
        return self.article


class Output(models.Model):
    value = models.CharField(max_length=1000)

    class Meta:
        verbose_name = ('Output')
        verbose_name_plural = ('Outputs')

    def __str__(self):
        return self.value
