import re

from typing import List

from bs4 import Tag
from bs4 import BeautifulSoup
import requests

base_url = 'http://www.zimuku.net'

def analysis_Div4Zimu(div_block) -> dict:
    zimu = dict()

    hit1 = div_block.find_all('a', href=re.compile(r'/subs/\d+.html'))  # type:List[Tag]
    if None == hit1:
        return None

    img = hit1[0].findChild()
    zimu['pic'] = 'http:' + img['data-original']
    zimu['name'] = hit1[1].string

    div_items = div_block.find_all('div', class_='sublist')
    for div_item in div_items:
        trs = div_item.find_all('tr')

        list_one=list()
        for tr in trs:
            one=dict()
            # language
            img = tr.find('img')  # type:Tag
            one['language_pic']=base_url+'/'+img.attrs['src']
            one['language'] = img.attrs['alt'].lstrip()
            # detail_url
            a=tr.find('a')
            one['detail_url'] = base_url + a.attrs['href']
            list_one.append(one)
        zimu['ones']=list_one
    return zimu


def get_RelatedList(keyword: str) -> list:
    '''从关键字找出相关的字幕信息'''
    r = requests.get(base_url + '/search?ad=1&q={0}'.format(keyword))
    print('---> search url ：{0}'.format(r.request.url))

    dom = BeautifulSoup(r.text, 'html.parser')

    list_zimu = list()

    div_blocks = dom.find_all('div', class_='item prel clearfix')
    for div_block in div_blocks:  # type:Tag
        zimu = analysis_Div4Zimu(div_block)
        if zimu:
            list_zimu.append(zimu)
            print(zimu)
        break
    return list_zimu


def get_Detail(detail_url: str):
    r = requests.get(detail_url)
    hit = re.findall(re.compile('/download/\w*"(?=>)'), r.text)[0]
    hit = base_url + hit

    r=requests.get(hit)
    if r.status_code==200:
        with open('test.srt','wb') as f:
            for chunk in r:
                f.write(chunk)

    print(hit)


list_zimu = get_RelatedList('金刚')
if list_zimu.__len__() > 0:
    zimu=list_zimu[0]
    ones=zimu['ones']
    one=ones[0]
    get_Detail(one['detail_url'])
