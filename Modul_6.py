import time

def get_thread(thread_time):
    time.sleep(1)
    print(thread_time)

list_1 = ('One', 'Two', 'Three', 'Four', 'Five')

for i in list_1:
    get_thread(i)

