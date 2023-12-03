from langchain.embeddings import HuggingFaceEmbeddings


def get_embeddings():
    return HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")
