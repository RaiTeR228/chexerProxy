# chexerProxy

обычная консольная программа, в proxyall.txt вставляете все proxy и запускаете, по окончании проверки рабочие прокси будут в working_proxies.txt файле.

можно вставить прокси через ":" "proxy:port" (работать будет)

пример в терминале:
  Проверка прокси в процессе:
Proxy 51.222.108.216:45512 не работает.
Proxy 159.65.245.255:80 работает. Пинг: 336ms
Proxy 64.227.4.244:8888 работает. Пинг: 327ms
Proxy 165.227.196.37:54940 не работает.
Proxy 5.161.103.41:88 не работает.
Proxy 93.127.215.97:80 не работает.
Proxy 154.16.146.47:80 работает. Пинг: 1182ms
Proxy 198.160.7.15:80 не работает.
Proxy 23.19.244.109:1080 не работает.
Proxy 154.16.146.48:80 не работает.
Proxy 155.94.241.130:3128 работает. Пинг: 377ms
Proxy 155.94.241.134:3128 работает. Пинг: 399ms
Proxy 154.16.146.45:80 не работает.
Proxy 51.161.56.52:80 не работает.
Proxy 138.197.102.119:80 не работает.
Proxy 45.43.11.72:1080 не работает.
Proxy 35.185.196.38:3128 работает. Пинг: 454ms
Proxy 167.102.133.107:80 работает. Пинг: 367ms
Proxy 20.3.145.1:3128 не работает.
Proxy 159.54.149.67:80 не работает.
Proxy 198.74.51.79:8888 работает. Пинг: 442ms
Proxy 154.16.146.44:80 не работает.
Proxy 89.116.191.51:80 не работает.
Proxy 149.56.148.20:80 работает. Пинг: 401ms
Proxy 159.54.145.18:80 не работает.
Proxy 87.98.187.57:80 работает. Пинг: 353ms
Proxy 155.94.241.131:3128 работает. Пинг: 380ms
Proxy 149.202.91.219:80 не работает.
Proxy 47.251.28.148:8081 не работает.
Proxy 94.130.94.45:80 работает. Пинг: 355ms
Все прокси проверены. Рабочие прокси записаны в файл working_proxies.txt

проверка прокси идет через http://example.com по типу как bs4 проверяет обратный запрос.
