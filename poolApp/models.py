from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.TextField()
    opt1 = models.CharField(max_length=30)
    opt2 = models.CharField(max_length=30)
    opt3 = models.CharField(max_length=30)
    opt1count = models.IntegerField(default=0)
    opt2count = models.IntegerField(default=0)
    opt3count = models.IntegerField(default=0)

    def total(self):
        return self.opt1count + self.opt2count + self.opt3count