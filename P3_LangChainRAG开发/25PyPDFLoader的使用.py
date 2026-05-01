"""
LangChain PyPDFLoader 的使用示例

此示例展示如何使用 PyPDFLoader 加载 PDF 文件。

PyPDFLoader：用于加载 PDF 文件，支持文本提取。

load() vs lazy_load() 的区别：
- load()：一次性加载所有文档到内存，返回文档列表
- lazy_load()：返回迭代器，按需加载，适合大文件

前置要求：
pip install pypdf
"""

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(file_path="./data/test.pdf")

print("=== lazy_load() 方法 ===")
print("返回迭代器，按需加载，适合处理大文件")
print("-" * 50)

lazy_loader = loader.lazy_load()
print(f"lazy_load() 返回类型: {type(lazy_loader)}")
print("-" * 50)



print("\n使用迭代器逐页加载：")
for i, doc in enumerate(lazy_loader):
    print(f"第 {i + 1} 页内容：")
    print(doc.page_content)
    print(f"元数据: {doc.metadata}")
    print("-" * 30)