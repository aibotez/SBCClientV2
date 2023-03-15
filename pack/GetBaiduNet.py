
import requests,os,time,json


class GetBaiduNet():
    def __init__(self,ui):
        self.ui = ui

    def BaiduNetUserExistCheck(self):
        url = 'http://'+self.ui.host+'/BaiduNetUserExistCheck/'
        res = requests.post(url,headers=self.ui.SBCRe.headers).text
        try:
            res = json.loads(res)
            print(res)
            if res['errno'] == '0':
                return res['cookie']
            return 0
        except:
            pass
        return 0

    def GetUserinfo(self):
        BaiduNetUserCookie = self.BaiduNetUserExistCheck()
        if not BaiduNetUserCookie:
            return 0
        url = 'http://' + self.ui.host + '/GetBaiduNetUserInfo/'
        res = requests.post(url, headers=self.ui.SBCRe.headers).text
        print(res)
        # self.getFilesFromPath('/')

    def getFilesFromPath(self,path):
        url = 'http://' + self.ui.host + '/GetBaiduNetFiles/'
        data={
            'showpath':path
        }
        res = requests.post(url, data=data,headers=self.ui.SBCRe.headers).text
        res = json.loads(res)

        filelist = []
        for i in res['list']:
            file = {}
            file = i
            file['fename'] = i['server_filename']
            file['big'] = i['size']
            file['date'] = i['server_mtime']
            file['filename'] = i['server_filename']
            filelist.append(file)
        print(res['navlist'])
        print(res['navlastpath'])
        for i in res['list']:
            print(i)
        return {'navlist':res['navlist'],'navlastpath':res['navlastpath'],'Filelist':filelist}
