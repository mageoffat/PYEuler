y = 0
x = 0
MAX = 999
for x in range(MAX):
    if x%3== 0 or x%5== 0:
        y += x
    x += 1
print(y)
