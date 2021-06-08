import random
number = random.randint(0, 100)
print(number)
counter = 0
left = int(0)
right = int(100)

'''Функция делает разбивку числа, из диапазона, на двое, в данном случае от 1 до 100. 
При этом проверяя в какой половине после разбивки находится число! 
Пока не угадает загаданное число.'''

while left < right:
  counter += 1
  middle = (left + right) // 2
  print("left: ", left, "right: ", right, "middle: ", middle)
  if number == left or number == right or number == middle:
    print(counter)
    break
  if number < middle:
    right = middle
  else:
    left = middle
