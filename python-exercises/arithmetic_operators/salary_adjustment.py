salary = float(input("What is the employee's salary? R$ "))
salary_increase = (salary) + ((15 * salary) / 100)
print(f"An employee who earned R${salary}, with 15% increase, starts to receive R${round(salary_increase,2)}.")