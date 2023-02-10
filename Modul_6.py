import time
from threading import Thread


def get_thread(thread_time):
    time.sleep(1)
    print(thread_time)


list_1 = ['One', 'Two', 'Three', 'Four', 'Five']
start_1 = time.time()
for i in list_1:
    get_thread(i)
end_1 = time.time()
treads = [Thread(target=get_thread, args=(i+1, )) for i in range(len(list_1))]
start_2 = time.time()
for t in treads:
    t.start()
for t in treads:
    t.join()
end_2 = time.time()
time_delta = (end_1 - start_1) - (end_2 - start_2)
print(f'Разница во времени выполнения {time_delta} с.')
