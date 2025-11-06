from controllers.app_controller import create_app
from utils.create_db import create_db
from mqtt_listener import start_thread

app = create_app()
start_thread(app)