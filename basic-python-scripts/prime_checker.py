# Prime Number Checker

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

if __name__ == "__main__":
    n = 29
    print(f"Is {n} a prime number?", is_prime(n))
