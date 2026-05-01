"""
LangChain JSONLoader 的使用示例

此示例展示如何使用 JSONLoader 加载 JSON 文件，
支持标准 JSON 文件和 JSON Lines 格式文件。

JSONLoader 特点：
- 支持通过 jq_schema 提取特定字段
- 支持 json_lines 模式（每行一个 JSON 对象）
- 适合加载结构化数据作为 RAG 的数据源
"""

from langchain_community.document_loaders import JSONLoader

# 创建 JSONLoader 实例
loader = JSONLoader(
    file_path="./data/stu_json_lines.json",  # JSON 文件路径
    jq_schema=".name",  # jq 查询表达式，提取 name 字段
    text_content=False,  # 是否提取文本内容（False 表示提取结构化数据）
    json_lines=True  # 是否为 JSON Lines 格式（每行一个 JSON 对象）
)

# 加载文档
docs = loader.load()

# 打印加载的文档
print(docs)