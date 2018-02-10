"""
ID: giliev91
LANG: PYTHON3
TASK: milk
"""
with open("milk.in", "r") as f:
    N, M = map(int, f.readline().strip().split())
    prices = [tuple(map(int, x.strip().split())) for x in f.readlines()]

prices.sort()
milk = 0
cost = 0
for price, amount in prices:
    if milk + amount > N:
        amount = N - milk
    
    milk += amount
    cost += price * amount
    
    if milk == N:
        break

with open("milk.out", "w") as f:
    f.write(str(cost) + "\n")