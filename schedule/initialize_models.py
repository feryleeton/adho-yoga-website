import datetime

from schedule.models import Day


def init_schedule_models():

    if Day.objects.all():
        print('Day objects already initialized !')
    else:
        Day.objects.create(name='Monday').save()
        Day.objects.create(name='Tuesday').save()
        Day.objects.create(name='Wednesday').save()
        Day.objects.create(name='Thursday').save()
        Day.objects.create(name='Friday').save()
        Day.objects.create(name='Saturday').save()
        Day.objects.create(name='Sunday').save()

        print('Day objects initialized successfully !')