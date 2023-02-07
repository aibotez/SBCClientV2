import os,json


class Load_Trans_Info():
    def __init__(self):
        self.DowningDocu = 'Downing.txt'

    def Load_Downing(self):
        pass
    def Load_Uping(self):
        pass
    def Load_CrossNet(self):
        pass
    def Finish(self):
        pass

class Update_Trans_Info():
    def __init__(self):
        self.DowningDocu = 'Downing.txt'
    def Update_Downing(self,**kwargs):#feinfo,Dowinfo,Oper
        if kwargs['Oper'] == 'add':
            feinfo = kwargs['feinfo']
            fename = feinfo['fename']
            fepath = feinfo['fepath']
            fetype = feinfo['fetype']
            fepath_base64 = feinfo['fepath_base64']
            Dowinfo = kwargs['Dowinfo']
            NetSource = Dowinfo['Source']
            DownPath = Dowinfo['DownPath']
            Tran_Dowing_Info = {}
            Tran_Dowing_Info[fepath_base64] = {
                'fename':fename,
                'fepath':fepath,
                'fetype':fetype,
                'NetSource':NetSource,
                'DownPath':DownPath
            }
            try:
                if not os.path.exists(self.DowningDocu):
                    os.mknod(self.DowningDocu)
                with open(self.DowningDocu, 'a', encoding='utf-8') as f:
                    f.write(json.dumps(Tran_Dowing_Info, ensure_ascii=False))
                return Tran_Dowing_Info
            except:
                return 0
        else:
            pass


# Update_Trans = Update_Trans_Info()
# Update_Trans.Update_Downing()



