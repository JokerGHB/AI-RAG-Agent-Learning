"""
LangChain TextLoader 和文档分割器示例

此示例展示如何使用 TextLoader 加载文本文件，
以及如何使用文本分割器将长文档分割成较小的块。

TextLoader：用于加载纯文本文件
Document Splitter：用于将长文档分割成较小的块，便于处理和向量化
"""

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 创建 TextLoader 实例，加载文本文件
loader = TextLoader(file_path="./data/document.txt", encoding="utf-8")

# 加载文档
docs = loader.load()
print("原始文档内容：")
print(docs)
print("=" * 50)

# 创建文本分割器
# RecursiveCharacterTextSplitter 按字符分割，优先按段落分割
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,  # 每个块的最大字符数
    chunk_overlap=10,  # 块之间的重叠字符数
    length_function=len  # 计算文本长度的函数
)

# 分割文档
split_docs = text_splitter.split_documents(docs)
print("分割后的文档块：")
for i, doc in enumerate(split_docs):
    print(f"块 {i + 1}: {doc.page_content}")
    print(f"元数据: {doc.metadata}")
    print("-" * 30)