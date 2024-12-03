class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': 'pending'
        }
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def update_task(self, index, title, description, due_date, status):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = {
                'title': title,
                'description': description,
                'due_date': due_date,
                'status': status  # Atualiza o status conforme recebido
            }

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]