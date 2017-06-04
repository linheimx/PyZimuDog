import re

from typing import List
from bs4 import Tag
from bs4 import BeautifulSoup
import requests


base_url = 'http://www.zimuku.net'


def get_RelatedList(keyword: str) -> list:
    '''
    从关键字找出相关的字幕信息
    :param keyword: 
    :return: 
    '''
    r = requests.get(base_url + '/search?ad=1&q={0}'.format(keyword))
    print('---> search url ：{0}'.format(r.request.url))

    dom = BeautifulSoup(r.text, 'html.parser')

    list_movie = list()

    div_blocks = dom.find_all('div', class_='item prel clearfix')
    for div_block in div_blocks:  # type:Tag
        movie = get_MoveInfo(div_block)
        if movie:
            list_movie.append(movie)
            print(movie)
        break
    return list_movie


def get_MoveInfo(div_block) -> dict:
    '''
    分析网页，获得电影的信息
    :param div_block: 
    :return: 
    '''
    movie = dict()

    hit1 = div_block.find_all('a', href=re.compile(r'/subs/\d+.html'))  # type:List[Tag]
    if None == hit1:
        return None

    img = hit1[0].findChild()
    movie['pic'] = 'http:' + img['data-original']
    movie['name'] = hit1[1].string

    div_items = div_block.find_all('div', class_='sublist')
    for div_item in div_items:
        trs = div_item.find_all('tr')

        list_one = list()
        for tr in trs:
            #  ------------------------------> zimu <-------------------------------
            zimu = dict()
            # language
            img = tr.find('img')  # type:Tag
            zimu['language_pic'] = base_url + '/' + img.attrs['src']
            zimu['language'] = img.attrs['alt'].lstrip()
            # detail_url
            a = tr.find('a')
            zimu['detail_url'] = base_url + a.attrs['href']
            list_one.append(zimu)
        movie['list_zimu'] = list_one
    return movie


def get_DownloadUrl(detail_url: str):
    '''
    获取字幕的下载地址
    :param detail_url: 
    :return str: 
    '''
    r = requests.get(detail_url)
    hitUrl = re.findall(re.compile('/download/\w*"(?=>)'), r.text)[0]
    hitUrl = base_url + hitUrl
    return hitUrl


def download_Zimu(url: str):
    '''
    下载字幕
    :param url: 
    :return: 
    '''
    print('download:' + url)
    r = requests.get(url)
    if r.status_code == 200:
        with open('test.srt', 'wb') as f:
            for chunk in r:
                f.write(chunk)


'''-------------------------> go <----------------------------'''

if __name__ == '__main__':
    movie = input("请输入电影名称:")
    list_zimu = get_RelatedList('本杰明·巴顿奇事')

    # if list_zimu.__len__() > 0:
    #     zimu = list_zimu[0]
    #     ones = zimu['list_zimu']
    #     one = ones[0]
    #
    #     # url = get_DownloadUrl(one['detail_url'])
    #     # download_Zimu(url)
