"""
LangChain 调用 Ollama 聊天模型示例

此示例展示如何使用 LangChain 的 ChatOllama 聊天模型，
在本地运行 Ollama 模型并进行多轮对话。
"""

from langchain_community.ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 初始化本地 Ollama 聊天模型
model = ChatOllama(model="qwen3:4b")

# 构建消息列表，包含多轮对话历史
messages = [
    SystemMessage(content="你是一个边塞诗人"),  # 设定角色
    HumanMessage(content="写一首唐诗"),  # 第一轮提问
    AIMessage(content="锄禾日当午，汗滴禾下土；谁知盘中餐，粒粒皆辛苦。"),  # 第一轮回复
    HumanMessage(content="按照你上一个回复的格式，再写一首唐诗")  # 第二轮提问
]

# 使用stream方法进行流式调用
res = model.stream(input=messages)

# 遍历生成器，逐块打印响应内容
for chunk in res:
    print(chunk.content, end="", flush=True)