from django.db import models


class ActivityPeriod(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



class UserDF(models.Model):
    activity_period = models.ForeignKey(
        ActivityPeriod, on_delete=models.SET_NULL, null=True
    )
    real_name = models.CharField(max_length=20) 
    tz = models.DateTimeField()

    def __str__(self):
        return self.real_name





