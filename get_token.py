
from urllib import request, parse
import json
import webbrowser

print('renren status start, get token, please copy the url')

renren_key = '7f67c7eb78a5475da8c9b264ceec49a6'

auth_para_dict = dict()
auth_para_dict['client_id'] = renren_key
auth_para_dict['response_type'] = 'token'
auth_para_dict['redirect_uri'] = 'http://xctest.sinaapp.com/renren_oauth'
# auth_para_dict['display'] = 'mobile'
auth_para_dict['scope'] = 'status_update'

auth_para = parse.urlencode(auth_para_dict)
auth_url = 'https://graph.renren.com/oauth/authorize?' + auth_para
# print(auth_url)

webbrowser.open_new(auth_url)
