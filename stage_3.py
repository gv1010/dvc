with open("artifacts01.txt", "r") as f:
    text = f.read()

with open("artifacts02.txt", "w+") as f:
    f.write("Input from stage3")

print(text)
print("end-of stage3")