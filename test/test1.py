import hashlib
import os
import pickle
from concurrent.futures import thread

import time

cache_root_dir = 'cache'


if not os.path.exists(cache_root_dir):
    os.makedirs(cache_root_dir)


def md5(s):
    m = hashlib.md5()
    m.update(bytes(s,'utf-8'))
    return m.hexdigest()


def cache_key(f, *args, **kwargs):
    s = '%s-%s-%s' % (f.__name__, str(args), str(kwargs))
    return os.path.join(cache_root_dir, '%s.dump' % md5(s))


def cache(f):
    def wrap(*args, **kwargs):
        fn = cache_key(f, *args, **kwargs)
        if os.path.exists(fn):
            print('loading cache')
            with open(fn, 'rb') as fr:
                return pickle.load(fr)

        obj = f(*args, **kwargs)
        with open(fn, 'wb') as fw:
            pickle.dump(obj, fw)
        return obj

    return wrap


@cache
def add(a, b):
    time.sleep(5)
    return a + b


if __name__ == '__main__':
    print(add(3, 4))
    print(add(3, 4))
    print(add(3, 4))
    print(add(3, 4))
    print(add(3, 4))