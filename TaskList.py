from Task import Task

class TaskList:
    tasks = []
    task_id_counter = 0

    def addTask(self, name, details=None, due_date=None):
        
        #Creamos nueva tarea
        task = Task(name=name, details=details, due_date=due_date)
        task.id = self.task_id_counter

        self.tasks.append(task)

        self.task_id_counter += 1

        return task
        
    def removeTask(self, task_id):
        for task in self.tasks:
            if task.id == task_id :
                self.tasks.remove(task)

    def changeTaskStatus(self, task_id):
        for task in self.tasks:
            if task.id == task_id :
                task.status = not task.status
            
    def viewTasks(self):
        print("**********Tasks**********")
        for task in self.tasks:
            print(task)
