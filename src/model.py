class User:

    def __init__(self, name, email, pwd, role, carrer):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.role = role
        self.carrer = carrer

    def to_dict(self):
        user_dict =  vars(self)
        user_dict['pwd'] = '*'
        return user_dict

    @staticmethod
    def schema():
        return ['name','email','pwd','role','carrer']
        
