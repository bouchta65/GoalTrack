from data.shema import (MetaData,engine,tasks)
from sqlalchemy import (Select,Insert,update,delete)

def add_task(nom,desc,priority,status):
    with engine.begin() as conn:
        conn.execute(Insert(tasks).values(
            nom = nom,
            description=desc,
            priority=priority,
            status = status
        ))

# add_task("test","test","test","test")

def update_task(task_id,nom=None,desc=None,priority=None,status=None):
    values_updated={}
    if nom is not None:
        values_updated["nom"]=nom
    if desc is not None:
        values_updated["description"]=desc
    if priority is not None:
        values_updated["priority"]=priority
    if status is not None:
        values_updated["status"]=status
    
    if not values_updated:
        print("there is not value to update !!!")

    with engine.begin() as conn:
        conn.execute(update(tasks)
        .where(tasks.c.id == task_id)
        .values(
            **values_updated
        ))

def delete_task(task_id):
    with engine.begin() as conn:
        conn.execute(delete(tasks)
        .where(tasks.c.id==task_id))

# delete_task(2)

    
def affiche_tasks():
    with engine.begin() as conn:
        res = conn.execute(Select(tasks.c.nom,tasks.c.description,tasks.c.priority,tasks.c.status))
        return res

print(affiche_tasks())


