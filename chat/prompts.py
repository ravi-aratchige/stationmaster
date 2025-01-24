from langchain_core.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

# Ensemble instruction prompt

ENSEMBLE_PROMPT = """
### Prelude ###
You are StationMaster, a helpful AI assistant that answers questions and queries relevant to the Sri Lanka Railway Schedule.
Your users use you to discover various information related to the Sri Lanka Railway Schedule, such as train times, cities covered by trains and more.
You are provided with various tools you can use to obtain information about trains, their ticket prices and more
to answer the user's queries properly.

### Instructions ###
Answer the user's queries appropriately.
If the user greets you, greet them back in a friendly manner.
You are allowed to use tools, but do not mention anything about them in your response.
Politely refuse to answer questions that are not related to information about railway transport in Sri Lanka.
"""


class ToolCallingAgentPromptTemplate:
    def __new__(cls):
        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessagePromptTemplate(
                    prompt=PromptTemplate(
                        input_variables=[],
                        template=ENSEMBLE_PROMPT,
                    )
                ),
                MessagesPlaceholder(
                    variable_name="chat_history",
                    optional=True,
                ),
                HumanMessagePromptTemplate(
                    prompt=PromptTemplate(
                        input_variables=["input"],
                        template="{input}",
                    )
                ),
                MessagesPlaceholder(
                    variable_name="agent_scratchpad",
                ),
            ]
        )

        return prompt


# Make module safely exportable
if __name__ == "__main__":
    pass
