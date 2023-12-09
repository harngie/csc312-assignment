class InfixToPostfixConverter:
    def __init__(self):
        self.infix = ""
        self.postfix = ""
        self.stack = []

    def get_infix(self, expression):
        self.infix = expression

    def show_infix(self):
        print("Infix Expression:", self.infix)

    def show_postfix(self):
        print("Postfix Expression:", self.postfix)

    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        elif op == '*' or op == '/':
            return 2
        else:
            return 0

    def convert_to_postfix(self):
        self.postfix = ""
        self.stack = []

        for sym in self.infix:
            if sym.isalnum():
                self.postfix += sym
            elif sym == '(':
                self.stack.append(sym)
            elif sym == ')':
                while self.stack and self.stack[-1] != '(':
                    self.postfix += self.stack.pop()
                self.stack.pop()  # Discard the '('
            elif sym in {'+', '-', '*', '/'}:
                while self.stack and self.precedence(self.stack[-1]) >= self.precedence(sym):
                    self.postfix += self.stack.pop()
                self.stack.append(sym)

        while self.stack:
            self.postfix += self.stack.pop()

def main():
    expressions = [
        "A + B - C",
        "(A + B) * C",
        "(A + B) * (C - D)",
        "A + ((B + C) * (E - F) - G) / (H - I)",
        "A + B * (C + D) - E / F * G + H"
    ]

    for expr in expressions:
        converter = InfixToPostfixConverter()
        converter.get_infix(expr)
        converter.convert_to_postfix()
        converter.show_infix()
        converter.show_postfix()
        print()

if __name__ == "__main__":
    main()
