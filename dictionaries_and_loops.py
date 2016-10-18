from collections import OrderedDict

# using a dictionary to store rapper performance times
performances = {'Local Rapper':'1:00pm',
                'Chance The Rapper': '4:00pm',
                'J.Cole': '6:00pm',
                'Jay Z':'10:00pm'}

# using a loop to concatenate the elements and remove unwanted space
for name, time in performances.items():
    print(name + ':' + time, sep='')