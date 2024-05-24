class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, item):
        self.myStack.append(item)

    def pop(self):
        if self.is_empty():
            deleted_item = self.myStack.pop()
            return deleted_item
        else:
            return None

    def peek(self):
        return self.myStack[-1] if self.is_empty() else None

    def size(self):
        return len(self.myStack)

    def is_empty(self):
        return True if self.myStack else False


def validation_sequence(sequence):
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']

    stack = Stack()

    if len(sequence) % 2 == 0:
        for x in sequence[:int(len(sequence)/2)]:
            stack.push(x)

        for y in sequence[int(len(sequence)/2)::]:

            if stack.peek() in open_brackets and open_brackets.index(stack.peek()) == close_brackets.index(y):
                stack.pop()
            else:
                return "Not balanced"

        return "Balanced"

    else:
        return "Not balanced"


assert validation_sequence("{{[()]}}"), "Balanced"
assert validation_sequence("(((([{}]))))"), "Balanced"

assert validation_sequence("}{}"), "Not balanced"
assert validation_sequence("[[{())}]"), "Not balanced"
assert validation_sequence("{{[(])]}}"), "Not balanced"
assert validation_sequence("[([])((([[[]]])))]{()}"), "Not balanced"
