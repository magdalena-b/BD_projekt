from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.postgres.fields import ArrayField
from datetime import datetime, date
from enum import Enum
from statistics import mean
#from djangoratings.fields import RatingField

class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        choices = list()

        # Loop thru defined enums
        for item in cls:
            choices.append((item.value, item.name))

        # return as tuple
        return tuple(choices)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.value


class RateOptions(ChoiceEnum):
    bad = 1
    not_good = 2
    not_bad = 3
    good = 4
    very_good = 5


RateOptions.bad.__name__ = 'Very bad'
RateOptions.not_good.__name__ = 'Bad'
RateOptions.not_bad.__name__ = 'Mediocre'
RateOptions.good.__name__ = 'Good'
RateOptions.very_good.__name__ = 'Very good'

R_O = (
    (1, 'Very bad'),
    (2, 'Bad'),
    (3, 'Mediocre'),
    (4, 'Good'),
    (5, 'Very good'),
)


class Trainer(models.Model):
    name = models.CharField(max_length=250)
    surname = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
     
    def __str__(self):
        return self.name + " " + self.surname

    def get_rate(self):
        rates = self.rate_set.all()
        if len(rates) <= 0:
            return "This trainer doesn't have any rates yet!"
        mean_rate = mean(item.rate for item in rates)
        closest_rate = int(round(mean_rate, 2))
        if(closest_rate > 0): closest_rate = closest_rate - 1
        return f'{round(mean_rate, 2)}-{R_O[closest_rate][1]}'

    def get_all_rates(self, user_id):
        users = self.rate_set.all()
        rated = False
        for user in users:
            if(user.user == user_id):
                rated = True
        return rated


class Classes(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=250, default='class description', editable=True)
    limit = models.PositiveIntegerField(null=True, default=15)

    def get_participants_number(self):
        signed_number = self.profile_set.all().count()
        return signed_number

    def can_sign(self):
        return self.limit is None or self.seats_left() > 0

    def seats_left(self):
        if self.limit is None:
            return 'no limit'
        return self.limit - self.get_participants_number()

    def name_and_date(self):
        day_of_week = self.date.strftime('%A %H:%M, %d %B %Y')
        return '{} - {}'.format(self.name, day_of_week)

    def __str__(self):
        day_of_week = self.date.strftime('%A %H:%M, %d %B %Y')
        return '{} - {} ({})'.format(self.name, self.description, day_of_week)

    def get_rate(self):
        rates = self.rate_set.all()
        if len(rates) <= 0:
            return "This class doesn't have any rates yet!"
        mean_rate = mean(item.rate for item in rates)
        closest_rate = int(round(mean_rate, 2))
        if(closest_rate > 0): closest_rate = closest_rate - 1
        return f'{round(mean_rate, 2)}-{R_O[closest_rate][1]}'

    def get_all_rates(self, user_id):
        users = self.rate_set.all()
        rated = False
        for user in users:
            if(user.user == user_id):
                rated = True
        return rated

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=500, null=True)
    surname = models.CharField(max_length=30, null=True)
    classes = models.ManyToManyField(Classes)
    def get_future_classes(self):
        return self.classes.filter(date__gt=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

    def get_past_classes(self):
        return self.classes.filter(date__lt=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Profile._meta.fields]

    def get_rated_classes(self):
        classes = self.classes.all()
        rated_classes = []

        for clss in classes:
            rates = clss.rate_set.all()
            for rate in rates:
                if(rate.user.id == self.id):
                        rated_classes.append(rate.classes)
        return rated_classes

    def get_not_rated_classes(self):
        classes = self.get_past_classes()
        not_rated_classes = []
        for c in classes:
            not_rated_classes.append(c)

        for clss in classes:
            rates = clss.rate_set.all()
            for rate in rates:
                if(rate.user.id == self.id):
                        not_rated_classes.remove(rate.classes)
        return not_rated_classes


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Rate(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    rate = models.IntegerField(choices=R_O)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['trainer', 'user'], name='one_time_rating_trainer'),
        ]