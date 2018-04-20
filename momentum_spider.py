# coding: utf-8
import re
import os
import urllib.request
from multiprocessing import Pool
import time

momentum_url = 'https://d3cbihxaqsuq0s.cloudfront.net/'


def spider():
    context = str(urllib.request.urlopen(momentum_url).read())
    return context


def parse_context(c):
#   c = c.decode('utf-8')
    image_keys = re.findall(r'\<Key\>(.+?)\<\/Key\>', c)
    '''for key in image_keys:
        print([momentum_url + key])'''
    return [
        momentum_url + key for key in image_keys
    ]


def main():
    context = spider()
    images = parse_context(context)[1:]

    p = Pool(6)
    p.map(save_img, images)
    p.close()
    p.join()


def save_img(img_url, file_path = 'D:\picture\mumentum'):
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        file_suffix = os.path.basename(img_url)
        filename = '{}{}{}'.format(file_path, os.path.sep, file_suffix)
        urllib.request.urlretrieve(img_url, filename=filename)
        print(filename)
    except IOError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == '__main__':

    print('start...')
    s = time.time()
    main()
    print('finished')
    print(time.time() - s)
