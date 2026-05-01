"""
LangChain 流式输出示例

此示例展示如何使用 LangChain 的 stream 方法实现流式输出，
让模型响应逐字返回，提升用户体验。
"""

from langchain_community.llms.tongyi import Tongyi

# 初始化通义千问大模型
model = Tongyi(model="qwen-max")

# 使用stream方法进行流式调用
# stream方法返回一个生成器，逐块返回模型响应
res = model.stream(input="你是谁能做什么？")

# 遍历生成器，逐块打印响应
# end="" 表示不换行
# flush=True 表示立即刷新输出缓冲区
for chunk in res:
    print(chunk, end="", flush=True)