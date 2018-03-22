from celery.schedules import crontab
from datetime import timedelta
BROKER_URL = 'redis://127.0.0.1:6379'               # 指定 Broker
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'  # 指定 Backend
CELERY_TIMEZONE='Asia/Shanghai'                     # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'
CELERY_IMPORTS = (                                  # 指定导入的任务模块
    'celery_app_beat.task1',
    'celery_app_beat.task2'
)

# schedules
CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'celery_app_beat.task1.add',
         'schedule': timedelta(seconds=3),       # 每 30 秒执行一次
         'args': (5, 8)                           # 任务函数参数
    },
    'multiply-at-some-time': {
        'task': 'celery_app_beat.task2.sub',
        'schedule': crontab(hour=9, minute=50),   # 每天早上 9 点 50 分执行一次
        'args': (3, 7)                            # 任务函数参数
    }
}
#
# BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop' # 使用RabbitMQ作为消息代理
#
# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' # 把任务结果存在了Redis
#
# CELERY_TASK_SERIALIZER = 'msgpack' # 任务序列化和反序列化使用msgpack方案
#
# CELERY_RESULT_SERIALIZER = 'json' # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON
#
# CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显
#
# CELERY_ACCEPT_CONTENT = ['json', 'msgpack'] # 指定接受的内容类型