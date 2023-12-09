def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors_stack(num):
    stack = []
    factors = []

    # Find prime factors and push them onto the stack
    for i in range(2, num + 1):
        while is_prime(i) and num % i == 0:
            stack.append(i)
            num //= i

    # Pop elements from the stack to get factors in descending order
    while stack:
        factors.append(stack.pop())

    return factors

def main():
    num = int(input("Enter a positive integer: "))
    factors = prime_factors_stack(num)

    if factors:
        print(f"Prime factors of {num} in descending order: {factors}")
    else:
        print(f"{num} has no prime factors.")

if __name__ == "__main__":
    main()
