from django.db import models

class Trainer(models.Model):
  name = models.CharField(max_length=250)
  surname = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  phone = models.CharField(max_length=250)

  def __str__(self):
    return self.name + " " + self.surname


class Classes(models.Model):
  trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
  date = models.CharField(max_length=250)
  name = models.CharField(max_length=250)


class User(models.Model):
  name = models.CharField(max_length=250)
  surname = models.CharField(max_length=250)
  email = models.CharField(max_length=250)
  phone = models.CharField(max_length=250)