import requests
import time

# Функция для проверки работоспособности прокси
def test_proxy(proxy):
    try:
        start_time = time.time()
        response = requests.get('http://example.com', proxies={"http": proxy, "https": proxy}, timeout=1)
        end_time = time.time()
        ping_time = round((end_time - start_time) * 1000)  # Преобразование времени из секунд в миллисекунды
        if response.status_code == 200:
            print(f"Proxy {proxy} работает. Пинг: {ping_time}ms")
            return True
    except:
        print(f"Proxy {proxy} не работает.")
        return False

# Чтение списка прокси из файла
input_file = "proxyall.txt"

with open(input_file, 'r') as f:
    proxies = f.read().splitlines()

print("Проверка прокси в процессе:")
for proxy in proxies:
    if test_proxy(proxy):
        with open("working_proxies.txt", 'a') as f:
            f.write(proxy + '\n')

print("Все прокси проверены. Рабочие прокси записаны в файл working_proxies.txt")
