import time

left = str("left")
no = str("no")
yes = str("yes")

print("You are at a path that splits 2 ways, there is a sign with arrows. The arrow pointing left says farm, and the arrow pointing right says town.")

time.sleep(2)

print("which way would you like to go?")

choice1 = str(input())

if choice1 == left:
    print("You walk to the farm and see lots of cattle and fields full of crop. In the distance you see a barn and an old woman in a rocking chair.")
    time.sleep(1)
    print("Would you like to approch the old woman?")
    
    choice2 = str(input())

if choice2 == no:
    print("Ok, there is also lots of cattle.")
    time.sleep(1)
    print("Would you like to go look at the animals?")

if choice2 == yes:
    print("You walk up the old woman, on closer inspection you see her eyes are closed and it looks like she is asleep.")
    time.sleep(1)
    print("Would you like to wake her up?")

choice6 = str(input())

if choice6 == yes:
    print("You shake her and she doesn't move, you feel her pulse and she has none. Freaked out, you run back to where you were.")
    time.sleep(2)
    print("There are also lots of cattle. Would you like to go look at the cattle?")
    
choice5 = str(input())

if choice5 == yes:
    print("There are lots of Cows, Pigs, and Chickens.")
    time.sleep(1)
    print("You see a pig with a ribbon on its head oinking at a spider, it's almost like they are communicating.")
    time.sleep(2)
    print("There is nothing else here, so you walk back to the splitting paths.")

if choice5 == no:
    print("There is nothing else to look at, so you walk back to the splitting paths.")



choice4 = str(input())

if choice4 == yes:
    print("There are lots of Cows, Pigs, and Chickens.")
    time.sleep(1)
    print("you see a pig with a ribbon on its head oinking at a spider, it's almost like they are communicating.")
    time.sleep(1)
    print("There is nothing else here to see, so you walk back to the splitting paths.")





