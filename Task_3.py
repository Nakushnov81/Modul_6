import time
from threading import Thread
import requests as rq


links = ['https://www.google.com', 'https://wordpress.org', 'http://www.microsoft.com', 'http://www.amazon.com', 'https://www.youtube.com']

def get_html(link):
    response = rq.get(link, timeout=2)
    response.encoding = 'utf8'
    return print(response.text)


start_1 = time.time()
for link in links:
    get_html(link)
end_1 = time.time()
treads = [Thread(target=get_html, args=(link, )) for link in links]
start_2 = time.time()
for t in treads:
    t.start()
for t in treads:
    t.join()
end_2 = time.time()
time_delta = (end_1 - start_1) - (end_2 - start_2)
print(f'Разница во времени выполнения {time_delta} с.')