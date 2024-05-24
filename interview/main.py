class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, item):
        self.myStack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        else:
            deleted_item = self.myStack.pop()
            return deleted_item

    def peek(self):
        return None if self.is_empty() else self.myStack[-1]

    def size(self):
        return len(self.myStack)

    def is_empty(self):
        return False if self.myStack else True


def validation_sequence(sequence):
    open_brackets = ['(', '{', '[']
    close_brackets = [')', '}', ']']

    stack = Stack()

    if len(sequence) % 2 == 0:
        for x in sequence[:int(len(sequence)/2)]:
            stack.push(x)

        for y in sequence[int(len(sequence)/2)::]:
            if stack.peek() in open_brackets and y in close_brackets:
                if open_brackets.index(stack.peek()) == close_brackets.index(y):
                    stack.pop()
            else:
                break

        return "Balanced" if stack.is_empty() else "Not balanced"

    else:
        return "Not balanced"


assert validation_sequence("{{[()]}}") == "Balanced"
assert validation_sequence("(((([{}]))))") == "Balanced"

assert validation_sequence("}{}") == "Not balanced"
assert validation_sequence("[[{())}]") == "Not balanced"
assert validation_sequence("{{[(])]}}"), "Not balanced"
assert validation_sequence("[([])((([[[]]])))]{()}"), "Not balanced"
assert validation_sequence("[([])((([[[]]]))[[{()}"), "Not balanced"
