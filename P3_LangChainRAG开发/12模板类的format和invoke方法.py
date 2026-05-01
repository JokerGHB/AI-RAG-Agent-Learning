"""
LangChain 模板类的 format 和 invoke 方法示例

此示例展示 PromptTemplate 的两种调用方式：
1. format() - 返回字符串
2. invoke() - 返回 PromptValue 对象
"""

from langchain_core.prompts import PromptTemplate

# 创建提示词模板
template = PromptTemplate.from_template("我的邻居是：{lastname}，最喜欢：{hobby}")

# 方法1：使用 format()
# 返回类型：str（字符串）
res = template.format(lastname="张大明", hobby="钓鱼")
print("format() 结果:", res, "类型:", type(res))

# 方法2：使用 invoke()
# 返回类型：PromptValue（提示值对象）
# invoke 方法更适合在链（Chain）中使用
res2 = template.invoke({"lastname": "周杰伦", "hobby": "唱歌"})
print("invoke() 结果:", res2, "类型:", type(res2))

# PromptValue 对象可以转换为字符串
print("invoke() 转换为字符串:", res2.to_string())