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

Proxy 155.94.241.130:3128 работает. Пинг: 377ms

Все прокси проверены. Рабочие прокси записаны в файл working_proxies.txt

проверка прокси идет через http://example.com по типу как bs4 проверяет обратный запрос.
