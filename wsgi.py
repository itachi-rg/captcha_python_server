#uwsgi always expects application, so importing as app does not work
from server import app as application

if __name__ == "__main__":
    application.run()
