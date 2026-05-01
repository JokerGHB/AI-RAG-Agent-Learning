"""
LangChain RunnableLambda 的基础使用示例

此示例展示如何使用 RunnableLambda 在链中插入自定义函数，
实现数据转换或自定义逻辑。

RunnableLambda 允许将普通函数集成到链中，
支持同步和异步函数。
"""

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# 创建字符串输出解析器
str_parse = StrOutputParser()

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 创建第一个提示词模板：生成名字
first_prompt = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，刚生了{gender}，请起名。仅告知名字，不包含其他信息"
)

# 创建第二个提示词模板：解析名字含义
second_prompt = PromptTemplate.from_template("姓名{name}，请帮我解析含义")

# 创建链，使用匿名函数作为中间处理步骤
# 匿名函数将 AIMessage 对象转换为 {"name": content} 的格式
# 这样第二个提示词模板就能正确获取 name 参数
chain = first_prompt | model | (lambda ai_msg: {"name": ai_msg.content}) | second_prompt | model | str_parse

# 使用流式调用
for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)