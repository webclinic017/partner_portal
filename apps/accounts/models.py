from django.contrib.auth.models import User
from django.db import models
from apps.core.models import BaseModel



class Partner(BaseModel):
    title = models.CharField(verbose_name='parceiro', max_length=255)
    erp_contract_code = models.CharField(
        verbose_name='codigo do contrato no erp', 
        max_length=10, 
        blank=True, 
        null=True
    )

    class Meta:
        verbose_name = 'parceiro (empresa)'
        verbose_name_plural = 'parceiros (empresa)'
        ordering = ('created_at',)

    def __str__(self):
        return self.title



class MonitorNetwork(BaseModel):
    partner = models.ForeignKey(Partner, verbose_name='parceiro', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='descrição', max_length=255)
    link = models.CharField(verbose_name='link do mapa', max_length=255)

    class Meta:
        verbose_name = 'Mapa de monitoramento'
        verbose_name_plural = 'Mapas de monitoramento'

    def __str__(self):
        return "{}".format(self.title)



class PartnerUser(BaseModel):
    partner = models.ForeignKey(
        Partner,
        verbose_name='parceiro',
        on_delete=models.CASCADE
    )
    user = models.OneToOneField(
        User,
        verbose_name='usuario',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'usuario (parceiro)'
        verbose_name_plural = 'usuarios (parceiro)'
        ordering = ('created_at',)

    def __str__(self):
        return "{} - {}".format(self.user, self.partner)




class CustomerUser(BaseModel):

    STATUS_CHOICES = (
        ('1', 'normal'),
        ('2', 'bloqueado'),
    )
    username = models.CharField(
        verbose_name='usuário', 
        max_length=255, 
        unique=True,
        error_messages={'unique':"Este usuário já está em uso."},
        help_text='Informação usuada para o cliente fazer login no serviço'
    )
    password = models.CharField(
        verbose_name='senha', 
        max_length=255,
        help_text='Senha que o cliente usará no login do serviço'
    )
    full_name = models.CharField(verbose_name='nome completo', max_length=255, null=True)
    phone = models.CharField(verbose_name='telefone', max_length=17, null=True)
    status = models.CharField(verbose_name='status', choices=STATUS_CHOICES, default=1, max_length=1)
    address = models.CharField(verbose_name='endereço', max_length=255, null=True)
    city = models.CharField(verbose_name='cidade', max_length=255, null=True)
    provided_by = models.ForeignKey(
        Partner, verbose_name='fornecido por', 
        null=True, 
        on_delete=models.PROTECT
    )
    created_by = models.ForeignKey(
        User, verbose_name='criado por', 
        null=True, 
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = 'usuário (oxentetv)'
        verbose_name_plural = 'usuários (oxentetv)'
        ordering = ('-created_at',)

    def __str__(self):
        return "{} - {}".format(self.username, self.full_name)



# class LogStatus(Base)

