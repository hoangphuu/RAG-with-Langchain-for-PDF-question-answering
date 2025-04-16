import re
from langchain_core.output_parsers import StrOutputParser

class Str_OutputParser(StrOutputParser):
    def __init__(self) -> None:
        super().__init__()

    def parse(self, text: str) -> str:
        return self.extract_answer(text)

    def extract_answer(self,
                     text_response: str,
                     pattern: str = r"Answer:\s*(.*)"
                     ) -> str:

        match = re.search(pattern, text_response)
        if match:
            answer_text = match.group(1).strip()
            return answer_text
        else:
            return "Answer not found."