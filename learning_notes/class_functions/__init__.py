class Invoice:

  def __init__(self, client, total): #the __init__ is a constructor, it allows self.variables to be called later on.
    self.client = client
    self.total = total


  def formatter(self):
    return f'{self.client} owes: ${self.total}'

  @property
  def client(self):
    return self._client

  @client.setter  
    def client(self):
      self._client = client


google = Invoice('google', 100)
snapchat = Invoice('SnapChat', 200)

print(google.formatter())
print(snapchat.formatter())

#self is the class referring to itself. So self.client is telling it to look into the class for it's next step

#if you want to make something unchangeable you need to use an _.  So, for example, slef._client achieves that

#decorators '@' are to show that something is important and will be caled