# Q5) Nesting if statements within a loop, with a range of 5, incrementing points based on output and breaking after
# step 4 with a points total.

points = 0
i = 1
print("Let\'s find out how you sleep...")

for i in range(5):
    if i == 4:
        points = str(points)
        print("You achieved " + points + " points.")
        break

    sleep = input("...Baby, how do you sleep when you lie to me?")
    sleep = sleep.lower()
    if sleep == "very well":
        points -= 10
        print("I'm hopin' that my love will keep you up tonight.")
    elif sleep == "poorly":
        points += 20
        print("All that fear and all that pressure.")
    else:
        points += 0
        print("Love to you is just a game.")