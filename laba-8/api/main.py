from core.manager import Application

manager = Application(__name__)

if __name__ == '__main__':
    manager.flask.run(debug=True)