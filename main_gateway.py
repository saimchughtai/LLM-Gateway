from policy import policy_engine

def run_gateway():

    prompt = input("Enter prompt: ")

    decision = policy_engine(prompt)

    print("Decision:", decision)

    if decision == "BLOCK":
        print("Prompt blocked due to security risk.")

    elif decision == "MASK":
        print("Sensitive information detected. Prompt will be masked.")

    else:
        print("Prompt allowed and sent to LLM.")


if __name__ == "__main__":
    run_gateway()

