from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "chave_super_secreta"  # Necessário para utilizar sessões

@app.route('/')
def home():
    # Se não existir uma lista de tarefas na sessão, cria uma nova
    if "tasks" not in session:
        session["tasks"] = [
            {"id": 1, "task": "Revirar garrafas", "done": False},
            {"id": 2, "task": "Colocar areia em pneus parados", "done": False},
            {"id": 3, "task": "Trocar água das plantas a cada 2 dias", "done": False},
            {"id": 4, "task": "Tampar caixas d’água", "done": False},
            {"id": 5, "task": "Limpar ralos e ambientes que possam acumular água parada", "done": False},
        ]
    
    return render_template("index.html", tasks=session["tasks"])

@app.route('/mark/<int:task_id>')
def mark_task(task_id):
    tasks = session["tasks"]  # Recupera a lista de tarefas específica do usuário
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    session["tasks"] = tasks  # Atualiza a lista na sessão do usuário
    return redirect(url_for('home'))

@app.route('/reset')
def reset_tasks():
    tasks = session["tasks"]
    for task in tasks:
        task["done"] = False
    session["tasks"] = tasks  # Reseta as tarefas apenas no dispositivo do usuário
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
