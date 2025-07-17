numList = []

for i in range(10):
    a = int(input(f"Enter number {i+1} : "))
    numList.append(a)
numList.sort(reverse=True)

print(numList)


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

countlist = []

for num in numList:
    count = 0
    for div in range(1, num + 1):
        if num % div == 0 and isPrime(div):
            count += 1
    countlist.append(count)

print(countlist)

maximum = max(countlist)
idx = countlist.index(maximum)
print(f"Greatest prime divisor is {numList[idx]}, with {maximum} prime divisors in total.")