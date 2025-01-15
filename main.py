from chat.agents import ToolBoundAgentBuilder


def main():
    test_question = "Are there trains available from Ja-ela to Colombo Fort?"
    message = input("Your question: ")
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    print(response["output"])


if __name__ == "__main__":
    main()
