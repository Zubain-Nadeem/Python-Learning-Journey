p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"


message = input("Enter your comment : ")

message = message.lower()


if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This comment is Scam !")

else:
    print("This comment is not Scam !")