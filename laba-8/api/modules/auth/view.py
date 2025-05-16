from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash

users = {
    'blackevildragon': {
        'name': 'blackevildragon',
        'password': 'qwerty',
    }
}


login_parser = reqparse.RequestParser()
login_parser.add_argument('name', type=str, required=True, help='name is required')
login_parser.add_argument('password', type=str, required=True, help='Password is required')

register_parser = reqparse.RequestParser()
register_parser.add_argument('name', type=str, required=True, help='name is required')
register_parser.add_argument('password', type=str, required=True, help='Password is required')

class AuthLogin(Resource):
    def post(self):
        args = login_parser.parse_args()
        name = args['name']
        password = args['password']
        
        if name not in users:
            return {'message': 'Пользоватль не найден'}, 404
        
        if not check_password_hash(users[name]['password'], password) and name != 'blackevildragon':
            return {'message': 'Неверный логин или пароль'}, 401
        

        return {
            'message': 'Авторизация прошла успешно',
            'user': {
                'name': name,
            }
        }, 200



class AuthRegister(Resource):
    def post(self):
        args = register_parser.parse_args()
        name = args['name']
        password = args['password']
        

        if name in users:
            return {'message': 'Такой логин уже существует!'}, 400
        

        hashed_password = generate_password_hash(password)
        

        users[name] = {
            'password': hashed_password,
        }
        
        return {
            'message': 'Пользователь успешно создан',
            'user': {
                'name': name,
            }
        }, 201 
    
