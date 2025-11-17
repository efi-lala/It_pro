
todo = ["Make your bed","Drink water","Study for 20–30 minutes","Take a short break","Exercise for 5–10 minutes",
"Sleep early"]

def add():
    todo.append(input("Enter new todo: "))
    print(todo)

def remove():
    todo.remove(input("Enter todo to remove: "))
    print(todo)

def main():
    print("Welcomeeeee")
    print("ur todo")
    print(todo)
    print("press 1 to add new todo")
    print("press 2 to remove todo")
    print("press 3 to remove ur all todos")
    
    t = int(input())
    if t == 1:
        add()
    elif t == 2:
        remove()
    elif t == 3:
        todo.clear()
        print("todo cleared")
    else:
        print("no no no no no,invalid input")

while True:
    main()


    
