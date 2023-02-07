
import mimetypes
import filetype

class FileType():
    def __init__(self):
        pass
    def GetFileType(self,fepath):
        fetypes = mimetypes.guess_type(fepath)
        fetype = 'others'
        try:
            Types = fetypes[0].split('/')
            # print(Types,fepath)
            if Types[0] == 'image':
                fetype = ['image',Types[1]]
                return fetype
            if Types[0] == 'video':
                fetype = ['video',Types[1]]
                return fetype
            if Types[1] == 'pdf':
                fetype = ['pdf','']
                return fetype
            if 'officedocument.wordprocessingml.document' in Types[1]:
                fetype = ['word','']
                return fetype
            if 'officedocument.presentationml.presentation' in Types[1]:
                fetype = ['ppt','']
                return fetype
            if 'officedocument.spreadsheetml.sheet' in Types[1]:
                fetype = ['excel','']
                return fetype
            if 'compressed' in Types[1] or 'tar' in Types[1]:
                fetype = ['zip','']
                return fetype
            if 'html' in Types[1]:
                fetype = ['html','']
                return fetype
            if 'x-msdownload' in Types[1]:
                fetype = ['exe','']
                return fetype
        except:
            pass

        try:
            kind = filetype.guess(fepath)
            if 'compressed' in kind.mime:
                fetype = ['zip','']
                return fetype
        except:
            pass
        return fetype

    def FileType(self,fepath):
        try:
            fetype = self.GetFileType(fepath)
            # fetype = fetypes[0].split('/')[0]
            if fetype[0] == 'image':
                path = '/static/img/filecon/imgcon.jpg'
                return [path, 'img']
                # imgtype = fetype[1]
                # return GetImgconBase64(fepath,imgtype)
            if fetype[0] == 'pdf':
                path = '/static/img/filecon/pdfcon.jpg'
                return [path, 'pdf']
            if fetype[0] == 'word':
                path = '/static/img/filecon/wordcon.jpg'
                return [path, 'word']
            if fetype[0] == 'ppt':
                path = '/static/img/filecon/pptcon.jpg'
                return [path, 'ppt']
            if fetype[0] == 'excel':
                path = '/static/img/filecon/excelcon.jpg'
                return [path, 'excel']
            if fetype[0] == 'zip':
                path = '/static/img/filecon/zipcon.png'
                return [path, 'zip']
            if fetype[0] == 'html':
                path = '/static/img/filecon/htmlcon.jpg'
                return [path, 'html']
            if fetype[0] == 'exe':
                path = '/static/img/filecon/execon.jpg'
                return [path, 'exe']
        except Exception as e:
            print(e)
        return ['/static/img/wj.jfif', 'other']