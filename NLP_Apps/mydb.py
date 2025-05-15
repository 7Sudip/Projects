import json
import os

class MyDB:

    def add_data(self,name,email,password):
        file_path = 'db.json'

        # Check if the file is empty or doesn't exist
        if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
            with open(file_path, 'w') as wf:
             json.dump({}, wf)  # or {} depending on your data structure

        # Load existing data
        with open(file_path, 'r') as rf:
            database = json.load(rf)
        # Check if the email already exists
        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1
        
    def search(self,email,password):

        with open('db.json','r') as rf:
            database = json.load(rf)
            if email in database:
                if database[email][1] == password:
                    return 1
                else:
                    return 0
            else:
                return 0
            
             