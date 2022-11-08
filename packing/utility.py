from django.db.models import Sum


def get_team_hours(team):
    '''
    Function that takes in a particular column of team data, filters it by day and,
    then adds their summed value to a list and outputs that list.
    '''
    week_total = []
    day_list = ['Saturday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    for day in day_list:
        t = team.filter(day=day, week__name='November Wk1').annotate(total_hours=Sum('time'))
        try:
            tt = t.first().total_hours
        except:
            tt = 0
        # make sure to expicitly add a zero to keep the day order
        if tt == 0:
            week_total.append(0)
        else:
            week_total.append(tt)

    return week_total