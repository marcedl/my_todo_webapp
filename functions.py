FILEPATH = (r"C:\Users\leona\OneDrive\Escritorio\Python Mega Course Build 20 Apps\app01_web\todos.txt")

def get_todos(filepath=FILEPATH):
  with open(filepath, "r") as file_local:
    todos_local = file_local.readlines()
  return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
      file.writelines(todos_arg)  


