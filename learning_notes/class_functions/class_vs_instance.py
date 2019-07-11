class Website:
  def __init__(self, title): # starts an instance
    self.title = title


ws = Website('My Website Title') # first instance
print(ws.__dict__)

ws_two = Website('My Second Title') # second instance
print(ws_two.__dict__)

#instance would end but if you knew the variable you can still call it




class DifferentWebsite:
  title = 'My Class Title' #hard coded into the class

dw = DifferentWebsite()  # Class attribute
print(dw.title)

dw_two = DifferentWebsite() # Class attribute
print(dw_two.title)