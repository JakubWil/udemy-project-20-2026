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