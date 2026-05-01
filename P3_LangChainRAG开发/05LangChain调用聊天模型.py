"""
LangChain 调用聊天模型示例

此示例展示如何使用 LangChain 的 ChatTongyi 聊天模型，
支持多轮对话历史和角色设定。
"""

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 构建消息列表，包含多轮对话历史
# 消息类型：
# - SystemMessage: 系统提示，设定角色和行为准则
# - HumanMessage: 用户输入
# - AIMessage: AI的回复
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