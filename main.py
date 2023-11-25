import dao

#user = {"name":"宮崎","score":"530000"}

#dao.insert_one(user)

result = dao.find_all()
print(result)
print(result[0]["name"])
#データベースを並び順でとれるとは限らない。取得するときにスコアが高い順などにしたいときは、
#ORDER BY SCORE DESCで高い順番で取得できる。
#受け取ってから並べ替えてもいいが、最初から並べ替えて取得する方がシンプル
