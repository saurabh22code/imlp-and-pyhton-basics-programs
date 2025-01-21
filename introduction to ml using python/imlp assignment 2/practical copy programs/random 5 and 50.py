def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)
num = int(input("Enter a number: "))
print(f"{num} is prime" if is_prime(num) else f"{num} is not prime")
n