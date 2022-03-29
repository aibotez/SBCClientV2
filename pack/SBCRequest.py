import os,requests,json

class SBCRe():
    def __init__(self):
        self.Cookie = ''
        self.headers = ''
        self.CurFileList = []
        self.host = 'pi.sbc.plus:800'
        self.UserEmail = '2290227486@qq.com'
        self.UserPassword = '123'
        self.GetSBCCookie()
        self.PublicHeaders()


    def PublicHeaders(self):
        headers = {
            'Cookie':self.Cookie
        }
        self.headers = headers

    def GetSBCCookie(self):
        url = 'http://'+self.host+'/loginVerify/'
        data = {
            'useremail': '2290227486@qq.com',
            'userpassword': '123',
        }
        res = requests.post(url, data=data, allow_redirects=False)
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        if 'coks' in cookie:
            self.Cookie = 'coks='+cookie['coks']
    def GetFileList(self,path):
        url = 'http://' + self.host + '/GetFileListbyClient/'
        data = {
            'path': path,
        }
        res = requests.post(url, data=data,headers=self.headers)
        FileDatas = json.loads(res.text)
        # print(FileDatas['FileList'])
        # for i in FileDatas['FileList']:
        #     print(i)
        self.CurFileList = FileDatas['FileList']

# def Login():
#     url = 'http://pi.sbc.plus:800/loginVerify/'
#
#     data = {
#         'useremail':'2290227486@qq.com',
#         'userpassword':'123',
#     }
#
#     res = requests.post(url,data=data,allow_redirects=False)
#     # res = requests.get(res.url)
#     cookies = res.cookies
#     cookie = requests.utils.dict_from_cookiejar(cookies)
#     print(cookie)
# SBCRe = SBCRe()
# SBCRe.GetFileList('/home/')