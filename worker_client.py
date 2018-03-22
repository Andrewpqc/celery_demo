from celery_app_worker.task1 import add
from celery_app_worker.task2 import sub
#下面两个函数不会阻塞
a=add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)
b=sub.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)


c=add.apply_async(args=[2,8],countdown=10) #10秒之后执行任务

from datetime import datetime,timedelta
#指定任务被调度的具体时间，参数类型是 datetime,使用这个参数可以指定在某一天的某一个时刻执行某一个任务
d=add.apply_async(args=[1,2],eta=datetime.utcnow() + timedelta(seconds=10))

#expires可以指定过期时间，其类型为int或者datetime
e=add.apply_async(args=[3, 7], expires=10)  # 10 秒后过期

print('hello world')
print(a.get())
print(b.get())