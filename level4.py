import urllib2 
import re
import locale
import request

request = request.RequestUrl()
headers = { 'User-Agent' :  'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:25.0) Gecko/20100101 Firefox/25.0',
            'Cookie' :  'd53db4de415c4e858dc761595623a898=+; Path=/\r\n',
            'Cookie' :  '18=+; Path=/\r\n',
            'Cookie' : 'cade-meu-cookie=esta+aqui; Path=/\r\n' }       
feeddata = request.open_url_and_get_content('http://hughes.sieve.com.br:8000/level4/')
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
pattern = r'R\$ ([\d\.,]+)'
match = re.search(pattern, site_status_3)
price = locale.atof(match.groups()[0])
print 'R$ %f' % price 
