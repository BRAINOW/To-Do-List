class Task:
    id = None
    name = None
    details = None
    due_date = None
    status:bool = False

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.details = kwargs.get("details","")
        self.due_date = kwargs.get("due_date",None)
        self.status = kwargs.get("status",False)

    def __repr__(self):
        return f"{self.id}: status={self.status} name={self.name}, details={self.details}, due_date={self.due_date}"
