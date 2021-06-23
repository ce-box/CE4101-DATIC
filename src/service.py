import os,csv
from src.model import User

class UserService:

    def __init__(self):
        self.table_name = '.users.csv'

    
    def list_clients(self) -> list:
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f,fieldnames=User.schema())
            return list(reader) 