from ollama import Client

client = Client(
  host='http://server_ip:11434',
  headers={'x-some-header': 'some-value'}
)
response = client.chat(model='qwen3.5:9b', messages=[
  {
    'role': 'user',
    'content': '介绍一下vln',
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