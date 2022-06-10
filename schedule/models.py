from django.db import models

# Create your models here.


class Day(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    start_time = models.TimeField()
    end_time = models.TimeField()
    trainer = models.CharField(max_length=30, blank=True)

    day = models.ForeignKey(Day, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'

    def __str__(self):
        return str(self.title) + ' [ ' + str(self.day) + ' ] '