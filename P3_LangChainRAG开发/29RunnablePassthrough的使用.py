"""
RunnablePassthrough 使用示例（实现自动检索增强的 RAG Chain）

此示例展示如何使用 RunnablePassthrough 简化 RAG 流程：
1. 将向量存储转换为 Retriever（检索器）
2. 使用 RunnablePassthrough 传递用户输入
3. 将 Retriever 结果自动格式化为上下文
4. 构建完整的 RAG Chain，实现自动检索和回答

与 28向量检索构建提示词.py 的区别：
- 旧版本：需要手动调用 similarity_search 获取检索结果
- 新版本：使用 Retriever + RunnablePassthrough，检索过程自动完成

RunnablePassthrough 作用：
- 用于传递输入值，不做任何转换
- 在 Chain 中保持输入变量的流动

前置要求：
pip install langchain-community dashscope
"""

from langchain_community.chat_models import ChatTongyi
from langchain_core.runnables import RunnablePassthrough
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# 1. 创建聊天模型实例
# 使用阿里云通义千问的 ChatTongyi 模型
model = ChatTongyi(model="qwen3-max")

# 2. 创建聊天提示词模板
# 参数说明：
# - system: 系统提示，{context} 替换为检索到的参考资料
# - user: 用户消息，{input} 替换为用户提问
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问: {input}")
    ]
)

# 3. 创建内存向量存储实例
# 使用 DashScope 嵌入模型将文本转换为向量
vector_store = InMemoryVectorStore(embedding=DashScopeEmbeddings(model="text-embedding-v4"))

# 4. 准备向量库数据（模拟知识库）
# add_texts: 将文本列表添加到向量存储中
vector_store.add_texts([
    "减肥就是要少吃多练",
    "在减脂期间吃东西很重要,清淡少油控制卡路里摄入并运动起来",
    "跑步是很好的运动哦"
])

# 5. 定义用户问题
input_text = "怎么减肥？"

# 6. 将向量存储转换为 Retriever（检索器）
# as_retriever: 将向量存储转换为可调用的检索器
# search_kwargs: 指定检索参数，k=2 表示返回最相关的2条结果
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 7. 定义打印函数（用于调试，观察构建的提示词）
def print_prompt(prompt):
    print(prompt.to_string())
    print("-" * 30)
    return prompt

# 8. 定义格式化函数
# 将检索到的 Document 列表格式化为字符串
# 参数说明：
# - docs: 检索到的 Document 对象列表
# - 返回格式化的字符串，如 "[文档1内容文档2内容]"
def format_func(docs):
    if not docs:
        return "无相关参考资料"
    formatted_str = "["
    for doc in docs:
        formatted_str += doc.page_content
    formatted_str += "]"
    return formatted_str

# 9. 构建 RAG Chain
# 流程说明：
# - {"input": RunnablePassthrough(), "context": retriever | format_func}: 
#     左侧输入时，input 直接透传，context 由 retriever 检索后经 format_func 格式化
# - | prompt: 将字典作为变量传递给 prompt 模板
# - | print_prompt: 打印调试
# - | model: 调用大模型生成回答
# - | StrOutputParser(): 解析输出为字符串
chain = {"input": RunnablePassthrough(), "context": retriever | format_func} | prompt | print_prompt | model | StrOutputParser()

# 10. 执行 Chain
# 注意：只需传入 input_text，retriever 会自动根据 input 进行检索
res = chain.invoke(input_text)

# 11. 打印最终回答
print(f"模型回答: {res}")