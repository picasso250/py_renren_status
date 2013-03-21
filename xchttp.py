import urllib.urlencode
import urllib.request
import webbrowser

print('renren status start')

def build_str(_dict):
    return '&'.join(["%s=%s" % (k, v) for k, v in _dict.items()])


renren_key = '7f67c7eb78a5475da8c9b264ceec49a6'

auth_para_dict = dict()
auth_para_dict['client_id'] = renren_key
auth_para_dict['response_type'] = 'token'
auth_para_dict['redirect_uri'] = 'http://graph.renren.com/oauth/login_success.html'
auth_para_dict['display'] = 'mobile'
auth_para_dict['scope'] = 'status_update'

ps = urllib.urlencode(auth_para_dict)
print(ps)

auth_para = '&'.join(["%s=%s" % (k, v) for k, v in auth_para_dict.items()])

auth_url = 'https://graph.renren.com/oauth/authorize?' + auth_para

# print(auth_url)

# webbrowser.open_new(auth_url)

req = urllib.request

r = req.urlopen(auth_url)
html = r.read()
print(html)

if 0:
    r = urllib.request.urlopen('http://www.baidu.com')
    html = r.read()
    print(html);

# http://shell.renren.com/228417767/status
# content=test&hostid=228417767&requestToken=-2031837365&_rtk=52a59da5&channel=renren
# http://code.jquery.com/jquery-1.9.1.min.js







ret_url = 'http://graph.renren.com/oauth/login_success.html#access_token=171902%7C6.68cf462ec3151fdc24b60f9646f21e12.2592000.1366437600-228417767&expires_in=2592243&scope=status_update'
ret_kvs = ret_url.split('#')[1].split('&')
ret_dict = dict();
for kv in ret_kvs:
    kv_arr = kv.split('=')
    ret_dict[kv_arr[0]] = kv_arr[1]
# print(ret_dict)

access_token = ret_dict['access_token']
arg_dict = dict()
arg_dict['v'] = '1.0'
arg_dict['access_token'] = access_token
arg_dict['format'] = 'json'
arg_dict['call_id'] = '1.0'

# arg_dict['']

