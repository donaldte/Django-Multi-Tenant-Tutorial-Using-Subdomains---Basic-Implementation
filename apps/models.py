from django.db import models

# Create your models here.
class Tenant(models.Model):
    name = models.CharField(max_length=45)
    subdomaiin = models.CharField(max_length=567)

class TenantAwareMode(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

class Member(TenantAwareMode):
    name = models.CharField(max_length=255)
