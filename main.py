import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()

query = input("Query:")

# Define llm
# model = ChatOpenAI(model="gpt-4o")
# model = ChatGroq(model="meta-llama/llama-4-maverick-17b-128e-instruct",api_key="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")
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key="AIzaSyCro0p3rEfIel4Mw3MKfEVaMtaPGN_WQr4")

## server parameters
server_params={
        "tools": {
                "command": "python",
                "args": ["toolss.py"],
                "transport": "stdio",
            },  
        "ddg-search": {
            "command": "uvx",
            "args": ["duckduckgo-mcp-server"],
            "transport": "stdio"
        }
    }

# Define MCP servers
async def run_agent():
    try:
        client = MultiServerMCPClient(server_params)
        tools = await client.get_tools()
    except Exception as e:
        print("⚠️ Failed to load tools:", e)
        return "Tool initialization failed. Check server logs."

    agent = create_react_agent(model, tools)
    system_message = SystemMessage(content=(
        "You have access to multiple tools that can help answer queries. "
        "Use them dynamically and efficiently based on the user's request. "
        "If you need to use a tool, respond with the tool name and its parameters in the format: "
        "`{{tool_name: 'tool_name', args: {arg1: value1, arg2: value2}}}`. "
        "When you cannot answer the query because of not enough information then always use the web search tool "
    ))

    agent_response = await agent.ainvoke({
        "messages": [system_message, HumanMessage(content=query)]
    })

    return agent_response["messages"][-1].content

    

# Run the agent
if __name__ == "__main__":
    response = asyncio.run(run_agent())
    print("\nFinal Response:", response)
