
import requests,os,time,json
from urllib.parse import quote,unquote
import time,requests,json,base64,re



class baidunet():
    def __init__(self,cookie):
        cookie = cookie.replace(' ','')
        self.cookies = cookie
        self.headers = ''
        self.PulublicHearders()

        self.ShareId =''
        self.ShareUk = ''
        self.FsId = ''
        self.timestamp = ''
        self.bdclnd = ''

    def DealCookie(self,cook):
        cook = cook.replace(' ','')
        cookie = ''
        coks = cook.split(';')
        for i in coks:
            if 'BDUSS' in i or 'STOKEN' in i:
                cookie = cookie + i + ';'
        return cookie

    def PulublicHearders(self):
        self.headers = {
            # 'User-Agent' : 'netdisk;4.6.2.0;PC;PC-Windows;10.0.10240;WindowsBaiduYunGuanJia',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
            'Cookie':self.DealCookie(self.cookies),
            'Host': 'pan.baidu.com',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'same-site',
            'Sec-Fetch-Mode': 'navigate',
            'Referer': 'https://pan.baidu.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    def size_format(self,size):
        size = int(size)
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

    def FormTime(self,times):
        format = '%Y-%m-%d %H:%M'
        time_tuple = time.localtime(times)
        result = time.strftime(format, time_tuple)
        return result

    def GetFileType(self,fe):
        if fe['isdir'] == 1:
            return 'folder'
        fename = fe['server_filename']
        fetype = fename.split('.')

        if len(fetype) < 1:
            return 'other'
        fetype = fetype[-1].lower()
        imgtypre = ['bmp','jpg','png','tif','gif''pcx','tga','exif','fpx','svg','psd','cdr','pcd','dxf','ufo','eps','ai','raw','WMF','webp','avif','apng']
        if fetype in imgtypre:
            return 'img'
        if fetype == 'pdf':
            return 'pdf'
        if fetype == 'exe':
            return 'exe'
        if 'doc' in fetype:
            return 'word'
        if 'ppt' in fetype:
            return 'ppt'
        if 'xls' in fetype:
            return 'excel'
        if 'html' in fetype:
            return 'html'
        if fetype in ['7z','zip','rar','gz','tgz','bz']:
            return 'zip'
        return 'other'

    def GetConImg(self,fe):
        fetype = self.GetFileType(fe)
        if fetype == 'folder':
            return '/static/img/foldersm.png'
        if fetype == 'img':
            path = '/static/img/filecon/imgcon.jpg'
            return path
            # imgtype = fetype[1]
            # return GetImgconBase64(fepath,imgtype)
        if fetype == 'pdf':
            path = '/static/img/filecon/pdfcon.jpg'
            return path
        if fetype == 'word':
            path = '/static/img/filecon/wordcon.jpg'
            return path
        if fetype == 'ppt':
            path = '/static/img/filecon/pptcon.jpg'
            return path
        if fetype == 'exe':
            path = '/static/img/filecon/execon.jpg'
            return path
        if fetype == 'excel':
            path = '/static/img/filecon/excelcon.jpg'
            return path
        if fetype == 'zip':
            path = '/static/img/filecon/zipcon.png'
            return path
        if fetype == 'html':
            path = '/static/img/filecon/htmlcon.jpg'
            return path
        else:
            return '/static/img/wj.jfif'
    def GetBaiduNetUserInfo(self):
        url = 'https://pan.baidu.com/api/loginStatus?clienttype=0&app_id=250528&web=1'
        # print(self.headers)
        res = requests.get(url,headers=self.headers).text
        resdata = json.loads(res)
        username = ''
        photo_url = '/static/img/cat0.jpg'
        if resdata['errno'] ==0:
            username = resdata['login_info']['username']
            photo_url = resdata['login_info']['photo_url']
        url = 'https://pan.baidu.com/api/quota?clienttype=0&app_id=250528&web=1'
        res = requests.get(url,headers=self.headers).text
        resdata = json.loads(res)
        usertotal = ''
        userused = ''
        userprecent = 0
        if resdata['errno'] ==0:
            usertotal = self.size_format(resdata['total'])
            userused = self.size_format(resdata['used'])
            userprecent = resdata['used']/resdata['total']
        return {'username':username,'userused':userused+'/'+usertotal,'userprecent':userprecent,'photo_url':photo_url}
    def VerShare(self,link_url,pass_code=None):
        if pass_code:
            # 生成时间戳
            t_str = str(int(round(time.time() * 1000)))
            check_url = 'https://pan.baidu.com/share/verify?surl=' + link_url[25:48] + '&t=' + t_str + '&channel=chunlei&web=1&clienttype=0'
            post_data = {'pwd': pass_code, 'vcode': '', 'vcode_str': '', }
            response_post = requests.post(url=check_url, headers=self.headers, data=post_data, timeout=10,
                                   allow_redirects=False,
                                   verify=False)
            # 在cookie中加入bdclnd参数
            if response_post.json()['errno'] == 0:
                bdclnd = response_post.json()['randsk']
                self.bdclnd = bdclnd
            else:
                # print('VerifyError')
                return response_post.json()['errno']
            if bool(re.search('BDCLND=', self.headers['Cookie'], re.IGNORECASE)):
                self.headers['Cookie'] = re.sub(r'BDCLND=(\S+?);', r'BDCLND=' + bdclnd + ';',
                                                  self.headers['Cookie'])
            else:
                self.headers['Cookie'] += '; BDCLND=' + bdclnd
    def GetShareInfo0(self,url,pass_code=None):
        self.VerShare(url.replace('?from=init',''),pass_code)
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        res = res.text
        # timestamp=re.findall(r'timestamp=(.*?)&', res)[0]
        # fid=re.findall(r'fid=(.*?)&', res)[0]
        fs_id_list = re.findall('"fs_id":(\\d+?),"', res)
        # sign = re.findall(r'sign=(.*?)&', res)[0]
        # sign = unquote(sign)
        # path = re.findall(r'object=(.*?)&', res)[0]
        shareid = re.findall('"shareid":(\\d+?),"', res)[0]
        shareuk = re.findall('"share_uk":"(\\d+?)","', res)[0]
        bdstoken = re.findall(r'"bdstoken":"(.*?)","', res)[0]
        # m = re.search('\"sign\":\"(.+?)\"', res)
        # print(timestamp,fid,sign,shareid,shareuk,path)
        return {'shareid':shareid,'shareuk':shareuk,'fsid':fs_id_list,'bdstoken':bdstoken}
    def SaveShare(self,Shareurl,SavePath,pass_code=None):
        shareInfo = self.GetShareInfo0(Shareurl,pass_code)
        url = 'https://pan.baidu.com/share/transfer'
        payload = {
            'shareid':shareInfo['shareid'],
            'from':shareInfo['shareuk'],
            'sekey':unquote(self.bdclnd),
            'channel': 'chunlei',
            'web': '1',
            'app_id': '250528',
            'bdstoken': shareInfo['bdstoken'],
            'clienttype': '0',
            # 'logid':'Njg0NzdGNEFFRjEzNUVGRjY1MkQxMzZGN0U5N0VFODU6Rkc9MQ==',
        }
        data = {
            'fsidlist':'[{}]'.format(shareInfo['fsid'][0]),
            'path': '{}'.format(SavePath)
        }
        res = requests.post(url, headers=self.headers, params=payload, data=data)
    def GetFileList(self,path):
        urlSer = 'https://pan.baidu.com/api/list?&dir={}'.format(quote(path))
        # print(self.cookies)
        headers = {
            'Cookie':self.cookies,
            'Host': 'pan.baidu.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        }
        res = requests.get(urlSer,headers=headers).text
        resdata = json.loads(res)
        if resdata['errno'] ==0:
            for i in range(len(resdata['list'])):
                filepath = base64.encodebytes(resdata['list'][i]['path'].encode('utf8')).decode()
                filepath = filepath.replace('\n', '')
                resdata['list'][i]['filelj'] = filepath
                resdata['list'][i]['imgpath'] = self.GetConImg(resdata['list'][i])
                resdata['list'][i]['size'] = self.size_format(resdata['list'][i]['size'])
                resdata['list'][i]['Size'] = resdata['list'][i]['size']
                resdata['list'][i]['fetype'] = self.GetFileType(resdata['list'][i])
                resdata['list'][i]['server_mtime'] = self.FormTime(resdata['list'][i]['server_mtime'])
                if resdata['list'][i]['isdir'] == 1:
                    resdata['list'][i]['size'] = '--'
        return resdata

    def GetDownLink(self,path):
        # print(self.DealCookie(self.cookies))
        heardes ={
            'User-Agent':'netdisk;P2SP;3.0.0.127',
            'Cookie':self.DealCookie(self.cookies),
            # 'Cookie':'BDUSS=WlEMzN1T25sRTgybnFaflJkUjVuOEc2VUZNc2c3TGtiLWVhME0zQ3Z6Qk12c0ZoSVFBQUFBJCQAAAAAAAAAAAEAAACnqKsdZGxvZWNxaTQyMjM0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEwxmmFMMZphW;STOKEN=c5816c3b29a51273a34621968b5b96fe55b8dca9381014d2ce64789e28419409;STOKEN=c5816c3b29a51273a34621968b5b96fe55b8dca9381014d2ce64789e28419409',
            'Host': 'd.pcs.baidu.com'
        }
        payload = {
            # 'sign': self.sign,
            'app_id': '250528',
            'method': 'locatedownload',
            'check_blue': '1',
            'es': '1',
            'esl': '1',
            'path':path,
            'ver':'4.0',
            'dtype':'1',
            'err_ver':'1.0',
            'ehps' : '1',
            'eck' : '1',
            'vip':'0',
            'open_pflag':'0',
            'dpkg':'1',
            'sd':'0',
            'clienttype':'9',
            'version':'3.0.0.127',
            # 'time':'1647091729',
            # 'rand':'7d67077c7a5d4ba9ba1004ec26c18c41d596ec6f',
            # 'devuid':'BDIMXV2-O_91B0C68690D247B58683966534818267-C_0-D_33534c59584e4b30354135333037205420202020-M_68F7283616CD-V_50A68A1D',
            'channel':'0',
            'version_app':'7.12.1.1',

        }
        url = 'https://d.pcs.baidu.com/rest/2.0/pcs/file'
        # url = 'https://d.pcs.baidu.com/rest/2.0/pcs/file?app_id=250528&method=locatedownload&check_blue=1&es=1&esl=1&path=%2Ftest%2F5K.mat&ver=4.0&dtype=1&err_ver=1.0&ehps=1&eck=1&vip=0&open_pflag=0&dpkg=1&sd=0&clienttype=9&version=3.0.0.127&time=1647091729&rand=7d67077c7a5d4ba9ba1004ec26c18c41d596ec6f&devuid=BDIMXV2-O_91B0C68690D247B58683966534818267-C_0-D_33534c59584e4b30354135333037205420202020-M_68F7283616CD-V_50A68A1D&channel=0&version_app=7.12.1.1'
        res = requests.post(url,headers=heardes,params=payload).text
        # print(res)
        resdata= json.loads(res)
        # print(resdata)
        # print(resdata['urls'])
        DownLink = resdata['urls'][0]['url']
        return DownLink

class GetBaiduNet():
    def __init__(self,ui):
        self.ui = ui
        self.cookie = None
        self.BaiduNetUserExistCheck()

    def BaiduNetUserExistCheck(self):
        url = 'http://'+self.ui.host+'/BaiduNetUserExistCheck/'
        res = requests.post(url,headers=self.ui.SBCRe.headers).text
        try:
            res = json.loads(res)
            # print(res)
            if res['errno'] == '0':
                self.cookie = res['cookie']
                return res['cookie']
            return 0
        except:
            pass
        return 0

    def GetUserinfo(self):
        BaiduNetUserCookie = self.BaiduNetUserExistCheck()
        if not BaiduNetUserCookie:
            return 0
        bdnOp = baidunet(self.cookie)
        UserInfo = bdnOp.GetBaiduNetUserInfo()
        return UserInfo

        # url = 'http://' + self.ui.host + '/GetBaiduNetUserInfo/'
        # res = requests.post(url, headers=self.ui.SBCRe.headers).text
        # print(res)
        # self.getFilesFromPath('/')

    def GetNavpath(self,path):
        navpath = 'home' + path
        navpathlist = navpath.split('/')
        navpaths = []
        s = ''
        for i in navpathlist:
            s = s + i + '/'
            s = s.replace('home', '')
            Npath = base64.encodebytes(s.encode('utf8')).decode()
            Npath = Npath.replace('\n', '')
            navpaths.append({'navname': i, 'path': s, 'pathId': Npath})
        return navpaths
    def getFilesFromPath(self,path):

        bdnOp = baidunet(self.cookie)
        bdn = bdnOp.GetFileList(path)
        data = bdn['list']
        navlist = self.GetNavpath(path)
        navlastpath = navlist[-1]['path']
        filelist = []
        for i in data:
            file = i
            file['fename'] = i['server_filename']
            file['big'] = i['size']
            file['date'] = i['server_mtime']
            file['filename'] = i['server_filename']
            filelist.append(file)
        return {'navlist':navlist,'navlastpath':navlastpath,'Filelist':filelist}


        # url = 'http://' + self.ui.host + '/GetBaiduNetFiles/'
        # data={
        #     'showpath':path
        # }
        # res = requests.post(url, data=data,headers=self.ui.SBCRe.headers).text
        # res = json.loads(res)
        #
        # filelist = []
        # for i in res['list']:
        #     file = {}
        #     file = i
        #     file['fename'] = i['server_filename']
        #     file['big'] = i['size']
        #     file['date'] = i['server_mtime']
        #     file['filename'] = i['server_filename']
        #     filelist.append(file)
        # # print(res['navlist'])
        # # print(res['navlastpath'])
        # # for i in res['list']:
        # #     print(i)
        # return {'navlist':res['navlist'],'navlastpath':res['navlastpath'],'Filelist':filelist}
