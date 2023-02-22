import subprocess
import os

# path = '/home/dataset'  # 待切割视频存储目录
# video_list = os.listdir(path)
# delta_X = 10  # 每10s切割
# save_path = '/home/save'
# mark = 0

path = 'test1.mp4'

def TimeFormat(t0):
    hour = int(t0/60/60)
    if hour < 0:
        hourstr = '00'
    else:
        if hour <10:
            hourstr = '0'+str(int(hour))
        else:
            hourstr = str(int(hour))
    tm0 = t0 - int(hour)*60*60
    tm = tm0/60
    if tm < 0:
        minstr = '00'
    else:
        if tm <10:
            minstr = '0'+str(int(tm))
        else:
            minstr = str(int(tm))
    ts = tm0 - int(tm) * 60
    if ts < 10:
        Secstr = '0'+str(ts)
    else:
        Secstr = str(ts)

    return hourstr+':'+minstr+':'+Secstr

# 获取视频的时长
def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    return float(result.stdout)

def cutVideo(path,timespan):
    videoName = 'tmp/'+os.path.basename(path)
    # 'ffmpeg -i input.mp4 -ss 00:01:20 -t 02:00:00 -vcodec copy -acodec copy output.mp4'
    command = 'ffmpeg -i {} -ss {} -to {} -vcodec copy -acodec copy  {}'.format(path,TimeFormat(timespan[0]),TimeFormat(timespan[1]),videoName)
    os.system(command)

TimeLen = get_length(path)
print(TimeLen)
cutVideo(path,[10,20])

#
#
# for file_name in video_list:
#     min = int(get_length(os.path.join(path, file_name))) // 60  # file_name视频的分钟数
#     second = int(get_length(os.path.join(path, file_name))) % 60  # file_name视频的秒数
#     for i in range(min + 1):
#         if second >= delta_X:  # 至少保证一次切割
#             start_time = 0
#             end_time = start_time + delta_X
#             for j in range((second // 10) + 1):
#                 min_temp = str(i)
#                 start = str(start_time)
#                 end = str(end_time)
#                 # crop video
#                 # 保证两位数
#                 if len(str(min_temp)) == 1:
#                     min_temp = '0' + str(min_temp)
#                 if len(str(start_time)) == 1:
#                     start = '0' + str(start_time)
#                 if len(str(end_time)) == 1:
#                     end = '0' + str(end_time)
#
#                 # 设置保存视频的名字
#                 if len(str(mark)) < 6:
#                     name = '0' * (6 - len(str(mark)) - 1) + str(mark)
#                 else:
#                     name = str(mark)
#                 command = 'ffmpeg -i {} -ss 00:{}:{} -to 00:{}:{} -strict -2 {}'.format(os.path.join(path, file_name),
#                                                                                         min_temp, start, min_temp, end,
#                                                                                         os.path.join(save_path,
#                                                                                                      'id' + str(
#                                                                                                          name)) + '.mp4')
#                 mark += 1
#                 os.system(command)
#                 if i != min or (i == min and (end_time + delta_X) < second):
#                     start_time += delta_X
#                     end_time += delta_X
#                 elif (end_time + delta_X) <= second:
#                     start_time += delta_X
#                     end_time += delta_X
#                 elif (end_time + delta_X) > second:  # 最后不足delta_X的部分会被舍弃
#                     break
