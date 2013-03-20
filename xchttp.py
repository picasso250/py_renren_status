
import urllib.request

print('renren status start')



renren_key = '7f67c7eb78a5475da8c9b264ceec49a6'

auth_para_dict = dict()
auth_para_dict['client_id'] = renren_key
auth_para_dict['response_type'] = 'token'
auth_para_dict['redirect_uri'] = 'http://graph.renren.com/oauth/login_success.html'
auth_para_dict['display'] = 'mobile'
auth_para_dict['scope'] = 'status_update'

auth_para = '&'.join(["%s=%s" % (k, v) for k, v in auth_para_dict.items()])

authUrl = 'https://graph.renren.com/oauth/authorize?' + auth_para

print(authUrl)

req = urllib.request

if 0:
    r = urllib.request.urlopen('http://www.baidu.com')
    html = r.read()
    print(html);

# http://shell.renren.com/228417767/status
# content=test&hostid=228417767&requestToken=-2031837365&_rtk=52a59da5&channel=renren
# http://code.jquery.com/jquery-1.9.1.min.js
