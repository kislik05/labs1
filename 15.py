"""Но мы можем комбинировать строки и числа, используя этот format()метод!

Метод format()принимает переданные аргументы, форматирует их и помещает в строку, где {}находятся заполнители:

Пример
Используйте format()метод для вставки чисел в строки:
"""
my = 18
mom = 45
txt = "My name is John, and I am {}, but my mom is {}"
print(txt.format(my, mom))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(itemno, quantity, price))