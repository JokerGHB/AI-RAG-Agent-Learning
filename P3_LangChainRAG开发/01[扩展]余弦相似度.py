import numpy as np

def get_dot(vec_a, vec_b):
    """
    计算两个向量的点积（内积）
    
    参数：
        vec_a: 第一个向量（列表或数组）
        vec_b: 第二个向量（列表或数组）
    
    返回：
        dot_sum: 两个向量的点积结果
    
    异常：
        ValueError: 如果两个向量维度不一致
    """
    if len(vec_a) != len(vec_b):
        raise ValueError("向量维度不一致")
    
    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b
    
    return dot_sum


def get_norm(vec):
    """
    计算向量的范数（模长）
    
    参数：
        vec: 输入向量（列表或数组）
    
    返回：
        norm: 向量的L2范数（欧几里得距离）
    """
    norm = 0
    for a in vec:
        norm += a ** 2
    
    return np.sqrt(norm)


def get_cosine_similarity(vec_a, vec_b):
    """
    计算两个向量的余弦相似度
    
    余弦相似度公式：cos(theta) = (A·B) / (||A|| * ||B||)
    
    参数：
        vec_a: 第一个向量（列表或数组）
        vec_b: 第二个向量（列表或数组）
    
    返回：
        similarity: 余弦相似度值，范围[-1, 1]
                    值越接近1表示越相似，越接近-1表示越不相似
    """
    dot_sum = get_dot(vec_a, vec_b)
    norm_a = get_norm(vec_a)
    norm_b = get_norm(vec_b)
    
    return dot_sum / (norm_a * norm_b)


if __name__ == "__main__":
    # 测试向量
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]  # 与vec_a方向相同，相似度高
    vec_c = [0.7, 0.5]  # 与vec_a有一定夹角
    vec_d = [-0.6, -0.5]  # 与vec_a方向相反，相似度低
    
    # 计算并打印余弦相似度
    print("ab:", get_cosine_similarity(vec_a, vec_b))
    print("ac:", get_cosine_similarity(vec_a, vec_c))
    print("ad:", get_cosine_similarity(vec_a, vec_d))