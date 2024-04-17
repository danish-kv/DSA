stack = []
def push():
    element = input('Push an element to stack')
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print('stack is empty!')
    else:
        e = stack.pop()
        print(f'"{e} "is poped from stack')
        print(stack)

while True:
    print('Select any option \n1. push \n2. pop \n3. Exit')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('wrong option')