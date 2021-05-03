profit, loss = int(input()), int(input())
print("Выручка больше убытков" if profit > loss else "Убыток больше выручки")
if profit > loss:
  print(profit // loss * 100)
  personal = int(input())
print("Прибыль на одного сотрудника составляет:", profit // personal)
