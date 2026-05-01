"""
LangChain 访问 Ollama 本地模型示例

此示例展示如何使用 LangChain 的 Ollama 集成来调用本地运行的大模型。

前置要求：
1. 安装 Ollama：https://ollama.com/
2. 下载模型：ollama pull qwen3:4b
3. 安装依赖：pip install langchain-ollama
"""

from langchain_ollama import OllamaLLM

# 初始化 Ollama 模型
# model参数指定本地模型名称，需要先通过 ollama pull 下载
model = OllamaLLM(model="qwen3:4b")

# 使用invoke方法调用本地模型
res = model.invoke(input="你是谁能做什么？")

# 打印模型响应
print(res)