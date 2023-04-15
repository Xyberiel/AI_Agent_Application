from agent_construction import construct_agent
from prelaunch_checks import prelaunch_check, check_api_keys
from memory_management import MemoryManager
from gui import launch_gui

def main():
    # Perform prelaunch checks
    prelaunch_check()
    openai_api_key, google_api_key = check_api_keys()

    # Initialize memory management
    memory_manager = MemoryManager()

    # Prompt the user to choose the desired ChatGPT model
    print("Please choose the desired ChatGPT model:")
    print("1. gpt-3.5-turbo")
    print("2. gpt-4")
    print("3. gpt-4-0314")
    print("4. gpt-4-32k")
    print("5. gpt-4-32k-0314")
    
    model_choice = int(input("Enter the number corresponding to your choice: "))

    model_mapping = {
        1: "gpt-3.5-turbo",
        2: "gpt-4",
        3: "gpt-4-0314",
        4: "gpt-4-32k",
        5: "gpt-4-32k-0314"
    }
    
    gpt_model = model_mapping.get(model_choice, "gpt-3.5-turbo")

    # Construct the AI agent
    agent_response = construct_agent(gpt_model, openai_api_key, google_api_key)
    print(agent_response)

    # Launch the GUI
    launch_gui()

if __name__ == "__main__":
    main()
