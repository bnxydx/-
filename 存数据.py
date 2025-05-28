import db
from paqu import get_hero_list, get_hero

conn = db.DBHelper(host="127.0.0.1", port=3306, user="root", password="123456", db="LoL")


version_result = conn.fetch_all("SELECT VERSION()")
print(f"Database Version: {version_result[0]['VERSION()']}")

# 存库
for hero_id, hero_name in get_hero_list():
    print(f'正在下载+++{hero_name}')
    l = get_hero(hero_id)
    print(l)
    print(f'完成{hero_name}')
    print("存入数据库")
    for data in l:
        conn.insert(
            "INSERT INTO main(hero_name, hero_img_url) VALUES (%s, %s)",
            (data[0], data[1])
        )
    # break


conn.close()
