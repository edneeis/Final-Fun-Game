print("Welcome to the Fun Game!\n") 
name = input("Hey, what's your name? \n")
age = int(input("How old are you? \n"))
boring_points = 5  

if age >= 18:
    print("Hooray, you are old enough to play!")
    print("RULES OF THE GAME::::::::::::::::::::::::::::::::::::::::::  You are starting out with 5 boring points. If you get 15 or more boring points you lose the game. If you remain with 5 boring points at the end of the game you win!")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    are_you_playing = input("Are you ready to play? ")

    if are_you_playing == "yes":
        print("Perfect,let's play!\n" )

        
        first_ans = input("First Question: Which activity do you consider fun to do on a Friday night? (dinner/music)? \n")
        if first_ans == "music":
            next_ans = input( " Great Choice! Now tell me if you had to choose an event to buy tickets to attend what would you choose? (hockey game/comedy show?)\n ")
       
            if next_ans == "comedy show": 
                print("That's right and I bet you'll bust a gut at that comedy show. Nice choice!\n")
 
            elif next_ans == "hockey game":
                print("Woah nerd are you sure? That sounds so boring you gain 5 boring points for that ridiculous answer!\n")
            boring_points += 10

        
      
        


            next_ans = input("Next question: A friend randomly texts you and says Universal Studios is having a Halloween drive thru exhibit for one night only. Do you go (yes/no)? \n")

            if next_ans == "no":
                  print("Unfreak-in believable! You would pass up such a fun event? Thats it, you get 10 boring points for that! That means you now have", boring_points,  "boring points and you lost the game and are automatically now the CEO of Boring Inc! Have a nice life!\n")
                  print("You have", boring_points, "total boring points")
                  boring_points += 10


             

                            
            else:
                  print("You won!! You kept your boring score down and Won the game. You really are so fun!")


         


        else:
          print("Dinner?!? Seriously?! You can do that on any night!10 boring points for you! You now have 15 boring points and lost\n ")
          boring_points += 10


    else:
      print("Ok thanks for stopping by")

else:
    print("Unfortunately you are not old enough to play :(")