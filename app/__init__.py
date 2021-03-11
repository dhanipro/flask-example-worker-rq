from flask import Flask
from redis import Redis
import rq
from .config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('background-job', connection=app.redis)

    # Register blueprints
    from app.kyc.view import kyc
    app.register_blueprint(kyc)

    return app