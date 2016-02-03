#Linux

##Mario
Коннектимся, смотрим файл в `forward/`.
`find . -type f` говорит, что файлов очень много.
Надеемся, что файл с флагом имеет другой размер.
Размер остальных -- 56 байт. Делаем


`find . -type f -size -56c`

и

`find . -type f -size +56c`

#Injections

##SQL1
`select * from users`

##SQL2
`' OR '1'='1`

##SQL3
`' OR '1'='1' -- `

(тут важно, что пробел на конце)

#HTTP

##Device checker
Нужно как-то подобрать заголовок User-Agent. Находим какой-нибудь список (например, http://useragentstring.com/pages/All/)
и с питоном (import requests (see http://docs.python-requests.org/en/latest/)) просто пробуем все.

Подойдет: Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110526 Firefox/6.0a1 Fennec/6.0a1

Ответ: USERAGENTISEASYTOFAKE

#Network2

##Hungary games
Заходим куда-нибудь типа http://www.gatherproxy.com/proxylistbycountry. Пишем скрипт, который перебирает 
просто по 1му прокси из страны (см `network2/hungry/a.py`. скрипт довольно убогий, TL просто на глаз подобран). 
Подойдет Венгрия.

Ответ: 5b89ab62c3786455c800073e96fb7040 

##IPv6
Разбор:

IPv6. До тех пор, пока вы подключены к IPv4, а сервер — к IPv6, вы не можете получить доступ к нему напрямую 
(читать «не можете отправить ему сетевой пакет»). Значит, либо нужно обрести компьютер с IPv6 (например, арендовать сервер), 
либо найти «посредника». Посредника можно реализовать либо с помощью 6to4 (https://ru.wikipedia.org/wiki/6to4), либо с 
помощью веб-прокси-в-IPv6 (да поможет нам гугл).

6to4 у меня так и не получилось настроить, а вот через это http://www.ipv6proxy.net/ можем посмотреть страничку. Там есть в
html `div` скрытый. В нем написан флаг.

##DNS
Берем какой-нибудь сервис типа http://viewdns.info/dnsrecord/?domain=secretzone.qctf.ru и просто смотрим запись dns для данного домена

Разбор:

DNS. Необходимо выполнить трансфер указанной зоны, мастер-NS-сервер это позволяет. Как выполнить трансфер? 
Ну даже не знааааю... (см. dig и nslookup)

Это можно сделать так: `dig -t AXFR secretzone.qctf.ru @root.secretzone.qctf.ru.`

Про `root.secretzone.qctf.ru.` мы узнаем через `dig -t ANY secretzone.qctf.ru`

##FTP
Разбор:

FTP. Фильтр «ftp-data» в ваершарке покажет TCP-соединения по протоколу FTP, в которых передавались 
данные (как вы помните, там есть управляющее соединение и соединения для данных). 
Остаётся лишь Follow TCP Stream и Save as.

#Network

##Netdump
Смотрим в wireshark'e. Видим, что ICMP. Последний байт каждого реквеста (или респонза) -- 1 буква ответа

##Get a password
Ответ: flag{bigdataisaproblemnotasolution}

Берем wireshark. Ищем строку passeword.

Видим, что она есть в запросе от .136 к .128 по протоколу `TELNET`

Сортируем все запросы и ищем ответы .128 к .136 по протоколу `TELNET`

Там их много. В каждом содержимое -- одна буква из флага
