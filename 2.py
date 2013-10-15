
limit = 4e6
n1 = 0
n2 = 1
sum = 0

while n2 < limit:
    if n2 % 2 == 0:
        sum += n2
    tmp = n2
    n2 = n2 + n1
    n1 = tmp

print sum
