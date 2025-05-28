import db

conn = db.DBHelper(host="127.0.0.1", port=3306, user="root", password="123456", db="LoL")

version_result = conn.fetch_all("SELECT VERSION()")
print(f"Database Version: {version_result[0]['VERSION()']}")

def search_heroes(keyword):
    """模糊搜索英雄"""
    results = conn.fetch_all(
        "SELECT * FROM main WHERE hero_name LIKE %s",
        (f"%{keyword}%",)
    )
    return results

# 使用示例
matches = search_heroes("安妮")
for hero in matches:
    print(f"{hero['hero_id']}: {hero['hero_name']}: {hero['hero_img_url']}")


