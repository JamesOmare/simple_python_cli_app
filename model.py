import datetime

class Todo:
    def __init__(self, task, category,
                 date_added = None, date_completed = None,
                 status = None, posistion = None):
        self.task = task
        self.category = category
        self.date_added = date_added if date_added else datetime.datetime.now().isoformat()
        self.date_completed = date_completed if date_completed else None
        self.status = status if status else 1
        self.position = posistion if posistion else None
        
    def __repr__(self) -> str:
        return f"Todo: {self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position}"
        