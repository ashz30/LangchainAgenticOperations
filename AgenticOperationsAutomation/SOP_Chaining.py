#https://python.langchain.com/docs/how_to/tools_chain/


import SOP.SOPProcessing
from langchain_openai import ChatOpenAI
from tools.ToolsManager import ToolsManager

if __name__ == '__main__':
    # get the SOP - standard RAG - unstructured text
    SOP_path = "SOP/SOP.txt"
    #use LLM to convert to sequence of steps
    SOP_text = SOP.SOPProcessing.read_SOP(SOP_path)

    llm = ChatOpenAI(model="gpt-4o-mini")
    userQuery = SOP_text
    manager = ToolsManager(llm, userQuery)
    response = manager.GetToolsResponse()


