#j2 - epidemiology (2020)

p = int(input())
n = int(input())
r = int(input())

day = 0
total_infected = n
newly_infected = n

while total_infected <= p:
    old_total = total_infected
    total_infected += newly_infected * r
    newly_infected = total_infected - old_total
    
    day += 1
    
print(day)