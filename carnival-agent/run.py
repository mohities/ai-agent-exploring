from src.agent.carnival_agent import CarnivalAgent

def main():
    assistant = CarnivalAgent()
    
    # Simple test queries
    print("=== Testing Mode ===\n")
    
    test_queries = [
        "When is Carnival?",
        "What should I pack for 3 days?",
        "How's the weather in February?",
        "Is Rio safe for tourists?",
        "Hello there"
    ]
    
    for query in test_queries:
        print(f"User: {query}")
        response = assistant.respond(query)
        print(f"Assistant: {response}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()