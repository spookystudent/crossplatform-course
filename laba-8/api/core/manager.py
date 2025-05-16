from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager


from typing import List

from modules.base import InterfaceModule
from modules.hello import HelloModule
from modules.auth import AuthModule


class Application:

    flask: 'Flask' = None
    router: 'Api' = None

    modules: dict = {}

    def __init__(self, __name__):
        self.flask = Flask(__name__)
        self.router = Api(self.flask)

        self.flask.config['JWT_SECRET_KEY'] = 'asdy98awohq3rio8yfahojop-090-89120*()&*^(&*^tfuyhGJJKHk)'  # В продакшене используйте надежный ключ!
        jwt = JWTManager(self.flask)


        self.init_modules(
            modules=[
                HelloModule,
                AuthModule,
            ]
        )


    def init_modules(self, modules: List['InterfaceModule']):
        for module in modules:
            self.modules[module.get_name()] = module(router=self.router)