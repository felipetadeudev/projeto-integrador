from flask import Flask, render_template, request, redirect, url_for
from task_manager import TaskManager

app = Flask(__name__)
task_manager = TaskManager()

@app.route('/')
def index():
    tasks = task_manager.get_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    task_manager.add_task(title, description, due_date)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    status = request.form.get('status', 'pending')  # Pode vir de 'edit' ou 'conclude' forms
    task_manager.update_task(task_id, title, description, due_date, status)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)