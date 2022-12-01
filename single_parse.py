import os
from turbojpeg import TurboJPEG
import time

jpeg = TurboJPEG()

def image_reader(img_path: str):
    in_file = open(img_path, 'rb')
    bgr_array_half = jpeg.decode(in_file.read())
    #print('file: ', (in_file))
    in_file.close()
    return bgr_array_half


arr_of_time=[]
for file in os.listdir('imgs/'):
    file='imgs/'+file
    start = time.time()
    img=image_reader(file)
    end = time.time()
    arr_of_time.append(end - start)

print('with single read')
print(f'{sum(arr_of_time)} seconds for {len(os.listdir("imgs/"))} images')
print('image shape: ',img.shape)