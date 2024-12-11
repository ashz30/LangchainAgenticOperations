
from tools.BpTools import ToolList
from langchain import hub

from langchain.agents import AgentExecutor, create_tool_calling_agent

class ToolsManager:

    def __init__(self, llm , userQuery):
        self.llm = llm
        self.userQuery = userQuery

    def GetToolsResponse(self):
        tools = ToolList.tools

        tools_assistant_prompt_file = "tools/tools_assistant_prompt.txt"

        with open(tools_assistant_prompt_file, 'r') as file:
            tools_assistant_prompt = file.read().strip()

        prompt = tools_assistant_prompt

        # Get the prompt to use - can be replaced with any prompt that includes variables "agent_scratchpad" and "input"!
        prompt = hub.pull("hwchase17/openai-tools-agent")
        prompt.pretty_print()

        # Construct the tool calling agent
        agent = create_tool_calling_agent(self.llm, tools, prompt)

        # Create an agent executor by passing in the agent and tools
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

        response = agent_executor.invoke(
            {
                "input": self.userQuery
            }
        )