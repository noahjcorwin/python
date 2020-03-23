import json
import os
import enum
import shutil
 
# Enum for size units
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4

def convert_unit(size_in_bytes, unit):
   """ Convert the size from bytes to other units like KB, MB or GB"""
   if unit == SIZE_UNIT.KB:
       return size_in_bytes/1024
   elif unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
   elif unit == SIZE_UNIT.GB:
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes

def get_file_size(file_name, size_type = SIZE_UNIT.BYTES ):
   """ Get file in size in given unit like KB, MB or GB"""
   size = os.path.getsize(file_name)
   return convert_unit(size, size_type)

network_source = '//server/source'
network_dest = '//server/dest'

hbcli = 'D:/recode/HandBrakeCLI.exe'
recode = 'D:/recode'

encoder = 'nvenc_h265'
container = 'av_mkv'
quality = '25'
framerate = '29.97'
audio = 'copy'
acm = "copy:ac3,copy:dtshd,copy:dts,copy:eac3,copy:truehd"
afb = 'ac3'
maxheight = '720'

media_list = []
media_files = os.listdir(network_source)
for m in media_files:
    if '1080p' in m:
        full_path = network_source + '/' + m
        size = get_file_size(full_path, size_type = SIZE_UNIT.GB)
        if size > 5:
            media_list += [full_path]

for file in media_list:
    file_name = file.split(network_source + '/')[-1]
    source = recode + '/'+ file_name
    dest = source.replace('1080p','720p')
    if '264' in dest:
        dest = source.replace('264','265')
    args = f" -i {source} -o {dest} -e {encoder} -f {container} -q {quality} -r {framerate} -E {audio} --audio-copy-mask {acm} --audio-fallback {afb} -Y {maxheight}"
    shutil.copyfile(file,source)
    encode = hbcli + args
    os.system(encode)
    new_dest = dest.replace(recode,network_dest)
    shutil.copyfile(dest,new_dest)

