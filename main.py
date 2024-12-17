from TaskList import TaskList 
from datetime import datetime


task_list = TaskList()

task_list.addTask(name="Descongelar el pollo")
task_list.addTask(name="Recoger cuarto", details="Ordenar escritorio", due_date=datetime.today().date())

task_list.viewTasks()
task_list.removeTask(1)
task_list.viewTasks()
task_list.changeTaskStatus(0)
task_list.viewTasks()
task_list.changeTaskStatus(0)
task_list.viewTasks()

