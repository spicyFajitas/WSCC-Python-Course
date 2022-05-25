import random
#create intro function with unimportant information and cool dashes
def Intro():
    print('This program simulates a user specified amount of racquetball games between players "A" and "B" based on user specified probablility that each player will win. \n\nA match win is determined when either player A or B won 2 of the 3 games played. The wins can be 2 games where one player won consecutively or 3 games where the third game was played to decide the winner of the match. \n\n----------------------------------------------------')
		
#where the magic happens
def simGame(nGames, probPA, probPB):
		#counter variables
    paWins = pbWins = 0
    paWins2 = pbWins2 = 0
    shutoutsA = shutoutsB = 0
    paMatches = pbMatches = 0
		#loops for however many games there are
    for i in range(nGames):
				#decides server
        if (i + 1) % 2 != 0:
            server = 'A'
        else:
            server ='B'
				#more counter variables
        paScore = pbScore = 0
				#tells the game to continue as long as the score limit has not been reached
        while paScore < 15 and pbScore < 15:
						#A can only score if they are server
            if server == 'A':
                if random.random() < probPA:
                    paScore += 1
                else:
                    server = 'B'
						#B can only score if they are server
            else:
                if random.random() < probPB:
                    pbScore += 1
                else:
                    server = 'A'
				#adds a win to A if score = 15
        if paScore == 15:
            paWins += 1; paWins2 += 1
				#adds a win to B if score = 15						
        else:
            pbWins += 1; pbWins2 += 1
				#adds a shutout to A if A's score is 15 and B's score is 0
        if paScore == 15 and pbScore == 0:
            shutoutsA +=1
				#adds a shutout to A if A's score is 15 and B's score is 0
        elif paScore == 0 and pbScore == 15:
            shutoutsB +=1
				#adds a Match win to A
        if paWins2 == 3:
            paMatches += 1; paWins2 = 0
				#adds a match win to B
        elif pbWins2 == 3:
            pbMatches += 1; pbWins2 = 0

		#this is just printing up the summary
    print("\nPlayer A wins>>", paWins,' ',"Win percentage>>", round((paWins / nGames) * 100, 2),'%')
    print("Player B wins>>", pbWins,' ',"Win percentage>>", round((pbWins / nGames) * 100, 2),'%')
    print("\nPlayer A wins by shutout>>", shutoutsA,' ',"Win % by shutout>>", round((shutoutsA / nGames) * 100, 2),'%')
    print("Player B wins by shutout>>", shutoutsB,' ',"Win % by shutout>>", round((shutoutsB / nGames) * 100, 2),'%')
    print("\nPlayer A match wins>>", paMatches,)
    print("Player B match wins>>", pbMatches,)
#defines main function
def main():
		#calls intro
    Intro()
		#gets inputs
    probPA = float(input("\nEnter the probability of player A winning>>"))
    probPB = float(input("Enter the probability of player B winning>>"))
    nGames = int(input("How many games will be played?>> "))
		#fancy formatting
    print("\n----------------------------------------------------")
		#call simGame function
    simGame(nGames, probPA, probPB)
    print("\n----------------------------------------------------")
main()