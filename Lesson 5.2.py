# урок 5.2

print ("Введите слово латинскими буквами")
word = str(input().lower())

vw_let = "aeiou"
cn_let = "bcdfghjklmnpqrstvwxyz"

vw_num = 0
cn_num = 0


for i in word:
     if i in vw_let:
         vw_num += 1
     elif i in cn_let:
         cn_num += 1

print (f"Гласных букв - {vw_num}")
print (f"Согласных букв - {cn_num}")

for j in vw_let:
    let = word.count(j)
    if let > 0:
        res = let
    else:
        res = False
    print (f"Букв {j} - {res}")  