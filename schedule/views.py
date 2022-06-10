from django.shortcuts import render
from schedule.models import Activity, Day

# Create your views here.


def schedule(request):
    activities = Activity.objects.all().order_by('end_time')
    days = Day.objects.all()

    # говнокод

    # forming dict['day'] = [act1, act2 ... actN]

    act_dict = {}

    for day in days:
        act_dict[day.name] = []

    for day in days:
        for activity in activities:
            if activity.day == day:
                try:
                    act_dict[day.name].append(activity)
                except KeyError:
                    act_dict[day.name] = [activity, ]

    longest_row_len = len(act_dict[sorted(act_dict, key=lambda k: len(act_dict[k]), reverse=True)[0]])

    for day, activity in act_dict.items():
        if len(activity) < longest_row_len:
            while len(activity) < longest_row_len:
                act_dict[day].append(' ')

    return render(request, 'schedule/schedule.html', {
        'act_dict': act_dict,
        'days': days,
        'longest': longest_row_len,
    })