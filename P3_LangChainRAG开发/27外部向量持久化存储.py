"""
LangChain 外部向量持久化存储示例（使用 Chroma）

此示例展示如何使用 Chroma 向量数据库进行持久化存储操作：
1. 创建 Chroma 向量存储实例（数据持久化到磁盘）
2. 使用 CSVLoader 读取 CSV 文件（info.csv）
3. 添加文档到向量存储（带自定义ID）
4. 删除指定ID的文档
5. 根据用户问题进行相似度搜索（支持过滤条件）

Chroma 特点：
- 数据持久化存储到磁盘（指定 persist_directory）
- 程序退出后数据不丢失，下次运行可继续使用
- 支持元数据过滤搜索
- 适合生产环境和需要长期保存数据的场景

info.csv 文件结构：
- source: 来源标识（如"黑马程序员"、"传智教育"）
- info: 信息内容

前置要求：
pip install langchain-chroma langchain-community dashscope
"""

from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.document_loaders import CSVLoader


# 创建 Chroma 向量存储实例（持久化到磁盘）
# 参数说明：
# - collection_name: 集合名称，用于区分不同的数据集合
# - embedding_function: 嵌入模型，用于将文本转换为向量表示
# - persist_directory: 持久化目录，数据库文件将保存在此目录下
vector_store = Chroma(
    collection_name="test",
    embedding_function=DashScopeEmbeddings(),
    persist_directory="./chroma_db"  # 数据将保存在 chroma_db 目录下
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

# 执行相似度搜索（支持元数据过滤）
# 参数说明：
# - query: 用户查询文本
# - k: 返回最相关的前k条结果
# - filter: 可选参数，按元数据过滤搜索结果
res =vector_store.similarity_search(
    "Python是不是简单易学啊？",
    3,
    filter={"source":"黑马程序员"}  # 只搜索来源为"黑马程序员"的文档
)

# 打印搜索结果
for doc in res:
    print(doc.page_content)
    print(f"元数据: {doc.metadata}")
    print("-" * 30)