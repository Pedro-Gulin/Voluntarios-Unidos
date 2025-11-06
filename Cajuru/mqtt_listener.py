# mqtt_listener.py
import threading
import paho.mqtt.client as mqtt
from controllers.shared_state import ultima_tag
import controllers.shared_state
from controllers.ponto_controller import processar_tag

MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_TOPIC = "exp.criativas/espparapc"

flask_app = None

def on_message(client, userdata, message):
    tag = message.payload.decode().strip()
    print(f"\n[MQTT] Tag recebida: {tag}")

    controllers.shared_state.ultima_tag = tag

    with flask_app.app_context():
        resultado = processar_tag(tag)
        print(f"[PROCESSAMENTO] {resultado}\n")

def iniciar_mqtt():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(MQTT_BROKER, 1883, 60)
    client.subscribe(MQTT_TOPIC)

    print("\n[MQTT] Conectado e escutando...\n")
    client.loop_forever()

def start_thread(app):
    global flask_app
    flask_app = app

    thread = threading.Thread(target=iniciar_mqtt)
    thread.daemon = True
    thread.start()