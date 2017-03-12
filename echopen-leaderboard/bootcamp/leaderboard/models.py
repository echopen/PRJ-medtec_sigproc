from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

import uuid

class Algorithm(models.Model):
    user = models.ForeignKey(User, default=1)
    username = models.TextField(default='toto')
    score = models.FloatField(default=10)
    cpu = models.IntegerField(default=10)
    time = models.FloatField(default=10)
    process_date =  models.DateTimeField(default=datetime.now, blank=True)
    rank = models.IntegerField(default=1)
    source_code = models.TextField(default='toto')
    
    def get_fields_and_values(self):
            return [(field, field.value_to_string(self)) for field in Algorithm._meta.fields]


    def __str__(self):              # __unicode__ on Python 2
        return self.headline
