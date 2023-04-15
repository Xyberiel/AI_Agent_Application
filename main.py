from agent_construction import construct_agent
from prelaunch_checks import check_api_keys
from memory_management import MemoryManager
from gui import launch_gui

def main():
    # Initialize memory management
    print("Initializing memory management...")
    memory_manager = MemoryManager()

    # Launch the GUI
    print("Launching GUI...")
    launch_gui()

if __name__ == "__main__":
    main()
