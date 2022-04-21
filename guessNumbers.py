import random

print("Welcome to the Guess numbers game")

tempFile = open('file.txt', 'r')
lines= tempFile.readline()
metaDataVars= lines.split(",")
tempFile.close()

gamesPlayed= int(metaDataVars[0]) | 0 
print("You have played ",gamesPlayed," games")

wins = int(metaDataVars[1]) | 0
print("You have won ",wins," games")

lostGames = int(metaDataVars[2]) | 0
print("You have lost ",lostGames," games")

playAgain = "yes"

while playAgain =="yes" or playAgain =="Y" or playAgain =="y":
    turnsLeft=10
    randomNumber = random.randint(1,100)
    gamesPlayed+=1
    allTrials =[]
   
    while(turnsLeft > 0):
        userGuessedNumber = (int)(input("Please enter a number between 1 & 100 "))
        if(userGuessedNumber > 100 or userGuessedNumber <= 0 ):
            print("Your number is out of range")
            print("You have ",turnsLeft," turns left")
            continue
        elif(userGuessedNumber in allTrials ):
            print("Your have entered this number before")
            print("You have ",turnsLeft," turns left")
            continue
        elif(userGuessedNumber == randomNumber):
            print("You have guessed the number") 
            # win = True
            wins+=1 
            playAgain =(input("Do you want to play again? (y/n) "))
            if(playAgain =="yes" or playAgain =="Y" or playAgain =="y"):
                pass
            else:
                exit()
            randomNumber = random.randint(1,100)
            gamesPlayed+=1
            allTrials =[]
            turnsLeft-=1
            print("You have ",turnsLeft," turns left")  
        elif(userGuessedNumber > randomNumber):
            print("Your number is bigger than the required number")
            turnsLeft-=1
            print("You have ",turnsLeft," turns left")
            allTrials.append(userGuessedNumber)
            continue    
        elif(userGuessedNumber < randomNumber):
            print("Your number is smaller than the required number")
            turnsLeft-=1
            print("You have ",turnsLeft," turns left")
            allTrials.append(userGuessedNumber)
            continue  


    print("You have finished all of your trials")
    lostGames+=1
    playAgain =(input("Do you want to play again? (y/n)"))
 
print("Thanks for playing")
tempFile = open('file.txt', 'w')
Line = [str(gamesPlayed),",",str(wins),",",str(lostGames)]
tempFile.writelines(Line)
tempFile.close()







    

     

