import random
tiles = [
  {'name': 'Go', 'cost': 0, 'location': 0, 'type': 'pass', 'base_rent': 2, 'group': None},
  {'name': 'Mediterranean Avenue', 'cost': 60, 'location': 1, 'type': 'property', 'base_rent': 2, 'group': 'brown',
   'owner': None},
  {'name': 'Community Chest', 'cost': 0, 'location': 2, 'type': 'chest', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Baltic Avenue', 'cost': 60, 'location': 3, 'type': 'property', 'base_rent': 4, 'group': 'brown',
   'owner': None},
  {'name': 'Income Tax', 'cost': 0, 'location': 4, 'type': 'tax', 'base_rent': 100,
   'group': 'chill'},
  {'name': 'Reading RR', 'cost': 200, 'location': 5, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
   'owner': None},
  {'name': 'Oriental Avenue', 'cost': 100, 'location': 6, 'type': 'property', 'base_rent': 6,
   'group': 'blue', 'owner': None},
  {'name': 'Chance', 'cost': 0, 'location': 7, 'type': 'chance', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Vermont Avenue', 'cost': 100, 'location': 8, 'type': 'property', 'base_rent': 6, 'group': 'blue',
   'owner': None},
  {'name': 'Connecticut Avenue', 'cost': 120, 'location': 9, 'type': 'property', 'base_rent': 8,
   'group': 'blue', 'owner': None},
  {'name': 'Jail', 'cost': 0, 'location': 10, 'type': 'chest', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'St. Charles', 'cost': 140, 'location': 11, 'type': 'property', 'base_rent': 10, 'group': 'purple',
   'owner': None},
  {'name': 'Electric Company', 'cost': 150, 'location': 12, 'type': 'utility', 'base_rent': 1,
   'group': 'utility', 'owner': None},
  {'name': 'States Avenue', 'cost': 70, 'location': 13, 'type': 'property', 'base_rent': 10, 'group': 'purple',
   'owner': None},
  {'name': 'Virginia Avenue', 'cost': 160, 'location': 14, 'type': 'property', 'base_rent': 12,
   'group': 'purple', 'owner': None},
  {'name': 'Pennsylvania RR', 'cost': 200, 'location': 15, 'type': 'railroad', 'base_rent': 25,
   'base_rent': 25, 'group': 'white', 'owner': None},
  {'name': 'St. James', 'cost': 180, 'location': 16, 'type': 'property', 'base_rent': 14, 'group': 'orange',
   'owner': None},
  {'name': 'Community Chest', 'cost': 0, 'location': 17, 'type': 'chest', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Tennessee Avenue', 'cost': 180, 'location': 18, 'type': 'property', 'base_rent': 14,
   'group': 'orange', 'owner': None},
  {'name': 'New York', 'cost': 200, 'location': 19, 'type': 'property', 'base_rent': 16, 'group': 'orange',
   'owner': None},
  {'name': 'Free Parking', 'cost': 0, 'location': 20, 'type': 'parking', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Kentucky Avenue', 'cost': 220, 'location': 21, 'type': 'property', 'base_rent': 18, 'group': 'red',
   'owner': None},
  {'name': 'Chance', 'cost': 0, 'location': 22, 'type': 'chance', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Indiana Avenue', 'cost': 220, 'location': 23, 'type': 'property', 'base_rent': 18, 'group': 'red',
   'owner': None},
  {'name': 'Illinois Avenue', 'cost': 240, 'location': 24, 'type': 'property', 'base_rent': 20, 'group': 'red',
   'owner': None},
  {'name': 'B&O RR', 'cost': 200, 'location': 25, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
   'owner': None},
  {'name': 'Atlantic Avenue', 'cost': 260, 'location': 26, 'type': 'property', 'base_rent': 22,
   'group': 'yellow', 'owner': None},
  {'name': 'Ventnor Avenue', 'cost': 260, 'location': 27, 'type': 'property', 'base_rent': 22,
   'group': 'yellow', 'owner': None},
  {'name': 'Water Works', 'cost': 150, 'location': 28, 'type': 'utility', 'base_rent': 1,
   'group': 'utility', 'owner': None},
  {'name': 'Marvin Gardens', 'cost': 280, 'location': 29, 'type': 'property', 'base_rent': 24, 'group': 'yellow',
   'owner': None},
  {'name': 'Go To Jail!', 'cost': 0, 'location': 30, 'type': 'gotojail', 'base_rent': 0,
   'group': 'jail'},
  {'name': 'Pacific Avenue', 'cost': 300, 'location': 31, 'type': 'property', 'base_rent': 26, 'group': 'green',
   'owner': None},
  {'name': 'North Carolina', 'cost': 300, 'location': 32, 'type': 'property', 'base_rent': 26, 'group': 'green',
   'owner': None},
  {'name': 'Community Chest', 'cost': 0, 'location': 33, 'type': 'chest', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Pennsylvania Avenue', 'cost': 320, 'location': 34, 'type': 'property', 'base_rent': 28,
   'group': 'green', 'owner': None},
  {'name': 'Short Line', 'cost': 200, 'location': 35, 'type': 'railroad', 'base_rent': 25, 'group': 'white',
   'owner': None},
  {'name': 'Chance', 'cost': 0, 'location': 36, 'type': 'chance', 'base_rent': 0,
   'group': 'chill'},
  {'name': 'Park Place', 'cost': 350, 'location': 37, 'type': 'property', 'base_rent': 35, 'group': 'darkblue',
   'owner': None},
  {'name': 'Luxury Tax', 'cost': 0, 'location': 38, 'type': 'tax', 'base_rent': 75,
   'group': 'chill'},
  {'name': 'Boardwalk', 'cost': 400, 'location': 39, 'type': 'property', 'base_rent': 50, 'group': 'darkblue',
   'owner': None}
]

loss_count = 1
class Player:
	
	def __init__(self, player_number, is_human, cash, position, name, last_roll):
		self.player_number = player_number
		self.is_human = is_human
		self.cash = cash
		self.properties_owned = []
		self.position = position
		self.name = name
		self.last_roll = last_roll
		

	def dice_roll(self):
		
		die_0 = random.randint(1,6)
		die_1 = random.randint(1,6)
		total = die_0 + die_1
		self.position += total
		if self.position >= len(tiles):
			self.position -= len(tiles)
			if self.position == 0:
				self.cash += 200
				print("Landed on GO collect 200")
			else:
				self.cash += 100
				print("Pass GO collect 100.")


		last_roll = total
		print("Die 1 was {}, die 2 was {} for a total of {}".format(die_0, die_1, total))
		if die_0 == die_1:
			return True
		else:
			return False
		#roll dice

	def buy_property(self):
		self.cash -= tiles[self.position]['cost'] 
		tiles[self.position]['owner'] = self
		self.properties_owned.append(self.position)
		print("Player {} is purchasing {} for {}".format(self.name, tiles[self.position]['name'], tiles[self.position]['cost']))
	def print_player_landed_on(self):
		print("Player {} landed on {}".format(self.name, tiles[self.position]['name']))

	def print_player_purchasing(self):
		print("Player {} is purchasing {} for {}".format(self.name, tiles[self.position]['name'], tiles[self.position]['cost']))

	def print_player_info(self):
		if self.properties_owned is not None:
			print("Player name: {}, cash {}. {} properties owned:".format(self.name, self.cash, len(self.properties_owned)))
			for i in self.properties_owned:
				print("\t{}, {}".format(tiles[i]['name'], tiles[i]['group']))
	def afford(self):
		if tiles[self.position]['cost'] <= self.cash:
			return True
		else:
			return False

	def pay_rent(self, other, amount):
		global loss_count
		if(self.cash - amount < 0):
			print("Player {} has lost! All money and properties will be transferred to {}.".format(self.name, other.name))
			other.cash += self.cash
			for j in self.properties_owned:
				tiles[j]['owner'] = other

			other.properties_owned.extend(self.properties_owned)
			self.properties_owned = None
			self.cash = -1
			loss_count += 1
		else:
			self.cash -= amount
			other.cash += amount
			print("{} landed on {}'s property and paid rent in the amount of {}.".format(self.name, other.name, amount))

def calculate_rent(debter, owner):
	color_sum = 0;
	modifier = 1
	for prop in owner.properties_owned:
		if tiles[prop]['group'] == tiles[debter.position]['group']:
			color_sum += 1

	if tiles[prop]['type'] == "property":
		if color_sum == 3:
			modifier = 2
	elif tiles[prop]['type'] == "railroad":
		if color_sum == 4:
			modifier = 8
		elif color_sum == 3:
			modifier = 4
		elif color_sum == 2:
			modifier = 2
	elif tiles[prop]['type'] == "utility":
		if color_sum == 2:
			return debter.last_roll * 10
		else:
			return debter.last_roll * 4

	return tiles[debter.position]['base_rent'] * modifier
def owned(player):
	owner = tiles[player.position]['owner']
	if owner == None:
		return False
	elif owner.name == player.name:
		print("Property is owned by player {}.".format(player.name))
	else:
		player.pay_rent(owner, calculate_rent(player, owner))

def is_chill(player):
	if tiles[player.position]['group'] == "chill":
		print("Landed on a chill property. Nothing to see here...")
		return True
	elif tiles[player.position]['group'] == "jail":
		player.position = 9;
		print("Go to jail!")
	elif tiles[player.position]['name'] == "Go":
		return True
	elif tiles[player.position]['name'] == "Luxury Tax":
		player.cash -= 100
	elif tiles[player.position]['name'] == "Income Tax":
		player.cash -= 200
	else:
		return False


def play(players, player_num):
	while(True):
		for p in players:
			if p.cash >= 0:
				print("Player {} it's your turn! cash {}, location {} ({})".format(p.name, p.cash, p.position, tiles[p.position]['name']))
				double_count = 0
				if p.is_human:
					input("Hit any key to roll dice, human!")
					doubles = p.dice_roll()
					go = True
					while(go):
						p.print_player_landed_on()
						if is_chill(p) is False:
							if owned(p) is False:
								if p.afford():
									ans = input("Would you like to buy {}? Cost: {}, you have {}. (Enter y/n):".format(tiles[p.position]['name'], tiles[p.position]['cost'], p.cash))
									if ans == 'y':
										p.buy_property()
									else:
										print("{} chose not to buy the property.".format(p.name))

						if doubles:
							double_count += 1							
							if double_count == 3:
								p.position = 9
								print("Go to jail!")
								print("Doubles! Rolling again.")
								res = p.dice_roll()
							else:
								go = False
						else:
							go = False
				else:
					doubles = p.dice_roll()
					go = True
					while(go):
						p.print_player_landed_on()
						if is_chill(p) is False:
							if owned(p, loss_count) is False:
								if p.afford():
									p.buy_property()
								else:
									print("{} cannot afford this property.".format(p.name))
						if doubles:
							double_count += 1
							if double_count == 3:
								p.position = 9
								print("Go to jail!")
								go = False
							else:
								print("Doubles! Rolling again.")
								res = p.dice_roll()						
						else:
							go = False


				
				print("{} players and {} loss count.".format(player_num, loss_count))

				if loss_count == player_num - 1:
					print("Game over!")
					exit()
				p.print_player_info()

				input("Current turn over. Press any key to end turn\n")


players = []
player_num = input("How many players?(2-4): ")

# while isinstance(player_num, int) is False or int(player_num) < 1 or int(player_num) > 4:
# 	player_num = int(input("Invalid input. Try again. How many players?(2-4): "))
player_num = int(player_num)
print("Okay {} players.".format(player_num))
for i in range(player_num):
	invalid_input = True
	while(invalid_input):
		h_b = input("Player {}, enter 'h' for human 'b' for bot: ".format(str(i + 1)))
		if h_b == 'h':
			name = input("Enter player name: ")
			players.append(Player(i + 1, True, 1500, 0, name, 0))
			invalid_input = False
		elif h_b == 'b':
			name = "bot" + str(i + 1);
			players.append(Player(i + 1, False, 1500, 0, name, 0))
			invalid_input = False
		else:
			print("Invalid input.")
			

play(players, player_num)
