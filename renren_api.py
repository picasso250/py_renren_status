
from urllib import request, parse
import json

def get_auth_url():
    renren_key = '7f67c7eb78a5475da8c9b264ceec49a6'

    auth_para_dict = dict()
    auth_para_dict['client_id'] = renren_key
    auth_para_dict['response_type'] = 'token'
    auth_para_dict['redirect_uri'] = 'http://xctest.sinaapp.com/renren_oauth'
    auth_para_dict['scope'] = 'status_update'

    auth_para = parse.urlencode(auth_para_dict)
    auth_url = 'https://graph.renren.com/oauth/authorize?' + auth_para
    return auth_url

def parse_token(ret_url):
    ret_dict = dict();
    for kv in ret_url.split('#')[1].split('&'):
        k,v = kv.split('=')
        ret_dict[k] = parse.unquote(v) # 因为我们一会儿还要urlencode，所以要先unquote
    return ret_dict

def update_status(access_token, status):
    arg_dict = dict()
    arg_dict['v'] = '1.0'
    arg_dict['access_token'] = access_token
    arg_dict['format'] = 'json'

    arg_dict['method'] = 'status.set'
    arg_dict['status'] = status

    api_base_url = 'https://api.renren.com/restserver.do'

    req = request.urlopen(api_base_url, parse.urlencode(arg_dict).encode('utf8'))
    json_str = req.read().decode('utf8')
    json_arr = json.loads(json_str)

    return json_arr['result']

if __name__ == '__main__':
    print('test get_auth_url')
    auth_url = get_auth_url()
    print(auth_url)

    print('test parse_token')
    token = parse_token('http://xctest.sinaapp.com/renren_oauth#access_token=171902%7C6.e337de58f8715af0b7738ed90876a4d9.2592000.1366473600-228417767&expires_in=2595103&scope=status_update')
    print(token)

    print('test update_status')
    r = update_status(token['access_token'], '测试发布状态')
    if r:
        print('ok')
    else:
        print('Error')