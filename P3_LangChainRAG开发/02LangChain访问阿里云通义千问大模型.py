"""
LangChain 访问阿里云通义千问大模型示例

此示例展示如何使用 LangChain 的 Tongyi 集成来调用阿里云的通义千问大模型。

前置要求：
1. 安装依赖：pip install langchain langchain-community
2. 配置环境变量 ALIBABA_CLOUD_API_KEY（阿里云API密钥）
"""

from langchain_community.llms.tongyi import Tongyi

# 初始化通义千问大模型
# model参数指定模型名称，如 "qwen-max", "qwen-plus" 等
model = Tongyi(model="qwen-max")

# 使用invoke方法调用模型
# input参数为用户的提问内容
response = model.invoke(input="你是谁能做什么？")

# 打印模型的响应
print(response)