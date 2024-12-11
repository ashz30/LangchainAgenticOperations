
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate
from langchain_core.tools import tool



def read_SOP(SOP_path : str):
    with open(SOP_path, 'r') as file:
        SOP_text = file.read()
    return SOP_text


#convert SOP to list
def convert_SOP (SOP_text):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")
    with open('SOP/system_prompt_conversion.txt', 'r') as file:
        system_prompt = file.read().strip()
    prompt = system_prompt + " " +SOP_text
    response = llm.invoke(prompt)
    return response
