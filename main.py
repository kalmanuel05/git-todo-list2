def list_todos(to_dos):

    print(to_dos)

def add_todo(to_dos):

  print("How many to do's would you like to add")
  
  counter = int(input("> "))
  while counter <= 0: 
    print("ERROR:(Please provide a valid input")
    add_todo(to_dos)

  for i in range(counter): 
     print("Enter to do's")
     to_dos.append(input("> "))

def edit_todo(to_dos):
    
    edit = to_dos.index(input("""What would you like to edit
> """))
    to_dos[edit] = input("""Enter edit
> """)
  
def delete_todo(to_dos): 

   print("Would you like to delete an item or would you like to delete all?")
   
   answer = input("> ")

   if answer == "item": 
    index = to_dos.index(input("""What item would you like to delete
> """))
    del to_dos[index]

   elif answer == "all": 
      del to_dos[:]
   else: 
      menu(to_dos)

   print("""Would you like to delete more?""")
   answer = input("> ")
   if answer == "yes": 
      delete_todo(to_dos)
   else: 
      menu(to_dos)

def menu(to_dos):
    print("""What would you like to do?
1. List todos
2. Add a todo
3. Edit a todo
4. Delete a todo
5. Quit""")
    choice = input("> ")
    if choice == "1":
      list_todos(to_dos)
    elif choice == "2": 
      add_todo(to_dos)
    elif choice == "3": 
      edit_todo(to_dos)
    elif choice == "4": 
      delete_todo(to_dos)
    elif choice == "5": 
      print("Bye!")
      exit(0)
    else: 
      print("Ohh no! Invalid input.")
    menu(to_dos)

def main():
    
    print("Welcome to your todo list!")
    to_dos = []
    menu(to_dos)

main()
