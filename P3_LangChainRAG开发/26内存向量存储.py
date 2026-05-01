"""
LangChain 内存向量存储示例

此示例展示如何使用 InMemoryVectorStore 进行向量存储操作：
1. 创建内存向量存储实例
2. 使用 CSVLoader 读取 CSV 文件（info.csv）
3. 添加文档到向量存储（带自定义ID）
4. 删除指定ID的文档
5. 根据用户问题进行相似度搜索

InMemoryVectorStore 特点：
- 数据存储在内存中，程序退出后数据丢失
- 适合小规模数据测试和原型开发
- 支持文档的添加、删除和搜索操作

info.csv 文件结构：
- source: 来源标识（如"黑马程序员"、"传智教育"）
- info: 信息内容

前置要求：
pip install langchain-community dashscope
"""

from langchain_community.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader


# 创建内存向量存储实例
# 参数说明：
# - embedding: 嵌入模型，用于将文本转换为向量表示
vector_store = InMemoryVectorStore(
    embedding=DashScopeEmbeddings()  # 使用阿里云 DashScope 嵌入模型
)

# 创建 CSVLoader 实例，加载 info.csv 文件
# 参数说明：
# - file_path: CSV 文件路径
# - encoding: 文件编码
# - source_column: 指定哪一列作为文档的来源标识（会存入 metadata）
loader = CSVLoader(
    file_path="./data/info.csv",
    encoding="utf-8",
    source_column="source"
)

# 加载文档，返回 Document 对象列表
# 每个 Document 包含 page_content（文本内容）和 metadata（元数据）
documents = loader.load()

# 将文档添加到向量存储
# 参数说明：
# - documents: 要添加的 Document 对象列表
# - ids: 可选参数，为每个文档指定自定义ID（便于后续删除操作）
vector_store.add_documents(
    documents=documents,
    ids = ["id" + str(i) for i in range(1,len(documents)+1)]  # 生成 id1, id2, ..., idN
)

# 从向量存储中删除指定ID的文档
# 参数说明：
# - ids: 要删除的文档ID列表
vector_store.delete(["id1","id2"])

# 执行相似度搜索
# 参数说明：
# - query: 用户查询文本
# - k: 返回最相关的前k条结果
res =vector_store.similarity_search(
    "Python是不是简单易学啊？",
    3
)

# 打印搜索结果
print(res)