from django.db import models
from django.contrib.auth.models import User

class ListType(models.Model):
    listtitle=models.Charfield (max_length=64)
    listcreatedate=models.Datefield()
    listcreatetime=models=models.TimeField()
    listitem=models.Charfield (max_length=64)
    listitemduedate=models.DateField()
    listduetime=models=models.TimeField()
    listpriority=models.Charfield (max_length=16)
    
li    class Meta:
        db_table='todolist'
        verbose_name_plural='ListTypes'

    def __str__(self):
        return self.listtitle