
# from pyaudio import *
import wave
import os
import cv2

# def GetWav(path):
#     if os.path.exists(path+'.wav'):
#         os.remove(path+'.wav')
#     cmd = 'ffmpeg -i {} -f wav {}.wav'.format(path,os.path.basename(path))
#     os.system(cmd)
#
# path = 'test1.mp4'
# # GetWav(path)


class VideoFram():
    def __init__(self):
        pass

    def CreatWav(self,path):
        if os.path.exists(path + '.wav'):
            os.remove(path + '.wav')
        cmd = 'ffmpeg -i {} -f wav {}.wav'.format(path, os.path.basename(path))
        os.system(cmd)

    def GetVideoFrams(self,Videopath,framidexs):
        cap = cv2.VideoCapture(Videopath)
        # cap.set(cv2.CAP_PROP_POS_MSEC, timespan[0])
        cap.set(cv2.CAP_PROP_POS_FRAMES, framidexs[0])  # 设置帧数标记
        frams = []
        curidx = framidexs[0]
        while (cap.isOpened()):
            ret, im = cap.read()  # 获取图像
            if not ret:  # 如果获取失败，则结束
                print("exit")
                break
            frams.append(im)
            cv2.waitKey(1)
            curidx += 1
            if curidx > framidexs[1]:
                break
        return frams

    def GetAudioFrams(self,path,framidexs):
        wf = wave.open(path, 'rb')  # 打开WAV文件
        wf.readframes(framidexs[0])  # 读取第一帧数据
        data = wf.readframes(framidexs[1]-framidexs[0])
        return data
    def GetVideoInfo(self,Videopath,Audiopath):
        # 3 CV_CAP_PROP_FRAME_WIDTH  # 视频帧宽度
        # 4 CV_CAP_PROP_FRAME_HEIGHT  # 视频帧高度
        cap = cv2.VideoCapture(Videopath)
        VideoFramsTotal = cap.get(7)
        VideoFramRate = cap.get(5)
        wf = wave.open(Audiopath, 'rb')  # 打开WAV文件
        AuduoFramsRate = wf.getnframes()
        AudioFramRate = wf.getframerate()
        return {'VideoFramsTotal':VideoFramsTotal,'VideoFramRate':VideoFramRate,'AuduoFramsRate':AuduoFramsRate,'AudioFramRate':AudioFramRate}


# def getVideo(path):
#     cap=cv2.VideoCapture(path)
#     frames_num = cap.get(7)
#     print(frames_num,cap.get(5))
#
# def play(path):
#     # 用文本文件记录wave模块解码每一帧所产生的内容。注意这里不是保存为二进制文件
#     # dump_buff_file = open(r"Ring01.dup", 'w')
#
#     chunk = 1  # 指定WAV文件的大小
#     wf = wave.open(path, 'rb')  # 打开WAV文件
#     p = PyAudio()  # 初始化PyAudio模块
#
#     # 打开一个数据流对象，解码而成的帧将直接通过它播放出来，我们就能听到声音啦
#     stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
#                     rate=wf.getframerate(), output=True)
#     print(wf.getnframes())
#     print(wf.getsampwidth(),wf.getframerate())
#     wf.readframes(wf.getnframes()-100)  # 读取第一帧数据
#     # print(data)  # 以文本形式打印出第一帧数据，实际上是转义之后的十六进制字符串
#     data = wf.readframes(chunk)
#     # 播放音频，并使用while循环继续读取并播放后面的帧数
#     # 结束的标志为wave模块读到了空的帧
#     while data != b'':
#
#         stream.write(data)  # 将帧写入数据流对象中，以此播放之
#         data = wf.readframes(chunk)  # 继续读取后面的帧
#         # dump_buff_file.write(str(data) + "\n---------------------------------------\n")  # 将读出的帧写入文件中，每一个帧用分割线隔开以便阅读
#
#     stream.stop_stream()  # 停止数据流
#     stream.close()  # 关闭数据流
#     p.terminate()  # 关闭 PyAudio
#     print('play函数结束！')
#
# getVideo(path)
# play(path+'.wav')