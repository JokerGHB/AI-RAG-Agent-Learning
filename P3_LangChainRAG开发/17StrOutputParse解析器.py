"""
LangChain StrOutputParser 解析器示例

此示例展示如何使用 StrOutputParser 将模型响应转换为字符串。

StrOutputParser 的作用：
- 将 AIMessage 对象转换为纯字符串
- 提取消息的 content 字段
"""

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

# 创建字符串输出解析器
parse = StrOutputParser()

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 创建提示词模板
prompt = PromptTemplate.from_template("我的邻居姓：{lastname}，刚生了{gender}，请起名，仅告知我名字无需其他内容")

# 创建链：prompt -> model -> parse -> model -> parse
chain = prompt | model | parse | model | parse

# 调用链，返回字符串类型
res = chain.invoke({"lastname": "张", "gender": "女儿"})
print("结果:", res)
print("结果类型:", type(res))