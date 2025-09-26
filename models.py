class Task:

    def __init__(self,nom:str,description:str,date,priority:str,status:str):
        self.nom = nom
        self.description = description
        self.priority = priority
        self.status = status
        self.date = date

    def to_tuple(self):
        return (self.nom, self.description, self.priority, self.status)

