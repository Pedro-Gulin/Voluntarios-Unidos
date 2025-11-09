# controllers/app_controller.py
from flask import Flask, render_template, request, redirect, url_for, flash
from controllers.users_controller import user
from models import db
import os
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from models.user.users import Users
from models.voluntarios.voluntarios import Voluntarios
from controllers.voluntarios_controller import voluntarios
from controllers.areas_controller import areas_
from controllers.atuacao_controller import atuacao
from models.voluntarios.areas import Areas
from models.voluntarios.atuacao import Atuacao
from controllers.ponto_controller import ponto_
from models.voluntarios.ponto import Ponto
from controllers.ponto_controller import processar_tag
import paho.mqtt.client as mqtt
import threading
from controllers import shared_state
from controllers.shared_state import ultima_tag
from models.voluntarios.escala import Escala
from controllers.escala_controller import escala_
from models.voluntarios.habilidades import Habilidades
from controllers.habilidades_controller import habilidades_
from models.voluntarios.habilidade_voluntario import Habilidade_voluntario
from controllers.habilidade_voluntario_controller import habilidade_voluntario_
from models.voluntarios.nucleo_voluntariado import nucleo_voluntariado
from controllers.nucleo_voluntariado_controller import nucleo_voluntariado_
from controllers.relatorios_controller import relatorios_
from flask import current_app

MQTT_BROKER = "broker.mqttdashboard.com"
MQTT_TOPIC_SEND = "exp.criativas/pcparaesp"
MQTT_TOPIC_RECEIVE = "exp.criativas/espparapc"


def on_message(client, userdata, message):
    with current_app.app_context():
        tag = message.payload.decode()
        shared_state.ultima_tag = tag
        print(f"Tag recebida: {tag}")

        try:
            resultado = processar_tag(tag)
            client.publish(MQTT_TOPIC_SEND, resultado)
        except Exception as e:
            print("Erro no processamento:", e)


def start_mqtt():
    client = mqtt.Client(client_id="teste_flask_mqtt")
    client.on_message = on_message
    client.connect(MQTT_BROKER)
    client.subscribe(MQTT_TOPIC_RECEIVE)
    client.loop_start()
    return client

def create_app():
    app = Flask(__name__,
                template_folder="./views/",
                static_folder="./static/",
                root_path="./")

    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        db_url = "mysql+pymysql://root:1234@localhost:3307/voluntarios_cajuru"

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'rex2704'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'connect_args': {'charset': 'utf8mb4'},
    'execution_options': {'schema_translate_map': None}
    }

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')

            user = Users.query.filter_by(email=email).first()

            if not user or user.password != password:
                flash('Email ou senha incorretos!')
                return redirect(url_for('home'))

            login_user(user)
            flash('Login realizado com sucesso!')
            return redirect(url_for('home'))

        return render_template('index.html')

    @app.route('/')
    def index():
        return render_template("login.html")

    @app.route('/home')
    def home():
        return render_template("index.html")

    @app.route('/users')
    @login_required
    def users():
        users = Users.get_users()
        return render_template("users.html", users=users)

    @app.route('/listar_voluntarios')
    def listar_voluntarios():
        voluntarios = Voluntarios.buscar_voluntarios()
        return render_template("listar_voluntarios.html", voluntarios = voluntarios)

    @app.route('/areas')
    def areas():
        areas = Areas.buscar_areas()
        return render_template("listar_areas.html", areas=areas)

    @app.route('/atuacao')
    def atuacao_():
        atuacoes = Atuacao.buscar_atuacoes()
        return render_template("listar_atuacoes.html", atuacoes=atuacoes)
    
    @app.route('/chama_ponto')
    def chama_ponto():
        return render_template("chama_ponto.html")

    @app.route('/ponto')
    def pontos():
        pontos = Ponto.buscar_pontos()
        return render_template("listar_pontos.html", pontos = pontos)
    
    @app.route('/vincular_tag')
    def vincular_tag():
        return render_template("/cadastrar_ponto.html")

    @app.route("/ultima_tag")
    def ultima_tag_route():
        from controllers.shared_state import ultima_tag
        return ultima_tag if ultima_tag else "Nenhuma tag lida ainda"

    @app.route('/escalas')
    def escalas():
        escalas = Escala.buscar_escalas()
        return render_template("escalas.html", escalas = escalas)

    @app.route('/habilidades')
    def habilidades():
        habilidades = Habilidades.buscar_habilidades()
        return render_template("habilidades.html", habilidades = habilidades)

    @app.route('/habilidade_voluntario')
    def habilidade_voluntario():
        habilidades_voluntario = Habilidade_voluntario.buscar_habilidade_voluntario()
        return render_template("habilidade_voluntario.html", habilidades_voluntario = habilidades_voluntario)

    @app.route('/nucleo_voluntariado')
    def nucleo_voluntariadoss():
        nucleos_voluntariados = nucleo_voluntariado.buscar_nucleo_voluntarios()
        return render_template("nucleo_voluntariado.html", nucleos_voluntariados = nucleos_voluntariados)

    @app.route('/relatorios')
    def relatirioss():
        return render_template("relatorios.html")

    app.register_blueprint(user, url_prefix='/')
    app.register_blueprint(voluntarios, url_prefix='/')
    app.register_blueprint(areas_, url_prefix='/')
    app.register_blueprint(atuacao, url_prefix='/')
    app.register_blueprint(ponto_, url_prefix='/')
    app.register_blueprint(escala_, url_prefix='/')
    app.register_blueprint(habilidades_, url_prefix='/')
    app.register_blueprint(habilidade_voluntario_, url_prefix='/')
    app.register_blueprint(nucleo_voluntariado_, url_prefix='/')
    app.register_blueprint(relatorios_, url_prefix='/')

    mqtt_thread = threading.Thread(target=start_mqtt)
    mqtt_thread.daemon = True
    mqtt_thread.start()

    return app