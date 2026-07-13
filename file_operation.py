# with open("asset/system_prompt.txt", "r", encoding="utf-8") as f:
#      system_prompt = f.read()
#      print(f"system_prompt: {system_prompt}")

# with open("asset/system_prompt.txt", "w", encoding="utf-8") as f:
#      f.write(system_prompt)

# import json

# user={
#     "name": "东北雨姐",
#     "personality": "活泼开朗的东北姑娘",
#     "gender": "女",
#     "hobby": "唱歌、跳舞、旅游"
# }

# with open("asset/user.json", "w", encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False, indent=4)

# with open("asset/user.json", "r", encoding="utf-8") as f:
#     user_data = json.load(f)
#     print(f"user_data: {user_data}")
#     print(user_data["name"])

from pathlib import Path

filepath=Path("data")
print(filepath)
filepath=Path(__file__)
print(filepath)
print(filepath.name)
filepath=filepath.with_name("1.py")
print(filepath)
print(filepath.name)