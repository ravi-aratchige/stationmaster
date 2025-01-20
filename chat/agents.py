from settings import AGENT_VERBOSITY
from providers.chat_models import GroqChatModel
from chat.prompts import ToolBoundAgentPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent
from oracle.contextualizers import get_ticket_prices, get_trains_between_stations


class ToolBoundAgentBuilder:
    def __new__(cls):
        # Initialize model to be used by agent
        model = GroqChatModel()

        # Build agent toolkit (contextualizers)
        toolkit = [get_trains_between_stations, get_ticket_prices]

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


# Make module safely exportable
if __name__ == "__main__":
    pass
