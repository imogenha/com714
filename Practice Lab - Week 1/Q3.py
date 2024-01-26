# Q3) Loop
# Loop through a reversed range with loop size dependent on user input. If statement used at range 0 to change output.

question = int(input("How many times should I break free?"))
print(question)

print("I'm stronger than I've been before...")

for i in reversed(range(question)):
    if i == 0:
        print('Cause I can\'t resist it no more!')
        break
    var = str(i)
    print("..." + var + ": this is the part when I break free")