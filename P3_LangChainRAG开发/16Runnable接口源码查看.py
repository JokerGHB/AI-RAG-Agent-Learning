"""
LangChain Runnable 接口示例

此示例展示如何通过管道操作符组合多个组件，
并查看生成的链类型。

Runnable 是 LangChain 中所有可组合组件的基础接口，
支持 invoke、stream、batch 等方法。
"""

from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

# 创建提示词模板
prompt = PromptTemplate.from_template("你是一个AI助手")

# 初始化模型
model = Tongyi(model="qwen-max")

# 使用管道操作符组合组件
# 链的结构：prompt -> model -> prompt -> model
chain = prompt | model | prompt | model

# 打印链的类型
# 这会显示组合后的 RunnableSequence 类型
print("链的类型:", type(chain))