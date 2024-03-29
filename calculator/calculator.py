'''calculator file'''

from importlib import import_module
import traceback
import logging
import os
import pandas as pd

# Configure logging
log_level = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=log_level)

class Calculator:
    '''Calculator class'''
    def __init__(self):
        self.history = pd.DataFrame(columns=['Expression', 'Result'])
        self.logger = logging.getLogger(__name__)

    def add_to_history(self, expression, result):
        '''Function to add to history'''
        self.history = self.history.append({
            'Expression': expression, 'Result': result}, ignore_index=True)
        self.logger.info("Added expression '%s' with result %s to history.", expression, result)

    def get_history(self):
        '''Function to get history'''
        return self.history

    def clear_history(self):
        '''Function to clear history'''
        self.history = pd.DataFrame(columns=['Expression', 'Result'])

    def save_history(self, filename):
        '''Function to save history'''
        self.history.to_csv(filename, index=False)

    def load_history(self, filename):
        '''Function to load history'''
        self.history = pd.read_csv(filename)

    def perform_operation(self, operation, a, b):
        '''Function to perform operations'''
        plugin_name = f"{operation}_plugin"
        try:
            plugin_module = import_module(f"plugins.{plugin_name}")
            plugin = getattr(plugin_module, f"{operation.capitalize()}Plugin")()
            result = plugin.execute(a, b)
            self.add_to_history(f"{a} {operation} {b}", result)
            return result
        except Exception as e:
            traceback.print_exc()  # Print full traceback
            raise ValueError(f"Plugin for {operation} not found: {e}") from e
