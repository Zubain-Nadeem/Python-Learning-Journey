with open("donkey.txt") as f :
    content = f.read()
    

updated_content = content.replace("donkey" , "######")

with open("donkey.txt" , "w") as f :
    f.write(updated_content)