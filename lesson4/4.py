import time
from datetime import datetime


n = int(input('Введите n: '))


def dt_tm():
    t = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    time.sleep(1)
    return t


res = [str(dt_tm()) for i in range(n)]
print(res)
