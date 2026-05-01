"""
LangChain 消息的简写形式示例

此示例展示如何使用元组形式的消息简写语法，
简化消息的创建过程。
"""

from langchain_community.chat_models.tongyi import ChatTongyi

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 使用元组简写形式创建消息列表
# 格式：(消息类型, 消息内容)
# 支持的类型：
# - "system": 系统消息，设定角色
# - "human": 用户消息
# - "ai": AI回复消息
# - "function": 函数调用消息
messages = [
    ("system", "你是一个边塞诗人"),  # 系统提示
    ("human", "写一首唐诗"),  # 用户输入
    ("ai", "锄禾日当午，汗滴禾下土；谁知盘中餐，粒粒皆辛苦。"),  # AI回复
    ("human", "按照你上一个回复的格式，再写一首唐诗"),  # 用户输入
]

# 使用stream方法进行流式调用
res = model.stream(input=messages)

# 遍历生成器，逐块打印响应内容
for chunk in res:
    print(chunk.content, end="", flush=True)