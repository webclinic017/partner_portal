from django.db import models


class CustomerUser(models.Model):
    username = models.CharField(verbose_name='usuário', max_length=255, unique=True)
    password = models.CharField(verbose_name='senha', max_length=255)

    def __str__(self):
        return "{} - {}".format(self.username, self.password)