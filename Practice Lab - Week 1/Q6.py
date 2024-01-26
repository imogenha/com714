# Q6) Functions
# Function to describe friend, decision-making based on input.


def describe_friend(friend):
    friend = friend.lower()
    if friend == "50 cent":
        print("He be getting rich or die trying.")
    elif friend == "dr dre":
        print("He be needing California love.")
    elif friend == "rhianna":
        print("She be needing an umbrella.")
    else:
        print("They be cool.")


# Function to nest the first function within another.

def display_friend(friend):
    print(friend + " can be described as follows:")
    describe_friend(friend)


# Logical function tying the prior two together with output dependent on user input.

def run():
    friend = input("Enter a friend\'s name: ")
    term = input("Enter either describe or display: ")
    term = term.lower()
    if term == "describe":
        describe_friend(friend)
    elif term == "display":
        display_friend(friend)
    else:
        print("Invalid command!")


run()