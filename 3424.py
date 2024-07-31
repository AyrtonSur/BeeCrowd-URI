tam = int(input())
sequence = input()
lastLetter = "b"
boolean = True
num = 0
for n in range(tam):
    if lastLetter == sequence[n] and boolean == True and sequence[n] == "a":
        num += 2
        boolean = False
    elif lastLetter != sequence[n]:
        boolean = True
    elif lastLetter == sequence[n] and sequence[n] == "a":
        num += 1 
    lastLetter = sequence[n]

print(num)
