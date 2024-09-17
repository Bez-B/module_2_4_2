# ПОПЫТКА №3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Решение
primes = []
not_primes = []

for i in range(1, len(numbers)):
    for j in range(2, int(numbers[i] ** 0.5)+1):
        is_prime = True
        if numbers[i] % numbers[j] == 0:
            is_prime = False
            not_primes.append(numbers[i])
            break
        if is_prime:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
# Вывод результата
# print()
print('Primes: ', primes)
print('Not Primes: ', not_primes)

