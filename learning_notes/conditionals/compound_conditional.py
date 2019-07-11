username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Get thee hence')
#both have to be True

if username == 'jonsnow' or password == 'thenorth':
#one has to be True

#a more real word example
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#email or login has to be true, then password has to be true.

logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')

#means that we want logged in is true, but the standard user is false, so they are admins.