import Configuracion as a

class Task(a.db.Model):
    
    id = a.db.Column(a.db.Integer, primary_key=True)
    title = a.db.Column(a.db.String(70), unique=True)
    description = a.db.Column(a.db.String(100))
    
    
    def __init__(self, title, description):
        self.title=title
        self.description=description
        
a.db.create_all()