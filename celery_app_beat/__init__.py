from celery import Celery
app = Celery('demo')                                # 创建 Celery 实例
app.config_from_object('celery_app_beat.celeryconfig')   # 通过 Celery 实例加载配置模块
