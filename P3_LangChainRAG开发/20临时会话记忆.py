"""
LangChain 临时会话记忆示例

此示例展示如何使用 InMemoryChatMessageHistory 实现临时会话记忆功能。

InMemoryChatMessageHistory 的特点：
- 会话历史存储在内存中
- 程序重启后历史会丢失
- 适合临时会话场景

核心组件：
1. InMemoryChatMessageHistory: 内存会话历史存储
2. RunnableWithMessageHistory: 包装链以支持会话历史
3. MessagesPlaceholder: 提示词模板中的历史占位符
"""

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

# 初始化聊天模型
model = ChatTongyi(model="qwen-max")

# 创建聊天提示词模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你需要根据会话历史回应用户问题。"),
    MessagesPlaceholder("chat_history"),  # 会话历史占位符
    ("human", "{input}")  # 用户输入占位符
])

# 创建字符串输出解析器
str_parser = StrOutputParser()

# 辅助函数：打印完整提示词（用于调试）
def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt

# 创建基础链
base_chain = prompt | print_prompt | model | str_parser

# 会话历史存储字典（内存中的会话存储）
store = {}

# 获取会话历史的函数
def get_history(session_id):
    """
    根据会话ID获取或创建会话历史
    
    Args:
        session_id: 会话唯一标识
        
    Returns:
        InMemoryChatMessageHistory 实例
    """
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 创建带会话历史的链
conversation_chain = RunnableWithMessageHistory(
    base_chain,
    get_history,
    input_messages_key="input",  # 用户输入的参数名
    history_messages_key="chat_history"  # 历史消息的参数名
)

if __name__ == "__main__":
    # 会话配置
    session_config = {
        "configurable": {
            "session_id": "user_001"
        }
    }
    
    # 第1次对话
    res = conversation_chain.invoke({"input": "小明有两只猫"}, session_config)
    print("第1次执行：", res)
    
    # 第2次对话（历史已包含第一次）
    res = conversation_chain.invoke({"input": "小刚有一只狗"}, session_config)
    print("第2次执行：", res)
    
    # 第3次对话（历史已包含前两次）
    res = conversation_chain.invoke({"input": "总共几只动物"}, session_config)
    print("第3次执行：", res)