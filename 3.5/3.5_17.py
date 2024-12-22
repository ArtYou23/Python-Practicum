with open("secret.txt", encoding="UTF-8") as file:
    for symbol in file.read():
        print(chr(ord(symbol) % 128), end="")