from django.db import models

class Trainer(models.Model):
  name = models.CharField(max_length=250)
  surname = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  phone = models.CharField(max_length=250)


class Classes(models.Model):
  trainer = model.ForeignKey(Trainer, on_delete=models.CASCADE)