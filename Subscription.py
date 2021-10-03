import json
class Subscription:

    def __init__(self):
        self.subs = dict()

    def add_subscription(self, name:str, renew:int):
        
        if name in self.subs:
            raise ValueError(f'{name} Already Subscripted')
        else:
            self.subs[name] = renew

    def remove_subscription(self, name:str):
        if name not in self.subs:
            raise ValueError(f'Unable to remove, you did not subscribe to {name}')
        else:
            del self.subs[name]

    def load(self, filename:str):
        with open(filename) as json_file:
            self.subs = json.load(json_file)

    def save(self, filename:str):
        with open(filename, 'w') as outfile:
            json.dump(self.subs, outfile)

    def display(self):
        print(self.subs)