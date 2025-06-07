# створення змінних: назва_змінної = значення
# назви можуть містити літери, цифри та символи підкреслення
my_variable = "значення"

# типи даних
age = 25  # int
price = 19.99  # float
name = "Vlad"  # str

# input() - функція для введення даних з клавіатури
nickname = input("Enter your nickname:")

print(f"Hello, dear {nickname} !")

# оператори
print("Vlad" + "Oleg")  # "VladOleg" конкатенація рядків
print("Vlad" * 3)  # "VladVladVlad" повторення рядка
# "Vlad" * "Oleg"  # помилка, не можна множити рядки

# перетворення типів даних
price = float("123.5")  # перетворення рядка в дробове число
number = int("123")  # перетворення рядка в ціле число

w = int(input("Enter width: "))
h = int(input("Enter height: "))

print(f"Площа прямокутника зі стороною {w} та {h} = {w * h} см^2")

# Завдання: знайти площу кола по радіусу, який вводить користувач
import math

radius = float(input("Enter radius: "))

print(f"Площа кола з радіусом {radius} = {round(math.pi * radius ** 2, 1)} см^2")
