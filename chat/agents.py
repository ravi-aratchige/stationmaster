from providers.chat_models import GroqChatModel
from chat.prompts import ToolBoundAgentPromptTemplate
from oracle.contextualizers import search_for_basic_information
from langchain.agents import AgentExecutor, create_tool_calling_agent
from settings import AGENT_VERBOSITY


class ToolBoundAgentBuilder:
    def __new__(cls):
        # Initialize model to be used by agent
        model = GroqChatModel()

        # Build agent toolkit (contextualizers)
        toolkit = [search_for_basic_information]

        # Define agent instruction prompt
        prompt = ToolBoundAgentPromptTemplate()

        # Create agent with tool-calling capabilities
        agent = create_tool_calling_agent(
            model,
            toolkit,
            prompt,
        )

        # Define agent executor runtime
        runnable_agent = AgentExecutor(
            agent=agent,
            tools=toolkit,
            verbose=AGENT_VERBOSITY,
        )

        return runnable_agent
