from agent import Agent


def main():

    print("=" * 60)
    print("My CLI Assistant")
    print("Type 'exit' or 'quit' to stop.")
    print("=" * 60)

    agent = Agent()

    while True:

        user_input = input("\n> ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        if not user_input:
            continue

        try:
            response = agent.chat(user_input)
            print(f"\nAssistant:\n{response}")

        except KeyboardInterrupt:
            print("\nOperation cancelled.")

        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()