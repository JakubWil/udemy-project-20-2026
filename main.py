def get_todos(filepath="todos.txt"):

    """
    Odczytuje plik i zapisuje rezultat do tablicy

    Argumenty:
        fielpath: (string): plik tekstowy do odczutu

    
    Zwraca:
        tablice rezultatu odczytu pliku

    """

    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath="todos.txt"):
     
    """
    Zapisuje do pliku tekstowego tablice 

    Argumenty:
        todos: tablica z zadaniami to-do
        fielpath: (string): plik tekstowy do odczutu

    
    Zwraca:
        Nic 

    """
    with open(filepath, "w") as file:
        file.writelines(todos)




while True:

    user_action = input("Type add,show, edit exit: ").strip().lower()
    
    
    if user_action.startswith('add'):
            todo = user_action[4:] + "\n"


            todos = get_todos("todos.txt")
            
            todos.append(todo)

            write_todos(todos, "todos.txt")
                

    elif user_action.startswith('show'):

            todos = get_todos("todos.txt")

            print("Your todos:")
            for i, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{i + 1}. {item}")

            
    elif user_action.startswith('edit'):
            try:
            
                index = int(user_action[5:]) - 1

                todos = get_todos("todos.txt")

                new_todo = input("Enter the new todo: ") + "\n"

                todos[index] = new_todo

                write_todos(todos, "todos.txt")
            except ValueError:
                print("Please enter a valid number for the todo index.")

    elif user_action.startswith('complete'):
        
        try:
            
            index = int(user_action[9:]) - 1
        
            todos = get_todos("todos.txt")

            todos.pop(index) 

            write_todos(todos, "todos.txt")
        except IndexError:
            print("There is no todo with that number.")

    elif user_action.startswith('exit'):
            print("Exiting the todo app.")
            break
    
    else:
            print("Invalid command. Please try again.")

    