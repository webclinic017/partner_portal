from django.db import models


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True, verbose_name='ativo?')
    is_excluded = models.BooleanField(default=False, verbose_name='excluido?')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='atualizado em')

    class Meta:
        abstract = True