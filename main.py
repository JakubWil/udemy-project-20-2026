import functions as f
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is: {now}")

while True:

    user_action = input("Type add,show, edit exit: ").strip().lower()
    
    
    if user_action.startswith('add'):
            todo = user_action[4:] + "\n"


            todos = f.get_todos("todos.txt")
            
            todos.append(todo)

            f.write_todos(todos, "todos.txt")
                

    elif user_action.startswith('show'):

            todos = f.get_todos("todos.txt")

            print("Your todos:")
            for i, item in enumerate(todos):
                item = item.strip('\n')
                print(f"{i + 1}. {item}")

            
    elif user_action.startswith('edit'):
            try:
            
                index = int(user_action[5:]) - 1

                todos = f.get_todos("todos.txt")

                new_todo = input("Enter the new todo: ") + "\n"

                todos[index] = new_todo

                f.write_todos(todos, "todos.txt")
            except ValueError:
                print("Please enter a valid number for the todo index.")

    elif user_action.startswith('complete'):
        
        try:
            
            index = int(user_action[9:]) - 1
        
            todos = f.get_todos("todos.txt")

            todos.pop(index) 

            f.write_todos(todos, "todos.txt")
        except IndexError:
            print("There is no todo with that number.")

    elif user_action.startswith('exit'):
            print("Exiting the todo app.")
            break
    
    else:
            print("Invalid command. Please try again.")

    