from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="./data/stu.csv",
    csv_args={
        "delimiter": ",",
        "quotechar": '"',
        "fieldnames": ["name", "age", "gender"],
    },
    encoding="utf-8",
)

# docs = loader.load()

# for doc in docs:
#     print(type(doc),doc)

for doc in loader.lazy_load():
    print(doc)
