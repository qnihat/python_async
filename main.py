import os
from multiprocessing.pool import ThreadPool
from turbojpeg import TurboJPEG

import time

jpeg = TurboJPEG()
num_process = 10
data_folder='real_img/my_data/'


def image_reader(img_path: str):
    in_file = open(img_path, 'rb')
    bgr_array_half = jpeg.decode(in_file.read())
    in_file.close()
    return bgr_array_half


def run_im_reader(process:int, image_paths:list):
    print(f'Running {num_process} process')
    results = ThreadPool(process).imap_unordered(image_reader, image_paths)
    for img in results:
        pass
    print('image shape: ',img.shape)

images_url=[]
for file in os.listdir(data_folder):
    file=data_folder+file
    images_url.append(file)

print('num of imgs: ',len(images_url))
start = time.time()
run_im_reader(num_process, images_url)
end = time.time()
print(f'{end - start} seconds')