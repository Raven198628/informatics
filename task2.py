money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
while (salary + money_capital > spend):
    money_capital = money_capital + salary - spend  # остаток за месяц
    spend += spend * increase  # индексируем траты
    month += 1  # подсчитываем месяцы
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month)