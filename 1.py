print("Доброго времени суток!")
A = input("Введите имя: ")
B = input("Введите фамилию: ")
C = int(input("Введите год рождения: "))
print("Вы уверены, что ввели всё верно?")
print(A, B, C,  sep="_")
input()
Z = A
A = B
B = Z
C = C + 60
print("Фамилия_Имя_ГодРождения+60лет: ")
print(A, B, C,  sep="_")
input()