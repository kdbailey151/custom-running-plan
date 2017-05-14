import m26

'#Get parameter information from user'
print('What is your current average weekly mileage?')
starting_mileage = int(input())

print('How many weeks do you want to train: enter 8, 12, 16, 18 or 20?')
num_weeks = int(input())

'''#print('Which day do you want to do your long run?')'
#long_run = input()'''

'''#print('What is your goal race pace?')
race_pace = input()'''

d1 = m26.Distance(26.2)
t1 = m26.ElapsedTime('4:00:00')
s1 = m26.Speed(d1, t1)
Easy = s1.pace_per_mile()

t2 = m26.ElapsedTime('3:18:00')
s2 = m26.Speed(d1, t2)
Tempo = s2.pace_per_mile()

def weekly_total(week):
    '''(List of list of str, int) -> int

    Return the total weekly mileage from a given list of days, miles per day.

    >>> weekly_total(week1)
    27
    '''

    total = 0
    i = 0
    for t in range(len(week)-1):
        total = total + week[i][1]
        i = i + 1
    week[i][1] = total
    return total

def pace_change(Easy):
    '''(string) -> string
    Return a new pace approximately one second per mile faster by mulitplying
    the speed in mph by 1.0418 and converting back to pace per mile.

    >>> pace_change('9:09:01')
    ('9:07:32')
    '''
    
    
    new_s = (s1.mph() * 1.0418)
    
    return new_s.pace_per_mile()
    

'#create starting weekly mileage templates based on initial mileage input'

if starting_mileage > 30:
    week_one = ([['M', 0], ['T', 4], ['W', 4], ['Th', 6], ['F', 5], ['S', 0],
                 ['Su', 12], ['Total', 31]])
elif starting_mileage > 25 <= 30:
    week_one = ([['M', 0, 'Rest'], ['T', 4, Tempo], ['W', 0, 'Rest'], ['Th', 6, Easy],
                 ['F', 5, Easy], ['S', 0, 'Rest'],['Su', 11, Easy], ['Total', 26, '']])
elif starting_mileage > 20 <= 25:
    week_one = ([['M', 0], ['T', 3], ['W', 0], ['Th', 5], ['F', 4], ['S', 0],
                 ['Su', 9], ['Total', 21]])
elif starting_mileage > 15 <= 20:
    week_one = ([['M', 0], ['T', 2], ['W', 0], ['Th', 4], ['F', 3], ['S', 0],
                 ['Su', 6], ['Total', 15]])
else:
    week_one = ([['M', 0], ['T', 1], ['W', 0], ['Th', 3], ['F', 2], ['S', 0],
                 ['Su', 4], ['Total', 10]])


def next_week_phase_one(week):
    '''(List of List of strings) -> List of list of strings

    Return a list of list of strings with values for mileage increased by one
    for Sunday and Tuesday given a list of weekly mileages.

    >>>next_week_phase_one([week1)
    ([['M', 0], ['T', 5], ['W', 4], ['Th', 6], ['F', 6], ['S', 0], ['Su', 13],
    ['Total', 33])
    '''
    new_week = []
    i = 0

    for l in week:
        if l[0] != 'Total':
            '''#daily mileage stays the same except for Sunday and Tuesday'''
            if l[0] not in ('Su', 'T'):
                new_week.append(week[i])
                i = i + 1
                if l[2] == Easy:
                    pace_change(Easy)
                    new_week.append(week[i])
                    i = i + 1
                else:
                    new_week.append(week[i])
                    i = i + 1
            else:
                'add day/mileage to days of week'
                week[i][1] = week[i][1] + 1
                new_week.append(week[i])
                i = i + 1
                if l[2] == Easy:
                    pace_change(Easy)
                    new_week.append(week[i])
                    i = i + 1
                else:
                    new_week.append(week[i])
                    i = i + 1
        else:
            weekly_total(week_one)
            new_week.append(week[i])
    
    return new_week


def next_week_phase_two(week):
    '''(List of List of strings) -> List of list of strings

    Return a list of list of strings with values for mileage increased by one
    for Sunday and Tuesday given a list of weekly mileages.

    >>>next_week_phase_one([week1)
    ([['M', 0], ['T', 4], ['W', 4], ['Th', 6], ['F', 7], ['S', 0], ['Su', 13],
    ['Total', 33])
    '''
    new_week = []
    i = 0

    for l in week:
        if l[0] != 'Total':
            '#daily mileage stays the same except for Sunday and Friday'
            if l[0] not in ('Su', 'F'):
                new_week.append(week[i])   
                i = i + 1        
            else:
                week[i][1] = week[i][1] + 1
                new_week.append(week[i])
                i = i + 1                
        else:
            weekly_total(week_one)
            new_week.append(week[i])           
    return new_week



def next_week_phase_three(week):
    '''(List of List of string, int) -> List of list of string, int

    Return a list of list of strings with values for mileage increased by one for
    Wednesday and Thursday given a list of weekly mileages.

    >>>next_week_phase_one([week1)
    ([['M', 0], ['T', 4], ['W', 5], ['Th', 7], ['F', 6], ['S', 0], ['Su', 12],
    ['Total', 31])
    '''
    new_week = []
    i = 0
       
    for l in week:
        if l[0] != 'Total':
            if l[0] not in ('W', 'Su'):
                new_week.append(week[i])
                i = i + 1                
            else:
                week[i][1] = week[i][1] + 1
                new_week.append(week[i])
                i = i + 1               
        else:
            weekly_total(week_one)
            new_week.append(week[i])           
    return new_week

def bump_up(week):
    '''(List of List of string, int) -> List of list of string, int

    Return a new weekly mileage list adding one new day of running and simultaneously decreasing other daily mileage except long run.
    
    >>> bump_up(week1)
    ([['M', 0], ['T', 3], ['W', 4], ['Th', 5], ['F', 5], ['S', 4], ['Su', 11],
    ['Total', 32])
    '''
    new_week = []
    i = 0

    for l in week:
        if l[0] == 'Total':
            weekly_total(week_one)
            new_week.append(week[i])            
        if l[0] in ('M', 'T', 'Th', 'F'):
                if l[1] != 0:
                    l[1] = l[1] -1
                    new_week.append(week[i])
                    i = i + 1
                else:
                    new_week.append(week[i])
                    i = i + 1
        if l[0] == 'Su':
            l[1] = l[1] + 2
            new_week.append(week[i])
            i= i + 1
        if l[0] == 'W':
                if l[1] == 0:
                    l[1] = 3                    
                    new_week.append(week[i])
                    i = i + 1                    
                else:
                    l[1] = l[1] - 1
                    new_week.append(week[i])
                    i = i + 1
        if l[0] == 'S':
            if week[2][1] == 0:
                l[1] = 3                    
                new_week.append(week[i])
                i = i + 1
            else:
                new_week.append(week[i])
    return new_week
    
def cutback_week(week):
    '''(List of List of strings) -> List of list of strings

    Return a list of list of strings with values for mileage decreased by
    twenty percent for each day of the week given a list of weekly mileages.

    >>> cutback_week(week1)
    ([['M', 0], ['T', 3], ['W', 3], ['Th', 4], ['F', 4], ['S', 0], ['Su', 9],
    ['Total', 23])
    '''
    new_week = []
    i = 0

    for l in week:
        if l[0] != 'Total':
            '#decrease each days mileage by 20 percent(multiply by .8)'
            week[i][1] = int(week[i][1] * .8)
            '#add each decrease day/mileage to new week'
            new_week.append(week[i])  
            i = i + 1
        else:
            weekly_total(week_one)
            new_week.append(week[i])       
 
    return new_week
    
def taper(week):
    '''(List of List of string, int) -> List of list of string, int

    Return a list of list of strings with values for mileage decreased by
    thirty percent for each day of the week given a list of weekly mileages.

    >>> taper(week1)
    ([['M',0],['T',2], ['W', 0], ['Th', 2], ['F', 2], ['S', 0],['Su', 7]])
    '''
    new_week = []
    i = 0
  
    for l in week:
        if l[0] != 'Total':
            '#decrease each days mileage by 20 percent(multiply by .8)'
            week[i][1] = int(week[i][1] * .7)  
            new_week.append(week[i])
            i = i + 1
        else:
            weekly_total(week_one)
            new_week.append(week[i])    
    return new_week

def catch_up_week(week):
    '''(List of List of strings) -> List of list of strings

    Return a list of list of strings with values for mileage increased by
    thirty-five percent for each day of the week given a list of weekly mileages.

    >>> catch_up_week(week1)
    ([['M', 0], ['T', 5], ['W', 5], ['Th', 7], ['F', 6], ['S', 0], ['Su', 15],
    ['Total', 38]])
    '''
    new_week = []
    i = 0

    for l in week:
        if l[0] != 'Total':
            '#increase each days mileage by 35 percent(multiply by 1.35)'
            week[i][1] = int(week[i][1] * 1.35)  
            new_week.append(week[i])
            i = i + 1            
        else:
            weekly_total(week_one)
            new_week.append(week[i])    
    return new_week

def running_plan(week):
    '''

    Return a running plan with the following structure from a prompted input:

    week_one #based on pre-determined template for a given starting mileage
    next_week_phase_one x 2
    cut_back
    bump_up
    next_week_phase_two x 2
    cut_back
    bump_up
    next_week-phase_three x 2
    cut_back
    bump_up
    next_week_phase_two x 2
    taper
    taper
    '''
    '#weeks 1-3'
    i = 0
    while num_weeks <= 18:
        for i in range(3):
            print(next_week_phase_one(week_one))
    #week 4       
        for i in range(1):        
            print(cutback_week(week_one))
    #week 5
        for i in range(1):
            print(catch_up_week(week_one))
    #weeks 6-7
        for i in range(2):
            print(next_week_phase_two(week_one))
    #week 8
        for i in range(1):
            print(cutback_week(week_one))
    #week 9
        if num_weeks <= 8:
            break
        else:
            for i in range(1):
                print(catch_up_week(week_one))
            for i in range(1):
                print(bump_up(week_one))
    
    #weeks 11-12
            for i in range(1):
                print(next_week_phase_three(week_one))
            for i in range(1):
                print(cutback_week(week_one))
            if num_weeks <= 12:
                break  
    #week 13-15
            else:
                for i in range(1):
                    print(catch_up_week(week_one))
                for i in range(2):
                    print(next_week_phase_three(week_one))                
    #weeks 15-16
                if num_weeks <= 16:                    
                    for i in range(1):
                        print(taper(week_one))
                    break
                else:
                    for i in range(1):
                        print(next_week_phase_three(week_one))
    #weeks 17-18
                    for i in range(2):
                        print(taper(week_one))
                    break
   
                 
running_plan(week_one)
