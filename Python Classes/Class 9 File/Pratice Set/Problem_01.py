with open("poem.txt") as f :
    content = f.read()
    
if ("Twinkle" in content):
    print("The word twinkle is present")
    
else :
    print("The word twinkle is not present")    