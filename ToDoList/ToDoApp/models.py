from django.db import models
from django.contrib.auth.models import User

class ListType(models.Model):
    listtitle=models.CharField (max_length=64)
    listcreatedate=models.DateField()
    listcreatetime=models.TimeField()
    listitem=models.CharField (max_length=64)
    listitemduedate=models.DateField()
    listduetime=models.TimeField()
    listpriority=models.CharField (max_length=16)
    
li    class Meta:
        db_table='todolist'
        verbose_name_plural='ListTypes'

    def __str__(self):
        return self.listtitle
