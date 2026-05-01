"""
LangChain 长期会话记忆示例

此示例展示如何实现基于文件的长期会话记忆功能。

通过继承 BaseChatMessageHistory 自定义 FileChatMessageHistory，
将会话历史持久化到文件中，实现程序重启后仍能保留会话历史。

核心组件：
1. FileChatMessageHistory: 自定义文件存储会话历史
2. RunnableWithMessageHistory: 包装链以支持会话历史
3. message_to_dict/messages_from_dict: 消息序列化/反序列化
"""

import json
import os
from typing import Sequence, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import message_to_dict, messages_from_dict, BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory


class FileChatMessageHistory(BaseChatMessageHistory):
    """
    基于文件的会话历史存储类
    
    继承 BaseChatMessageHistory，实现消息的持久化存储。
    """
    
    def __init__(self, session_id, storage_path) -> None:
        """
        初始化文件会话历史
        
        Args:
            session_id: 会话唯一标识
            storage_path: 存储目录路径
        """
        self.session_id = session_id
        self.storage_path = storage_path
        self.file_path = os.path.join(self.storage_path, self.session_id)
        
        # 确保存储目录存在
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        """
        添加消息到历史记录
        
        Args:
            messages: 要添加的消息序列
        """
        # 获取所有历史消息
        all_messages = list(self.messages)
        # 添加新消息
        all_messages.extend(messages)
        
        # 将消息序列化为字典列表
        new_messages = [message_to_dict(message) for message in all_messages]
        
        # 写入文件
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property
    def messages(self) -> List[BaseMessage]:
        """
        获取所有历史消息
        
        Returns:
            消息列表
        """
        try:
            with open(self.file_path, "r") as f:
                messages_data = json.load(f)
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            # 文件不存在时返回空列表
            return []

    def clear(self) -> None:
        """清空会话历史"""
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


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

# 获取会话历史的函数
def get_history(session_id):
    """
    根据会话ID获取文件存储的会话历史
    
    Args:
        session_id: 会话唯一标识
        
    Returns:
        FileChatMessageHistory 实例
    """
    return FileChatMessageHistory(session_id, "./chat_history")

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
    
    # # 第1次对话（取消注释以启用）
    # res = conversation_chain.invoke({"input": "小明有两只猫"}, session_config)
    # print("第1次执行：", res)
    
    # # 第2次对话（取消注释以启用）
    # res = conversation_chain.invoke({"input": "小刚有一只狗"}, session_config)
    # print("第2次执行：", res)
    
    # 第3次对话（基于前两次的历史）
    res = conversation_chain.invoke({"input": "总共几只动物"}, session_config)
    print("第3次执行：", res)