import random

map1 = [['X','','',''],['','X','','O'],['','O','','X'],['','','','X']]

# number_of_dragons = 3

# number_of_golds = 3

# def pick_a_tile():
# 	row = random.randint(0,3)
# 	column = random.randint(0,3)
# 	tile = [row,column]
	
# 	return row,column



# def check_if_empty(row, column):
	
#  	return map1[row, column] == ''
 	


# row,column = pick_a_tile()

class Game_object(object):
	def __init__(self,row,column):
		self.row = row
		self.column = column


player = Game_object(0,0)
player.lives = 3
player.coins = 0

class Dragon(Game_object):
	def fire(self):
		player.lives -=1
		return "The dragon spews fire and you are reduced to ash. -1 life"

class Coin(Game_object):
	def enwealth(self):
		player.coins += 1
		return "You got 1 coin richer! You have %d coin(s)"%player.coins

dragon = Dragon(3,4)
print dragon.fire()
print dragon.row
coin = Coin(1,2)
print coin.row
print player.coins
print coin.enwealth()
print player.coins
