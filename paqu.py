import requests
from fake_useragent import UserAgent
from time import sleep
from urllib.request import urlretrieve


def get_hero(hero_id=1):
    l = []
    url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{hero_id}.js'
    headers = {"User-Agent": UserAgent().chrome}
    resp = requests.get(url, headers=headers)
    # 获取相应数据
    for sk in resp.json().get('skins'):
        if sk.get("mainImg"):
            # print(f'皮肤名{sk.get("name")} 皮肤下载地址{sk.get("mainImg")}')
            # urlretrieve(sk.get("mainImg"), filename=f'./img/{sk.get("name").replace(" ", "_")}.jpg')
            sleep(0.2)
            l.append([sk.get("name"),sk.get("mainImg")])
    return l

def get_hero_list():
    url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
    headers = {"User-Agent": UserAgent().chrome}
    resp = requests.get(url, headers=headers)
    # 获取相应数据
    for i in resp.json().get('hero'):
        hero_id =  i.get("heroId")
        hero_name = i.get("name")
        # 将数据一一返回
        yield (hero_id, hero_name)


if __name__ == '__main__':
    # get_hero()
    for hero_id, hero_name in get_hero_list():
        print(f'正在下载+++{hero_name}')
        l = get_hero(hero_id)

        print(f'完成{hero_name}')
