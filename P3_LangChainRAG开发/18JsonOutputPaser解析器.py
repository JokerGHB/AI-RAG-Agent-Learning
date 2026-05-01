"""
LangChain JsonOutputParser 解析器示例

此示例展示如何使用 JsonOutputParser 将模型响应解析为 JSON 对象，
并在链中传递数据。

链的流程：
1. first_prompt -> model -> json_parse：生成名字并解析为 JSON
2. second_prompt -> model -> str_parse：根据名字解析含义
"""

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate

# 创建解析器
str_parse = StrOutputParser()  # 字符串解析器
json_parse = JsonOutputParser()  # JSON解析器

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 创建第一个提示词模板：生成名字并返回JSON格式
first_prompt = PromptTemplate.from_template(
    "我的邻居姓：{lastname}，刚生了{gender}，请起名。"
    "并封装为JSON格式返回给我。要求key是name，value是你起的名字，请严格遵守格式要求"
)

# 创建第二个提示词模板：解析名字含义
second_prompt = PromptTemplate.from_template("姓名{name}，请帮我解析含义")

# 创建完整链
# 流程：first_prompt -> model -> json_parse -> second_prompt -> model -> str_parse
chain = first_prompt | model | json_parse | second_prompt | model | str_parse

# 使用流式调用
for chunk in chain.stream({"lastname": "张", "gender": "女儿"}):
    print(chunk, end="", flush=True)