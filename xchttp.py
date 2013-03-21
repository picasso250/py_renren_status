
from urllib import request, parse
import json
import webbrowser

print('renren status start')

renren_key = '7f67c7eb78a5475da8c9b264ceec49a6'

auth_para_dict = dict()
auth_para_dict['client_id'] = renren_key
auth_para_dict['response_type'] = 'token'
auth_para_dict['redirect_uri'] = 'http://graph.renren.com/oauth/login_success.html'
auth_para_dict['display'] = 'mobile'
auth_para_dict['scope'] = 'status_update'

ps = parse.urlencode(auth_para_dict)
# print(ps)

auth_para = '&'.join(["%s=%s" % (k, v) for k, v in auth_para_dict.items()])

auth_url = 'https://graph.renren.com/oauth/authorize?' + auth_para
# print(auth_url)

# webbrowser.open_new(auth_url)

# req = urllib.request

# r = req.urlopen(auth_url)
# html = r.read()
# print(html)

# r = request.urlopen('http://www.baidu.com')
# html = r.read()
# print(html);

# http://shell.renren.com/228417767/status
# content=test&hostid=228417767&requestToken=-2031837365&_rtk=52a59da5&channel=renren
# http://code.jquery.com/jquery-1.9.1.min.js


ret_url = 'http://graph.renren.com/oauth/login_success.html#access_token=171902%7C6.68cf462ec3151fdc24b60f9646f21e12.2592000.1366437600-228417767&expires_in=2592243&scope=status_update'
ret_kvs = ret_url.split('#')[1].split('&')
ret_dict = dict();
for kv in ret_kvs:
    k,v = kv.split('=')
    ret_dict[k] = v
# print(ret_dict)

access_token = ret_dict['access_token']
arg_dict = dict()
arg_dict['v'] = '1.0'
arg_dict['access_token'] = access_token
arg_dict['format'] = 'json'

arg_dict['method'] = 'status.set'
arg_dict['status'] = 'test2'

# print(arg_dict);

api_base_url = 'https://api.renren.com/restserver.do'

url = api_base_url + parse.urlencode(arg_dict)
# print(url)

req = request.urlopen(api_base_url, parse.urlencode(arg_dict).encode('utf8'))
json_str = req.read().decode('utf8')
json_arr = json.loads(json_str)

print(json_arr)

