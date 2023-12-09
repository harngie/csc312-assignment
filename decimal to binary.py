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

def decimal_to_binary(decimal_num):
    stack = Stack()

    while decimal_num > 0:
        remainder = decimal_num % 2
        stack.push(remainder)
        decimal_num //= 2

    binary_str = ""
    while not stack.is_empty():
        binary_str += str(stack.pop())

    return binary_str if binary_str else "0"

def main():
    decimal_numbers = [13, 42, 255, 128, 240]

    for decimal_num in decimal_numbers:
        binary_num = decimal_to_binary(decimal_num)
        print(f"Decimal: {decimal_num} --> Binary: {binary_num}")

if __name__ == "__main__":
    main()
