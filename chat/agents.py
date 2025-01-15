from providers.chat_models import GroqChatModel

# from chat.contextualizers import get_hotel_information
# from chat.contextualizers import get_experience_information
from chat.prompts import ToolBoundAgentPromptTemplate
from langchain.agents import AgentExecutor, create_tool_calling_agent


class ToolBoundAgentBuilder:
    def __new__(cls):
        # Initialize model to be used by agent
        model = GroqChatModel()

        # Build agent toolkit (contextualizers)
        toolkit = [
            # get_hotel_information,
            # get_experience_information,
        ]

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
            verbose=True,
        )

        return runnable_agent
