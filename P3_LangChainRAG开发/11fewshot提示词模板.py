"""
LangChain Few-Shot 提示词模板示例

此示例展示如何使用 FewShotPromptTemplate 创建带有示例的提示词模板，
通过提供示例让模型学习特定的输出格式或行为。
"""

from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate
from langchain_community.llms.tongyi import Tongyi

# 创建示例模板，定义单个示例的格式
example_template = PromptTemplate.from_template("单词:{word},反义词:{antonym}")

# 准备示例数据
example_data = [
    {"word": "大", "antonym": "小"},
    {"word": "上", "antonym": "下"}
]

# 创建 Few-Shot 提示词模板
few_shot_prompt = FewShotPromptTemplate(
    examples=example_data,  # 示例数据列表
    example_prompt=example_template,  # 示例模板
    prefix="给出给定词的反义词，有如下示例",  # 前缀提示
    suffix="基于实例告诉我，{input_word}的反义词是？",  # 后缀提示（包含用户输入变量）
    input_variables=["input_word"]  # 输入变量列表
)

# 使用 invoke 方法生成完整提示词
prompt_text = few_shot_prompt.invoke(input={"input_word": "左"}).to_string()
print(prompt_text)

# 调用模型
model = Tongyi(model="qwen-max")
print("--------------------------------")
print(model.invoke(prompt_text))