from django.db.models import Sum


def get_team_hours(team):
    '''
    Function that takes in a particular column of team data, filters it by day and,
    then adds their summed value to a list and outputs that list.
    '''
    week_total = []
    day_list = [1, 2, 3, 4, 5, 6]
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


def filter_annotate(
    model_var,
    filter_list,
    filter_col,
    annotate_var,
    annotate_filter,
    type
):
    '''
    A function to query the database.
    '''
    calc_output_list = []
    name_output_list = []
    
    for item in filter_list:
        filtered = model_var.filter(filter_col=item)
        annotated = filtered.annotate(annotate_var=Sum(annotate_filter))
        try:
            annotated_sum = annotated.first().annotate_var
        except:
            annotated_sum = 0

        if annotated_sum == 0:
            output_list.append(0)
        else:
            output_list.append(annotated_sum)

        name_output_list.append(name)
    
    return calc_output_list, name_output_list