"""
LangChain 通用提示词模板示例

此示例展示如何使用 PromptTemplate 创建可复用的提示词模板，
通过参数化方式生成动态提示词。
"""

from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 使用 from_template 方法创建提示词模板
# 模板中使用 {变量名} 的形式定义占位符
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，你帮我起个名字，简单回答。"
)

# 使用 format 方法填充模板，生成具体的提示文本
prompt_text = prompt_template.format(lastname="张", gender="女")

# 初始化模型并调用
model = Tongyi(model="qwen-max")
response = model.invoke(input=prompt_text)
print(response)