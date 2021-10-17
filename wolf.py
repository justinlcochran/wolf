import random
import pandas as pd


active_roles = {}


with open(r"C:\Users\justi\OneDrive\Desktop\Python Learning\wolf\WolfRoles.csv") as wolfRoleFile:
	wolfRoleFile = pd.read_csv(wolfRoleFile).dropna()
	wolfRoleOptions = [row[1] for i, row in wolfRoleFile.iterrows()]
	wolfRoleDict = {row[1]: row[0] for i, row in wolfRoleFile.iterrows()}

with open(r"C:\Users\justi\OneDrive\Desktop\Python Learning\wolf\PositiveRoles.csv") as positiveRoleFile:
	positiveRoleFile = pd.read_csv(positiveRoleFile).dropna()
	positiveRoleOptions = [row[1] for i, row in positiveRoleFile.iterrows()]
	positiveRoleDict = {row[1]: row[0] for i, row in positiveRoleFile.iterrows()}

with open(r"C:\Users\justi\OneDrive\Desktop\Python Learning\wolf\NegativeRoles.csv") as negativeRoleFile:
	negativeRoleFile = pd.read_csv(negativeRoleFile).dropna()
	negativeRoleOptions = [row[1] for i, row in negativeRoleFile.iterrows()]
	negativeRoleDict = {row[1]: row[0] for i, row in negativeRoleFile.iterrows()}

allRolesDict = wolfRoleDict | positiveRoleDict | negativeRoleDict

def player_list_get():
	players = []
	player_total = int(input("How many players in this game? "))
	while player_total > len(players):
		print(players)
		players.append(input("Player Names: "))

def role_list_get():
	roles = []

while True:


wolf_count = int(input("How many wolves would you like in this game? "))

for i in range(wolfCount):
	roles.append(random.choice(wolfRoleOptions))



while len(roles) < len(players):
	gameScore = 0
	for i in roles:
		gameScore += allRolesDict[i]
	if gameScore < 0:
		roles.append(random.choice(positiveRoleOptions))
	else:
		roles.append(random.choice(negativeRoleOptions))

gameScore = 0
for i in roles:
	gameScore += allRolesDict[i]
random.shuffle(roles)
random.shuffle(players)
gameReport = {players[x]: roles[x] for x in range(len(players))}
print('\n\n')
for key, value in gameReport.items():
	print(f"{key}: {value}")
print(f"\nGame Score: {gameScore}")
