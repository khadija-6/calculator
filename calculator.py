import time

print("My name is khadija\nI use pogram to use with python")

print("if you want to  addition click A\nif you want to subtract click S\nif you want to muttply click X\nif you want to divid click D")


choise = input("\Wich leter?\n ").upper()

numberX = int(input("Write the fast number: "))
numberY = int(input("write the second number "))

addition = "A"
subtract = "S"
muttply = "X"
divid = "D"


if choise == addition:
    answer = numberX + numberY
    print(answer)
elif choise == subtract:
    answer = numberX - numberY
    print(answer)
elif choise == muttply:
    answer = numberX * numberY
    print(answer)
elif choise == divid:
    answer = numberX / numberY
    print(answer)
else:
    print("use  the intraction above")

print("wait for 5 second.....")

time.sleep(5)

