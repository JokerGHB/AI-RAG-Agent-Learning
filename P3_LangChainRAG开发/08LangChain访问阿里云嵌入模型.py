"""
LangChain 访问阿里云嵌入模型示例

此示例展示如何使用 LangChain 的 DashScopeEmbeddings 访问阿里云的嵌入模型，
将文本转换为向量表示。

前置要求：
1. 安装依赖：pip install langchain-community
2. 配置环境变量 DASHSCOPE_API_KEY（阿里云DashScope API密钥）
"""

from langchain_community.embeddings import DashScopeEmbeddings

# 初始化阿里云嵌入模型
model = DashScopeEmbeddings()

# 向量化单个查询文本
# embed_query 用于将用户查询转换为向量
query_embedding = model.embed_query("我喜欢你")
print("查询向量:", query_embedding)

# 向量化多个文档
# embed_documents 用于批量将文档转换为向量
document_embeddings = model.embed_documents(["我喜欢你", "我稀罕你", "晚上吃啥"])
print("文档向量列表:", document_embeddings)