ob_pass = input("Enter Practice CS obfuscated password: ")
split = []

for i in range(int(len(ob_pass)/3)):
    split.append(ob_pass[0 + i*3] + ob_pass[1 + i*3] + ob_pass[2 + i*3])

for i in range(len(split)):
    split[i] = chr(256 - int(split[i]))

print(*split, sep='')