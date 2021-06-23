from flask import Flask, request, make_response, redirect
from flask_cors import CORS
from src.service import UserService

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return 'Welcome to DATIC API!'

@app.route('/datic/api/auth',methods=['POST'])
def authenticate_user():
    if request.method == 'POST':
        email = request.json['email']
        pwd = request.json['pwd']

        user_service = UserService()
        user_list = user_service.list_clients()

        user = [usr for usr in user_list if usr['email'] == email]

        # Check for email in DATIC db
        if user:
            user = user[0]
            # Verify password
            if user['pwd'] == pwd:
                user['pwd'] = '*'
                return user
            else:
                return {'message':'User password is not correct'},400

        else:
            return {'message':f'User {email} not found'},404

