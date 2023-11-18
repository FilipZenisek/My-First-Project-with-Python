# Write your code here
"""
print('Prices:\n'
      'Bubblegum: $2\n'
      'Toffee: $0.2\n'
      'Ice cream: $5\n'
      'Milk chocolate: $4\n'
      'Doughnut: $2.5\n'
      'Pancake: $3.2')
"""

bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80
total_income = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

print('Earned amount:\n'
      f'Bubblegum: ${bubblegum}\n'
      f'Toffee: ${toffee}\n'
      f'Ice cream: ${ice_cream}\n'
      f'Milk chocolate: ${milk_chocolate}\n'
      f'Doughnut: ${doughnut}\n'
      f'Pancake: ${pancake}\n'
      f'\nIncome: ${total_income}')

staff_expenses = int(input('Staff expenses: $'))
other_expenses = int(input('Other expenses: $'))
print(f'Net income: ${total_income - (staff_expenses + other_expenses)}')
