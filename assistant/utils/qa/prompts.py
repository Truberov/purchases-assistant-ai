from langchain.prompts import PromptTemplate


prompt_template = """
As an expert in contextual reasoning and information extraction, your task is to respond to the following question based solely on the provided context. Imagine explaining the answer to a student without referencing any personal knowledge or the existence of contextual information.

CONTEXT
{context}
Question: {question}

Remember, if the necessary information isn't present in the context, indicate that you don't have the answer. Avoid referencing your own knowledge; rely solely on the context to formulate your response.

AI:"""


PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
