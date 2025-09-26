from models import Task
from data import db, shema

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def load_tasks(self):
        self.tasks.clear()
        task_dicts = db.get_tasks()
        for i in task_dicts:
            self.tasks.append(i)
        return self.tasks

    def add_tasks(self,nom,description,priority,status):
        db.add_tasks(nom,description,priority,status)
        self.load_tasks()

        
    def delete_task(self,task_id):
        if(db.check_task(task_id)):
            db.delete_task(task_id)
            self.load_tasks()
            return "task deleted sucesfully"
        else:
            return "task not exist"
        

    def update_tasks(self,task_id,nom,description,priority,status):
        db.update_task(task_id,nom,description,priority,status)
        self.load_tasks()





    
    

