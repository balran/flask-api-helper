from app import db
from dataclasses import dataclass

@dataclass
class {{package_name_class}}(db.Model):
    __tablename__ = '{{package_name}}'
    id: int
    
    id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self):
        pass
        
    def __repr__(self):
        pass
