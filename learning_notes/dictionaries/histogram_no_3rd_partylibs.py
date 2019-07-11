"""
g $$$$$$$$$$$$$$$$$$$$
f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
t $$$$$$$$$$
o $$$$$$$$$$$$
"""

sales = {
  'google': 20,
  'facebook': 34,
  'twitter': 10,
  'offline': 12,
}

#print(('g ') + sales['google'] * '$')


print(f"{'g '}{sales['google'] * '$'}")
print(f"{'f '}{sales['facebook'] * '$'}")
print(f"{'t '}{sales['twitter'] * '$'}")
print(f"{'o '}{sales['offline'] * '$'}")