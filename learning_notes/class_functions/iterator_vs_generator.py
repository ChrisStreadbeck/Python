class InfiniteLineup:
  def __init__(self, players):
    self.players = players
  
  def lineup(self):
    lineup_max = len(self.players)
    idx = 0

    while True:
      if idx < lineup_max:
        yield self.players[idx]
      else:
        idx = 0
        yield self.players[idx]
      
      idx += 1

  def __repr__(self):
    return f'<InfiniteLineup({self.players})'
  
  def __str__(self):
    return f"InfiniteLineup with the players: {', '.join(self.players)}"




astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

full_lineup = InfiniteLineup(astros)

astros_lineup = full_lineup.lineup()

print(next(astros_lineup))
print(next(astros_lineup))
print(next(astros_lineup))

print(repr(astros_lineup))
print(str(astros_lineup))