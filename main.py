from my_agent.agent import root_agent

if __name__ == "__main__":
    while True:
        query = input("Enter your query: ")
        if query.lower() in ["exit", "quit"]:
            break

        response = root_agent.execute(query)

        print("Response:\n", response)