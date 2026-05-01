"""
Python 的或运算符（|）重写示例

此示例展示如何通过重写 __or__ 方法，
实现自定义对象的管道操作，类似 LangChain 的链语法。

在 LangChain 中，正是通过这种方式实现了 prompt | model | parser 的链式调用。
"""

class Text(object):
    """
    文本对象类，支持管道操作
    """
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        """
        重写或运算符，返回一个序列对象
        """
        return Mysequence(self, other)

    def __str__(self):
        """
        返回对象的字符串表示
        """
        return self.name


class Mysequence(object):
    """
    序列对象类，支持链式管道操作
    """
    def __init__(self, *args):
        """
        初始化序列，接收多个 Text 对象
        """
        self.sequence = []
        for arg in args:
            self.sequence.append(arg.name)

    def __or__(self, other):
        """
        重写或运算符，追加新元素并返回自身（支持链式调用）
        """
        self.sequence.append(other.name)
        return self

    def run(self):
        """
        执行序列，打印所有元素
        """
        for i in self.sequence:
            print(i)


if __name__ == "__main__":
    # 创建多个 Text 对象
    a = Text('a')
    b = Text('b')
    c = Text('c')
    
    # 使用管道操作符组合对象
    # 等价于: a.__or__(b).__or__(c)
    d = a | b | c
    
    # 执行序列
    d.run()