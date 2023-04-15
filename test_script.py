from prelaunch_checks import prelaunch_check, check_api_keys
from agent_construction import construct_agent
from gui import launch_gui
from memory_management import MemoryManager

# Test prelaunch_check
print("Testing prelaunch_check")
try:
    prelaunch_check()
except RuntimeError as e:
    print(f"Prelaunch check failed: {e}")

openai_api_key, google_api_key = check_api_keys()

# Test memory management
print("Testing MemoryManager")
try:
    memory_manager = MemoryManager()
    print("MemoryManager initialized successfully")
except Exception as e:
    print(f"MemoryManager initialization failed: {e}")

# Test agent construction
print("Testing agent construction")
try:
    gpt_model = "gpt-3.5-turbo"
    agent_response = construct_agent(gpt_model, openai_api_key, google_api_key)
    print("Agent constructed successfully")
    print(agent_response)
except Exception as e:
    print(f"Agent construction failed: {e}")

# Test GUI launch
print("Testing GUI launch")
try:
    launch_gui()
    print("GUI launched successfully")
except Exception as e:
    print(f"GUI launch failed: {e}")
