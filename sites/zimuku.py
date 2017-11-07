from functools import lru_cache

from bs4 import BeautifulSoup, Tag
from models import Movie, PageMovie, Zimu
from utils import print_obj, fetch_text

base_url = 'http://www.zimuku.net'
api_movies = base_url + '/search?q={movie}&ad=1&p={page_index}'


@lru_cache(maxsize=2048)
def get_movie_list(kw_movie, pageIndex=0):
    url = api_movies.format(movie=kw_movie, page_index=pageIndex)
    html = fetch_text(url)
    dom = BeautifulSoup(html, 'html.parser')

    # movie
    div_items = dom.find_all('div', 'item prel clearfix')  # type:Tag
    movies = []
    for div in div_items:
        movie = process_movie_item(div)
        movies.append(movie)

    # page next
    haveNext = True
    div_page = dom.find('div', 'pagination l clearfix')
    index, haveNext = process_page_next(div_page)

    page = PageMovie(movies, index, haveNext)
    print_obj(page)


def process_page_next(div):
    # current
    span = div.select('span.current')[0]
    current = int(span.text)

    # next
    a_next = div.select('a.next')
    if a_next and len(a_next) == 1:
        return current, True
    else:
        return current, False


def process_movie_item(div_item: Tag) -> Movie:
    movie = Movie()

    # ----------------
    div1 = div_item.find('div', 'litpic hidden-xs hidden-sm')
    a = div1.findChild()
    # detail_url
    movie.detail_url = base_url + a['href']
    # avatar
    img = a.findChild()
    movie.avatar_url = img['data-original']

    # ---------------
    div2 = div_item.find('div', 'title')  # type:Tag
    b = div2.select("p a b")[0]  # type:Tag
    movie.name = b.text
    return movie


def i_____________________________________________________():
    pass


@lru_cache(maxsize=2048)
def get_zimu_list(url):
    html = fetch_text(url)
    dom = BeautifulSoup(html, 'html.parser')
    tbody = dom.select('div > table > tbody')[0]
    trs = tbody.select('tr')
    zimus = []
    for tr in trs:
        zimu = process_zimu(tr)
        zimus.append(zimu)

    print_obj(zimus)


def process_zimu(tr) -> Zimu:
    zimu = Zimu()
    a = tr.select('a')[0]
    zimu.name = a['title']
    zimu.detail_url = base_url + a['href']

    img = tr.select('img')[0]
    zimu.avatar_url = base_url + img['src']
    return zimu


def ii_____________________________________________________():
    pass


@lru_cache(maxsize=2048)
def get_download_url(url):
    html = fetch_text(url)
    dom = BeautifulSoup(html, 'html.parser')
    a = dom.select('a[dlurl]')[0]
    url = base_url + a['dlurl']
    return url


if __name__ == '__main__':
    get_movie_list('越狱')
    # # get_zimu_list('http://www.zimuku.net/subs/32677.html')
    # r = get_download_url('http://www.zimuku.net/detail/44173.html')
    # print(r)
