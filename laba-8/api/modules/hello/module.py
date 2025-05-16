from core.router import set_paths

from .view import HelloWorld

class HelloModule:


    def __init__(self, router):
        set_paths(
            router=router,
            paths={
                '/': HelloWorld
            }
        )

    @staticmethod
    def get_name():
        return 'HelloModule'