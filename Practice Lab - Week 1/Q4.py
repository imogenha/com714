# Q4) Function
# Take two parameters from the user, and depending on input, print a 'response'. Input converted to lowercase to
# avoid input issues.


def explain(what, where):
    what = what.lower()
    where = where.lower()
    if what == "monster" and where == "bed":
        print("I'm friends with the monster that's under my bed")
    elif what == "doctor" and where == "hospital":
        print("You're trying to save me, stop holding your breath")
    else:
        print("You think I\'m crazy, yeah, you think I\'m crazy")


explain("head", "wild")