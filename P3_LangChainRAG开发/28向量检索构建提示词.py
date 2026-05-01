"""
向量检索构建提示词示例（RAG 核心流程）

此示例展示完整的 RAG（Retrieval-Augmented Generation）流程：
1. 创建内存向量存储，并添加文本数据
2. 根据用户问题从向量库中检索相关文档
3. 将检索结果作为上下文构建提示词
4. 调用大模型生成回答

RAG 流程说明：
- Retrieval（检索）：根据用户问题在向量库中找到最相关的文档
- Augmented（增强）：将检索到的文档作为上下文注入提示词
- Generation（生成）：大模型基于上下文生成回答

此方法是构建智能问答系统的核心基础。

前置要求：
pip install langchain-community dashscope
"""

from langchain_community.chat_models import ChatTongyi
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. 创建聊天模型实例
# 使用阿里云通义千问的 ChatTongyi 模型
model = ChatTongyi(model="qwen3-max")

# 2. 创建聊天提示词模板
# 参数说明：
# - system: 系统提示，定义模型行为和角色，{context} 会替换为检索到的参考资料
# - user: 用户消息模板，{input} 会替换为用户提问
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "以我提供的已知参考资料为主，简洁和专业的回答用户问题。参考资料:{context}。"),
        ("user", "用户提问: {input}")
    ]
)

# 3. 创建内存向量存储实例
# 使用 DashScope 嵌入模型（text-embedding-v4）将文本转换为向量
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

# 6. 检索向量库
# similarity_search: 根据输入文本找到最相关的 k 条文档
result = vector_store.similarity_search(input_text, k=2)

# 7. 将检索结果拼接成上下文字符串
# 用于构建提示词中的 {context} 部分
reference_text = "["
for doc in result:
    reference_text += doc.page_content
reference_text += "]"
print(f"检索到的参考资料: {reference_text}")

# 8. 定义打印函数（用于调试，观察构建的提示词）
def print_prompt(prompt):
    print(prompt.to_string())
    print("-" * 30)
    return prompt

# 9. 构建 Chain（链式调用）
# 流程: prompt -> 打印调试 -> model -> 输出解析
chain = prompt | print_prompt | model | StrOutputParser()

# 10. 执行 Chain
# 将用户问题和检索到的参考资料传入
res = chain.invoke({"input": input_text, "context": reference_text})

# 11. 打印最终回答
print(f"模型回答: {res}")