import re
from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from .utils import Str_OutputParser

class Offline_RAG:
    def __init__(self, llm) -> None:
        self.llm = llm
        self.prompt = hub.pull("rlm/rag-prompt")
        self.str_parser = Str_OutputParser()

    def get_chain(self, retriever):
        input_data = {
            "context": retriever | self.format_docs,
            "question": RunnablePassthrough()
        }
        rag_chain = (
            input_data
            | self.prompt
            | self.llm
            | self.str_parser
        )
        return rag_chain

    def format_docs(self, docs):
        return "\n\n".join(doc.page_content for doc in docs)