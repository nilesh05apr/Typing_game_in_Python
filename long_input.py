import random
import time

words = []
with open('dataFile.txt','r') as f:
	for line in f:
		words.extend(line.split())
score = 0
x = time.time()
while True:
	i = random.randint(0,len(words)-1)
	out_string = words[i]
	print("Type words: "+ out_string)
	inp = input("\n")
	print()
	if inp == out_string:
		score += 10
		print("correct!")
		#print("score: "+str(score)+"\n")
	else:
		print("Incorrect")
		#print("grand score: "+str(score))
		break
y = time.time()
print("Grand_Score: " + str(score))
time_taken = y - x  
results = score/10
results = float(results)/float(time_taken)
print("Your results: " + str(results*60) + " wpm.")
