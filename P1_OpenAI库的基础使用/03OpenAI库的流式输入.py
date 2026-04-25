from openai import OpenAI

# 1.获取client对象，OpenAI类对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 2.调用模型
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {"role": "system", "content": "你是一个Python编程专家，"},
        {"role": "user", "content": "输出1-10数字，使用python代码"},
    ],
    stream=True
)

# 3.处理结果
for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content,
              end=" ",
              flush=True
              )