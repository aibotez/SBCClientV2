import os,requests,json,base64

class SBCRe():
    def __init__(self):
        self.Cookie = ''
        self.headers = ''
        self.CurFileList = []
        self.host = 'pi.sbc.plus:800'
        self.host = '127.0.0.1:90'
        self.host = '10.147.17.148:90'
        self.UserEmail = '2290227486@qq.com'
        self.UserPassword = '12'
        self.GetSBCCookie()
        self.PublicHeaders()


    def PublicHeaders(self):
        headers = {
            # 'Content-Type': 'application/json; charset=UTF-8',
            'Cookie':self.Cookie
        }
        self.headers = headers

    def GetSBCCookie(self):
        url = 'http://'+self.host+'/loginVerify/'
        data = {
            'useremail': '2290227486@qq.com',
            'userpassword': '12',
        }
        res = requests.post(url, data=data, allow_redirects=False)
        cookies = res.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        if 'coks' in cookie:
            self.Cookie = 'coks='+cookie['coks']
    def CheckRoFile(self,info):
        url = 'http://' + self.host + '/CheckFile/'
        data = info
        res = requests.post(url, data=data,headers=self.headers)
        # print(json.loads(res.text))
        # FileDatas = json.loads(res.text)
        return json.loads(res.text)

    def GetSBCShareFile1(self,data):
        url = 'http://' + self.host + '/GetSBCShareFile/'
        res = requests.get(url, params=data,headers=self.headers)
        return json.loads(res.text)
    def GetSBCShareFile0(self,url,check=None):
        data = {
            'client':'windows',
            'check':check,
        }
        res = requests.get(url, params=data,headers=self.headers)
        return json.loads(res.text)
    def SBCFileCopy(self,info):
        url = 'http://' + self.host + '/netOper/'
        data = json.dumps(info)
        res = requests.post(url, data=data,headers=self.headers)
        return res.text
    def SBCFileMove(self,info):
        url = 'http://' + self.host + '/netOper/'
        data = json.dumps(info)
        res = requests.post(url, data=data,headers=self.headers)
        return res.text
    def SBCFileInfos(self,info):
        # print(path)
        url = 'http://' + self.host + '/GetFilePorper/'
        data = json.dumps(info)
        res = requests.post(url, data=data,headers=self.headers)
        return json.loads(res.text)
    def SBCShare(self,info):
        # print(path)
        url = 'http://' + self.host + '/CreatShareFile/'
        data = json.dumps(info)
        res = requests.post(url, data=data,headers=self.headers)
        return json.loads(res.text)
    def NewFolder(self,info):
        # print(path)
        url = 'http://' + self.host + '/netOper/'
        data = {
            'netOper': 'NewFilder',
            'CurPath':info['CurPath'],
            'NewFolderName':info['NewFolderName'],
        }
        res = requests.post(url, data=data,headers=self.headers)
    def ReName(self,info):
        # print(path)
        url = 'http://' + self.host + '/ReName/'
        data = {
            'NewName': info['NewName'],
            'OldNamePath':info['fepath'],
        }
        res = requests.post(url, data=data,headers=self.headers)
    def GetRoFileMd5(self,path):
        # print(path)
        url = 'http://' + self.host + '/GetFileMd5/'
        data = {
            'path': path,
        }
        res = requests.post(url, data=data,headers=self.headers)
        # print(json.loads(res.text))

        # FileDatas = json.loads(res.text)
        return json.loads(res.text)
    def GetAllFilesfromFolder(self,path):
        url = 'http://' + self.host + '/GetAllFilesfromFolder/'
        data = {
            'path': path,
        }
        # print(self.headers)
        res = requests.post(url, data=data,headers=self.headers)
        # print(res)
        FileDatas = json.loads(res.text)
        return FileDatas
    def GetFileList(self,path):
        url = 'http://' + self.host + '/GetFileListbyClient/'
        data = {
            'path': path,
        }
        # print(self.headers)
        res = requests.post(url, data=data,headers=self.headers)
        # print(res)
        FileDatas = json.loads(res.text)
        # print(FileDatas['FileList'])
        # for i in FileDatas['FileList']:
        #     print(i)
        self.CurFileList = FileDatas['FileList']
        self.Nav = FileDatas['Nav']
        self.imgFiles = FileDatas['imgFiles']
        return FileDatas['FileList']

    def DelFile(self,fileinfo):
        url = 'http://' + self.host + '/DelFiles/'
        fileinfo['client'] = 'Windows'
        print(fileinfo)
        res = requests.post(url, data=json.dumps(fileinfo),headers=self.headers)

    def GetFileCon(self,Files):
        url = 'http://' + self.host + '/GetImgCon/'
        postdata = json.dumps(Files,ensure_ascii=False)
        postdata = base64.encodebytes(postdata.encode('utf8')).decode()
        data = {
            'imgdata': postdata,
        }
        # print(data)
        res = requests.post(url, data=json.dumps(data),headers=self.headers)
        Datas = json.loads(res.text)
        # print(Datas)
        return Datas

    def size_format(self,size):
        if size < 1024:
            return '%i' % size + 'size'
        elif 1024 <= size < 1024 * 1024:
            return '%.1f' % float(size / 1024) + 'KB'
        elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
            return '%.1f' % float(size / (1024 * 1024)) + 'MB'
        elif 1024 * 1024 * 1024 <= size < 1024 * 1024 * 1024 * 1024:
            return '%.1f' % float(size / (1024 * 1024 * 1024)) + 'GB'
        elif 1024 * 1024 * 1024 * 1024 <= size:
            return '%.1f' % float(size / (1024 * 1024 * 1024 * 1024)) + 'TB'

    def SearchFile(self,SearchContent,SearchFileType):
        url = 'http://' + self.host + '/SearchFile/'
        data = {
            'SearchContent':SearchContent,
            'SearchFileType':SearchFileType
        }
        res = requests.post(url, data=json.dumps(data),headers=self.headers)
        Datas = json.loads(res.text)['data']
        Datas = json.loads(Datas)

        feinfos = []
        FileMd5List = []
        for i in Datas:
            if i['fields']['FileMd5'] not in FileMd5List:
                feinfo = i['fields']
                feinfo['fetype'] = feinfo['FileType'].replace('image','img')
                feinfo['filelj'] = base64.encodebytes(feinfo['FilePath'].encode('utf8')).decode().replace('\n','')
                feinfo['filename'] = feinfo['FilePath'].split('/')[-1]
                feinfo['big'] =self.size_format(int(feinfo['FileSize']))
                feinfo['date'] = feinfo['FileModTime']
                feinfos.append(feinfo)
                FileMd5List.append(feinfo['FileMd5'])
            # print(feinfo)
        self.CurFileList = feinfos
        # return feinfos

    def getImgdata(self,path):
        url = 'http://' + self.host + '/preview/'
        data = {
            'filepath':path,
            'client':'windows'
        }
        res = requests.post(url, data=json.dumps(data),headers=self.headers)
        # print(res)
        return res.content


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
# SBCRe.SearchFile()


# SBCRe.GetFileList('/home/')
#
# data = {'imgdata': [{'fepath': '/home/11520C02B909A8A0B1D38A97BA96BA37.jpg'}, {'fepath': '/home/2C12CADA76FA80A522E17D558EAEB087.jpg'}, {'fepath': '/home/6D6DFF40203E909FF609672806FB1514.jpg'}, {'fepath': '/home/8e8a308ec508de6ec9dd73d49e4e0114.jpg'}, {'fepath': '/home/catgif.gif'}, {'fepath': '/home/excelcon.jpg'}, {'fepath': '/home/photo@6.jpg'}, {'fepath': '/home/revie1.png'}, {'fepath': '/home/Screenshot_2.022-02-25-13-52-11-93_3915bacb9306346f.jpg'}, {'fepath': '/home/Screenshot_2022-02-215-17-33-50-25_621daa935a4f457ca20c08298cc203d1.jpg'}, {'fepath': '/home/Screenshot_2022-02-25-13-52-11-93_3915bacb930634b7e206116f9dc9486f.jpg'}, {'fepath': '/home/Screenshot_2022-03-02-17-08-28-45_5b9ffa3eca6ceb7886a201532a778ee7.jpg'}, {'fepath': '/home/wx_camera_1646192764477.jpg'}, {'fepath': '/home/wx_camera_1646713330890.jpg'}, {'fepath': '/home/微信图片_20220307214129.jpg'}]}
# # SBCRe.GetFileCon(data)
#
# # data = 'dds计'
# print(str(data).encode('utf-8'))
