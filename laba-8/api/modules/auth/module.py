from core.router import set_paths

from .view import AuthLogin, AuthRegister

class AuthModule:


    def __init__(self, router):
        set_paths(
            router=router,
            paths={
                '/auth/login/': AuthLogin,
                '/auth/register/': AuthRegister
            }
        )

    @staticmethod
    def get_name():
        return 'AuthModule'