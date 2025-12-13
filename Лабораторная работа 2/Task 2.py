salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

debt = 0
current_spend = spend

for month in range(months):
 if month > 0:
     current_spend *= (1 + increase)
 if salary < current_spend:
     debt += current_spend - salary

money_capital = round(debt)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {money_capital}")
