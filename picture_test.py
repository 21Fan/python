'''
Created on 2017年10月4日

@author: wantao
'''
import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header(
        'Use-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_address = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_address.append('http:' + html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=', b)
    return img_address


def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download__mm(folder='OOXX'):
    os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))
    for i in range(10):
        page_num -= i
        page_url = url + 'page' + str(page_num) + '#comments'
        img_address = find_imgs(page_url)
        save_imgs(folder, img_address)


if __name__ == '__main__':
    download__mm()
