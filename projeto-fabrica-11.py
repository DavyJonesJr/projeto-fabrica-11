from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Espalhar lixo", "descricao": "Espalhar o lixo", "concluida": False},
    {"id": 2, "titulo": "Puxar pena", "descricao": "Puxar as penas", "concluida": False}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({"tarefas": tarefas, "total": len(tarefas)})

@app.route("/tasks/<int:id>", methods=["GET"])
def get_task_by_id(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify({"mensagem": "Tarefa encontrada!", "tarefa": tarefa})
        
    return jsonify({"mensagem": "Tarefa não encontrada!"}), 404
 
@app.route("/tasks", methods=["POST"])
def add_task():
    nova_tarefa = request.json

    nova_tarefa["id"] = len(tarefas) + 1
    tarefas.append(nova_tarefa)
    return jsonify({"mensagem": "Tarefa adicionada!", "tarefa": nova_tarefa})

@app.route("/tasks/<int:id>", methods=["PUT"])
def upadte_task(id):
    dados = request.json

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa.update(dados)
            return jsonify({"mensagem": "Tarefa atualizada!"})
        
    return jsonify({"mensagem": "Tarefa não encontrada!"}), 404

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa deletada!"})
        
    return jsonify({"mensagem": "Tarefa não encontrada!"}), 404

if __name__ == '__main__':
    app.run(debug=True)