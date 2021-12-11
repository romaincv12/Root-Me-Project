import urllib2, re
import urllib, os, subprocess, time, base64

opener = urllib2.build_opener()
continue_loop = True
while True:
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0')]
    opener.addheaders.append(('Cookie', 'challenge_frame=1; spip_session=myspip_session; PHPSESSID=myPHPSESSID'))
    opener.addheaders.append(('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'))
    opener.addheaders.append(('Accept-Language', 'en-US,en;q=0.5'))
    opener.addheaders.append(('Accept-Encoding', 'gzip, deflate'))
    opener.addheaders.append(('DNT', '1'))
    opener.addheaders.append(('Connection', 'Keep-Alive'))
    response = opener.open('http://challenge01.root-me.org/programmation/ch8/ch8.php?frame=1','')
    html = response.read()
    regex = r'data:image/png;base64,(.*)" /><br><br>'
    result = re.search(regex, html)
    result = result.group(1)
    result = base64.b64decode(result)
    file_handle = open('captcha.png', 'wb')
    file_handle.write(result)
    file_handle.close

    file_handle = open('captcha.png', 'rb')
    result = subprocess.Popen(['gocr -i captcha.png'], shell=True, stdout=subprocess.PIPE).communicate()[0]
    file_handle.close
    print result
    result = result.replace('\n', '')
    result = result.replace(' ', '')
    result = result.replace(',', '')
    result = result.replace('\'', '')
    print result

    values = {'cametu':result}
    post_data = urllib.urlencode(values)
    opener.addheaders.append(('Referer', 'http://challenge01.root-me.org/programmation/ch8/ch8.php?frame=1'))
    response = opener.open('http://challenge01.root-me.org//programmation/ch8/ch8.php?frame=1', post_data)
    file_handle = open('result.html', 'w')
    while 1:
        data = response.read()
        if not('Failed' in data) and data:
            continue_loop = False
        if not data:
            break
        file_handle.write(data)
    file_handle.close
    if continue_loop == False:
        break
