"""
LangChain ChatPromptTemplate 的使用示例

此示例展示如何使用 ChatPromptTemplate 创建聊天风格的提示词模板，
支持消息历史和动态内容插入。
"""

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 创建聊天提示词模板
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个边塞诗人，可以作诗"),  # 系统消息
    MessagesPlaceholder("history"),  # 历史消息占位符
    ("human", "请再来一首唐诗")  # 用户消息
])

# 准备历史对话数据
history_data = [
    ("human", "你来写一个唐诗"),
    ("ai", "床前明月光，疑是地上霜。举头望明月，低头思故乡。"),
    ("human", "请再来一首唐诗"),
    ("ai", "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。")
]

# 使用 invoke 方法填充模板
prompt_text = chat_prompt_template.invoke(input={"history": history_data}).to_string()
print(prompt_text)

# 调用模型
model = Tongyi(model="qwen-max")
print("--------------------------------")
print(model.invoke(prompt_text))