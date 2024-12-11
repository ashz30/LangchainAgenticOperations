#https://python.langchain.com/docs/how_to/tools_chain/

#SOP list based iteration

import SOP.SOPProcessing
import json
from langchain_openai import ChatOpenAI
from tools.ToolsManager import ToolsManager

if __name__ == '__main__':
    # get the SOP - standard RAG - unstructured text
    SOP_path = "SOP/SOP.txt"
    #use LLM to convert to sequence of steps
    SOP_text = SOP.SOPProcessing.read_SOP(SOP_path)
    response = SOP.SOPProcessing.convert_SOP(SOP_text)
    print(response.content)
    # Find the JSON part using the boundaries of `{` and `}`
    start_index = response.content.find('{')
    end_index = response.content.rfind('}') + 1
    # Extract the JSON string
    json_part = response.content[start_index:end_index]
    SOP_dict = json.loads(json_part)

    #convert SOP to list which will later be used to run the process autonomously using tools/AI agent (simople tools agent is fine ,no need for langraph as its a seq one)
    SOP_list = list(SOP_dict.values())
    print (SOP_list)

    llm = ChatOpenAI(model="gpt-4o-mini")

    for SOP in SOP_list:
        userQuery = SOP
        manager = ToolsManager(llm, userQuery)
        response = manager.GetToolsResponse()


