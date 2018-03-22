# celery_demo
a small demo of celery application

## 启动异步任务
项目根目录执行下列命令：
``` bash
$ celery -A celery_app_worker worker -loglevel info
```

## 启动定时任务
先在项目根目录执行：
``` bash
$ celery -A celery_app_beat worker -loglevel info
```
然后再开一个终端，同样在根目录执行：
``` bash
$ celery beat -A celery_app_beat
```

或者，同时启动Worker进程和Beat进程：
``` bash
$ celery -B -A celery_app_beat worker --loglevel=info
````