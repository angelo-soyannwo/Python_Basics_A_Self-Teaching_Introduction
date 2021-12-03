
with open("firstfile.txt", "r") as f:
    with open("secondfile.txt", "a") as f1:
        f1.write("\n")
        for line in f:
            f1.write(line)




