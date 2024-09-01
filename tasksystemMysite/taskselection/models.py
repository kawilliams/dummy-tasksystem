from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
    
class Task(models.Model):
    """
    code,category,desc,date,starttime,endtime,location,username,duration
    """
    code = models.IntegerField(unique=True)
    category = models.IntegerField(default=0)
    desc = models.TextField(max_length=200)
    date = models.DateField() #must be "YYYY-MM-DD" format
    starttime = models.TimeField()  #must be in "HH:MM:SS" format
    endtime = models.TimeField()
    location = models.TextField(max_length=200)
    
    _is_sticky = models.BooleanField(default=False, db_column="is_sticky")

    sv = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    @property
    def is_sticky(self):
        if settings.LOCK_TASKSELECTION:
            return True
        else:
            return self._is_sticky
        
    @is_sticky.setter
    def is_sticky(self, value):
        self._is_sticky = value
