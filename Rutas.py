import Configuracion as a, Task as t, TaskSchema as ts
from flask import request, jsonify


@a.app.route('/tasks', methods=['POST'])
def create_task():
    
    title = request.json['title']
    description = request.json['description']
    
    new_task = t.Task(title,description)
    a.db.session.add(new_task)
    a.db.session.commit()
   
    return ts.task_schema.jsonify(new_task)


@a.app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = t.Task.query.all()
    result = ts.tasks_schema.dump(all_tasks)
    return jsonify(result)

@a.app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = t.Task.query.get(id)
    return ts.task_schema.jsonify(task)    

@a.app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = t.Task.query.get(id)
    
    title = request.json['title']
    description = request.json['description']
    
    task.title = title
    task.description = description
    
    a.db.session.commit()
    return ts.task_schema.jsonify(task)

@a.app.route('/tasks/<id>',methods=['DELETE'])
def delete_task(id):
    task = t.Task.query.get(id)
    a.db.session.delete(task)
    a.db.session.commit()
    
    return ts.task_schema.jsonify(task)

@a.app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'Welcome to my API'})



if __name__ == "__main__":
    a.app.run(debug=True)