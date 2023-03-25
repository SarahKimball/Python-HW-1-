age = -7
isBirthday = True

if age >= 21: 
    print("You can drink")
    if isBirthday:
        print("Happy Bday here is a free marg")
elif age >= 18:
    print("You can come on but no drinking")
    if isBirthday:
        print("here is a FREE juice")
elif age <= -1:
    print("this is not possible")
else: 
    print("sorry GO HOME")
    