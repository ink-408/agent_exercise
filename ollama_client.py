import json
from pathlib import Path
from ollama import Client

try:
  config_path=Path(__file__).with_name('config.json')
  config=json.loads(config_path.read_text(encoding='utf-8'))
  ollama_host=config.get('ollama_host')
except Exception as e:
  raise RuntimeError(f'配置文件出错: {e}')

client = Client(
  host=ollama_host,
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='qwen3.5:9b', messages=[
  {
    'role': 'user',
    'content': '介绍一下台风',
  },
],
  stream=True
)
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)

for i in response:
  print(i['message']['content'],end='')
print()
