import unittest
from prelaunch_checks import prelaunch_check, check_api_keys, check_environment
from memory_management import MemoryManager
from gui import AIApp, launch_gui
import tkinter as tk
import threading


class TestAIApp(unittest.TestCase):

    def test_prelaunch_check(self):
        print("Testing prelaunch_check")
        with self.assertRaises(RuntimeError):
            prelaunch_check()

    def test_check_api_keys(self):
        print("Testing check_api_keys")
        try:
            check_api_keys()
        except RuntimeError as e:
            self.assertEqual(str(e), "Missing required API keys.")

    def test_check_environment(self):
        print("Testing check_environment")
        check_environment()

    def test_memory_manager(self):
        print("Testing MemoryManager")
        memory_manager = MemoryManager()
        self.assertIsNotNone(memory_manager)

    def test_gui_launch(self):
        print("Testing GUI launch")

        # Run the GUI in a separate thread, so it doesn't block the test script
        gui_thread = threading.Thread(target=launch_gui)
        gui_thread.start()

        # Give the GUI some time to launch before running the assertion
        self.assertIsInstance(AIApp(), tk.Tk)

        # Close the GUI window after a short delay
        gui_thread.join(timeout=5)


if __name__ == "__main__":
    unittest.main()
