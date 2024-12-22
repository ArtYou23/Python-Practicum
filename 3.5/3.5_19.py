sdvig = int(input())
sdvig = sdvig % 26
ans = []
with open("public", encoding="UTF-8") as f:
    for line in f:
        for letter in line:
            if letter.isalpha():
                d = (ord(letter) + sdvig)
                if letter.isupper():
                    ans.append(chr(d) if d <= 90 else chr(d - 90 + 64))
                if letter.islower():
                    ans.append(chr(d) if d <= 122 else chr(d - 123 + 97))
            else:
                ans.append(letter)
with open("private.txt", "w", encoding="UTF-8") as file_out:
    file_out.writelines(ans)