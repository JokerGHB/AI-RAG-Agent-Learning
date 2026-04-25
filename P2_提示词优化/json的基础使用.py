import json
d = {
    "name": "张三",
    "age": 18,
    "gender": "男"
}

s = json.dumps(d, ensure_ascii=False)
print(s)

l = [
    {
        "name": "张三",
        "age": 18,
        "gender": "男"
    },
    {
        "name": "李四",
        "age": 20,
        "gender": "女"
    },
    {
        "name": "王五",
        "age": 22,
        "gender": "男"
    }
]

print(json.dumps(l, ensure_ascii=False))

json_str = '{"name": "张三", "age": 18, "gender": "男"}'
json_array_str = '[{"name": "张三", "age": 18, "gender": "男"}, {"name": "李四", "age": 20, "gender": "女"}, {"name": "王五", "age": 22, "gender": "男"}]'

res_dict = json.loads(json_str)
print(res_dict, type(res_dict))

res_array = json.loads(json_array_str)
print(res_array, type(res_array))
