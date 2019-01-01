import urllib.request as url
flag = ''
while 1:
    res = url.urlopen('http://amkr.co.nf/file_to_read.html')
    data = res.read().decode('utf-8')
    if not data == flag:
        print(data)
        flag = data
        