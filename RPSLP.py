"""
Implement game of Rock Paper Scissors Lizard Spock
Get user input, produce a computer input, compaire the two
and produce an output. 
"""
from random import choice

options = {
"Rock":0, 
"Paper":0,
"Scissor":0,
"Lizzard":0,
"Spock":0
}
results = {
"win":0,
"tie":0,
"loss":0,
"total":0
}
counters = {
"Rock": ["Paper", "Spock"],
"Paper": ["Scissor", "Lizzard"],
"Scissor": ["Spock", "Rock"],
"Lizzard": ["Scissor", "Rock"],
"Spock": ["Paper", "Lizzard"]
}

def findWinner(user_input,comp_input):
	if comp_input in counters[user_input]:
		return "loss"
	elif comp_input == user_input:
		return "tie"
	else:
		return "win"

def updateResult(result):
	results[result] += 1
	results["total"] += 1

def displayResults():
	print "Total Games = "+str(results["total"])
	print "Wins = "+str(results["win"])+" "+str((float(results["win"])/results["total"]) * 100)+"%"
	print "Ties = "+str(results["tie"])+" "+str((float(results["tie"])/results["total"]) * 100)+"%"
	print "Loss = "+str(results["loss"])+" "+str((float(results["loss"])/results["total"]) * 100)+"%"

def randomAI():
	return choice(list(options))
	
"""
  Computer picks are based on taking the
  top picks so far and picking from the counter picks. 
  In the case of a tie of top picks the computer will only random 
  amongst the counter moves of those choices.
"""
def goodAI():
	max = 0
	max_played=[]
	poss_counter=[]
	for i in options:
		if max == options[i]:
			max_played.append(i)
		elif max < options[i]:
			max = options[i]
			max_played = []
			max_played.append(i)
	for i in max_played:
		poss_counter.extend(counters[i])
	return choice(poss_counter)	
	
while 1:
	print "Lets play "+ " ".join(list(options))+" or Quit"
	
	user_input = raw_input("Enter you choice:")
	if user_input == "Quit":
		print "Game Over"
		displayResults()
		break
	if user_input not in options:
		print "Enter valid option"
		continue
	
	options[user_input] += 1
	comp_input = goodAI()
	
	print "You entered: "+user_input
	print "Comp generated: "+comp_input
	result = findWinner(user_input,comp_input)
	updateResult(result)
	print "You "+result
	
