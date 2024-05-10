with open("myText.txt", "r") as file:
    for line in file:
        x = int(line)
        y = x + 1

with open("myText.txt", "w") as file:
    file.write(f"{y}")
