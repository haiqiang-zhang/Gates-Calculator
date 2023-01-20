'''
Author: Haiqiang Zhang
'''

class Stack:
    def __init__(self):
        self.__items = []

    def __str__(self):
        return "Stack: {}".format(self.__items)

    def __len__(self):
        return len(self.__items)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__items == other.__items
        else:
            return False

    def clear(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def peek(self):
        return self.__items[len(self.__items) - 1]

    def push_list(self, a_list):
        self.__items = self.__items + a_list

    def multi_pop(self, number):
        if number <= len(self.__items):
            number = -number
            self.__items = self.__items[:number]
            return True
        else:
            return False

    def copy(self):
        r = Stack()
        r.push_list(self.__items)
        return r

    def size(self):
        return len(self.__items)



def is_balanced_brackets(text):
    s = Stack()
    for index in range(len(text)):
        if text[index] == "(" or text[index] == "[" or text[index] == "{":
            s.push(text[index])
        elif s.size() != 0:
            if text[index] == ")" and s.peek() == "(":
                s.pop()
            elif text[index] == "]" and s.peek() == "[":
                s.pop()
            elif text[index] == "}" and s.peek() == "{":
                s.pop()
            elif text[index] == ")" or text[index] == "]" or text[index] == "}":
                return False
        elif text[index] == ")" or text[index] == "]" or text[index] == "}":
            return False
    if s.size() == 0:
        return True
    else:
        return False


def evaluate_postfix(postfix_list):
    s = Stack()
    for index in range(len(postfix_list)):
        if postfix_list[index] == '|':
            temp_former_number = s.peek()
            s.pop()
            s.push(int(str(bin(int(temp_former_number) + 1))[-1]))
            continue
        try:
            s.push(int(postfix_list[index]))
        except:
            b = s.peek()
            s.pop()
            a = s.peek()
            s.pop()
            s.push(compute(a, b, postfix_list[index]))
    return s.peek()


def compute(number1, number2, operator):
    if operator == '+':
        if number1 + number2 > 0:
            return 1
        else:
            return 0
    elif operator == '*':
        if number1 * number2 > 0:
            return 1
        else:
            return 0


def convert_infix_to_postfix(infix):
    output_string = []
    s = Stack()
    for index in range(len(infix)):
        if infix[index].isnumeric() == True:
            output_string.append(infix[index])
        elif infix[index] == '(' or infix[index] == '|':
            s.push(infix[index])
        elif infix[index] == "*" or infix[index] == "+":
            while s.is_empty() != True and s.peek() != "(":
                output_string.append(s.peek())
                s.pop()
            s.push(infix[index])
        elif infix[index] == ")":
            while s.peek() != '(':
                output_string.append(s.peek())
                s.pop()
            s.pop()
    while s.is_empty() != True:
        output_string.append(s.peek())
        s.pop()
    return output_string


def word_to_num(A, B, C, infix_list):
    fixed_list = infix_list.copy()
    output_tuple = ()

    for index in range(8):
        temp_list = fixed_list.copy()
        for index2 in range(len(infix_list)):
            if fixed_list[index2] == 'A':
                temp_list[index2] = str(A[index])
            if fixed_list[index2] == 'B':
                temp_list[index2] = str(B[index])
            if fixed_list[index2] == 'C':
                temp_list[index2] = str(C[index])
        output_tuple += (temp_list,)
    return output_tuple


def print_table(A, B, C, prompt_list):
    print('A | B | C || Output')
    print('--|---|---||-------')
    for index in range(len(prompt_list)):
        print(A[index], B[index], C[index], prompt_list[index], sep='   ')


def main():
    A = [0, 0, 0, 0, 1, 1, 1, 1]
    B = [0, 0, 1, 1, 0, 0, 1, 1]
    C = [0, 1, 0, 1, 0, 1, 0, 1]
    print()
    input_formula = input('Please input the gates formula: ')
    if is_balanced_brackets(input_formula):
        infix_list = []
        for index in range(len(input_formula)):
            infix_list.append(input_formula[index])
        infix_tuple = word_to_num(A, B, C, infix_list)
        postfix_tuple = ()
        for index in range(len(infix_tuple)):
            postfix_tuple += (convert_infix_to_postfix(infix_tuple[index]),)
        output_list = []
        for index in range(len(postfix_tuple)):
            output_list.append(evaluate_postfix(postfix_tuple[index]))
        print_table(A, B, C, output_list)
    else:
        print('Input Error, try Again')
    main()


if __name__ == '__main__':
    main()


# (A|*B|*C|)+(A|+B|+C)|