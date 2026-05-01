"""
LangChain Chain 的基础使用示例

此示例展示如何使用管道操作符（|）创建链，
将多个组件组合在一起执行。
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

# 初始化模型
model = Tongyi(model="qwen-max")

# 使用管道操作符创建链
# 链的执行流程：chat_prompt_template -> model
chain = chat_prompt_template | model

# 调用链
res = chain.invoke(input={"history": history_data})
print(res.content)