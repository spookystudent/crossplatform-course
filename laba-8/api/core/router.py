from flask_restful import Api

def set_paths(router: 'Api', paths: dict) -> None:
    for path in paths:
        router.add_resource(paths[path], path)
