from TaskList import TaskList 
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

check_true ="√"
check_false ="X"

task_list = TaskList()

def insertTask():
    name = new_task_entry.get()
    due_date = date_entry.get_date()
    task = task_list.addTask(name=name,due_date=due_date)
    cleanTable()
    fillTable()

    task_list.viewTasks()

def selectedItemId():
    selected_item = list_treeview.selection()
    if selected_item:
        item = selected_item[0]
        item_value = list_treeview.item(item, "text")
        return int(item_value)

def deleteTask():
    task_list.removeTask(selectedItemId())
    cleanTable()
    fillTable()
    task_list.viewTasks()

def fillTable():
    for task in task_list.tasks:
        list_treeview.insert("", "end", text=f"{task.id}", values=(check_true if task.status else check_false, task.name, task.due_date))

def cleanTable():
    for item in list_treeview.get_children():
        list_treeview.delete(item)

# Crear la ventana principal
ventana = tk.Tk()

ventana.title("Tu-Du")
# Configurar el tamaño de la ventana (opcional)
ventana.geometry("800x600")

new_task_label = tk.Label(ventana, text="Task Name")
new_task_label.pack(pady=0)

new_task_entry = tk.Entry(ventana)
new_task_entry.pack(pady=5)

date_entry = DateEntry(ventana, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.pack(padx=20, pady=20)

new_task_button = tk.Button(ventana, text="Create Task", command=insertTask)
new_task_button.pack(pady=5)

list_label = tk.Label(ventana, text="Tasks List")
list_label.pack(pady=0)

list_treeview = ttk.Treeview(ventana)
list_treeview.pack(padx=20, pady=20)

list_treeview['columns'] = ("Status", "Name", "Due Date")
list_treeview.column("#0", width=0, stretch=tk.NO) #No es deformable
list_treeview.column("Status", anchor=tk.CENTER, width=50)
list_treeview.column("Name", anchor=tk.W, width=150)
list_treeview.column("Due Date", anchor=tk.E, width=100)

# Agregar encabezados
list_treeview.heading("#0", text="", anchor=tk.W)
list_treeview.heading("Status", text="Status", anchor=tk.CENTER)
list_treeview.heading("Name", text="Name", anchor=tk.W)
list_treeview.heading("Due Date", text="Due Date", anchor=tk.E)

delete_task_button = tk.Button(ventana, text="Delete Task", command=deleteTask)
delete_task_button.pack(pady=5)

# Iniciar el bucle principal
ventana.mainloop()


# Insertar elementos
# "" : Identificador padre
# end : Posicion a insertar
# text="" : Texto a mostrar en la columna jerarquica (#0)
# values : Tupla de valores a mostrar

# list_treeview.insert("", "end", text="1", values=("True", "Pollo", datetime.today().date()))
