def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


#laid out for easier reading.
greeting('Morning', #time_of_day
         'Kristine', 'Hudgens', #tuple for args
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework') #dictionary for kwargs


#Using all types