class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def binary_to_decimal(binary_str):
    stack = Stack()
    decimal = 0
    weight = 0

    for bit in binary_str[::-1]:  # Process bits from right to left
        if bit == '1':
            decimal += 2**weight
        weight += 1

    return decimal

def main():
    binary_numbers = ["11000101", "10101010", "11111111", "10000000", "1111100000"]

    for binary_num in binary_numbers:
        decimal_num = binary_to_decimal(binary_num)
        print(f"Binary: {binary_num} --> Decimal: {decimal_num}")

if __name__ == "__main__":
    main()
