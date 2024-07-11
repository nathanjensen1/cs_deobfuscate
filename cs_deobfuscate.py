eNcryPtEd_pASSwOrD = input("Enter Practice CS \"encrypted\" password: ")

from textwrap import wrap
for i in wrap(eNcryPtEd_pASSwOrD, 3):
    print(chr(256 - int(i)), end='')