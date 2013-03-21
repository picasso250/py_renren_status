
from urllib import request, parse
import json
import webbrowser

print('renren status start')

status = 'test3'

ret_url = 'http://xctest.sinaapp.com/renren_oauth#access_token=171902%7C6.e337de58f8715af0b7738ed90876a4d9.2592000.1366473600-228417767&expires_in=2595103&scope=status_update'
ret_kvs = ret_url.split('#')[1].split('&')
ret_dict = dict();
for kv in ret_kvs:
    k,v = kv.split('=')
    ret_dict[k] = v
# print(ret_dict)

access_token = parse.unquote(ret_dict['access_token']) # 因为我们一会儿还要urlencode，所以要先unquote
# print(access_token)
# print(parse.unquote(access_token))


arg_dict = dict()
arg_dict['v'] = '1.0'
arg_dict['access_token'] = access_token
arg_dict['format'] = 'json'

arg_dict['method'] = 'status.set'
arg_dict['status'] = status

# print(parse.urlencode(arg_dict));

api_base_url = 'https://api.renren.com/restserver.do'

req = request.urlopen(api_base_url, parse.urlencode(arg_dict).encode('utf8'))
json_str = req.read().decode('utf8')
json_arr = json.loads(json_str)

if json_arr['result']:
    print('ok')
else:
    print('Error')
