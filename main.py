def list_todos(todos):
    """
        List todos
    """

def add_todo(todos):
    """
        Add todos
    """

def edit_todo(todos):
    """
        Edit todos
    """

def delete_todo(todos):
    """
        Edit todos
    """

def menu(todos):
    print("What would you like to do?")
    print("1. List todos")
    print("2. Add a todo")
    print("3. Edit a todo")
    print("4. Delete a todo")
    print("5. Quit")
    choice = input("> ")
    if choice == "1":
      list_todos(todos)
    elif choice == "2": 
      add_todo(todos)
    elif choice == "3": 
      edit_todo(todos)
    elif choice == "4": 
      delete_todo(todos)
    elif choice == "5": 
      print("Bye!")
      exit(0)
    else: 
      print("Ohh no! Invalid input.")
    menu(todos)

def main():
    print("Welcome to your todo list!")
    todos = []
    menu(todos)

main()