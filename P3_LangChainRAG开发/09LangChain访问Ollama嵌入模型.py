"""
LangChain 访问 Ollama 嵌入模型示例

此示例展示如何使用 LangChain 的 OllamaEmbeddings 在本地运行嵌入模型，
将文本转换为向量表示。

前置要求：
1. 安装 Ollama：https://ollama.com/
2. 下载嵌入模型：ollama pull qwen3-embedding:4b
3. 安装依赖：pip install langchain-ollama
"""

from langchain_ollama import OllamaEmbeddings

# 初始化本地 Ollama 嵌入模型
model = OllamaEmbeddings(model="qwen3-embedding:4b")

# 向量化单个查询文本
# embed_query 用于将用户查询转换为向量
query_embedding = model.embed_query("我喜欢你")
print("查询向量:", query_embedding)

# 向量化多个文档
# embed_documents 用于批量将文档转换为向量
document_embeddings = model.embed_documents(["我喜欢你", "我稀罕你", "晚上吃啥"])
print("文档向量列表:", document_embeddings)