from chat.agents import ToolBoundAgentBuilder


def main():
    message = input("Your question: ")
    agent = ToolBoundAgentBuilder()
    response = agent.invoke({"input": message})
    print(response)


if __name__ == "__main__":
    main()
