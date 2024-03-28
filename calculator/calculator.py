'''calculator file'''
# from add import AddPlugin
# from subtract import SubtractPlugin
# from multiply import MultiplyPlugin
# from divide import DividePlugin

from importlib import import_module

class Calculator:
    '''calculator class'''
    def __init__(self):
        self.history = []

    def add_to_history(self, expression, result):
        '''add operation to history'''
        self.history.append((expression, result))

    def get_history(self):
        '''show history function'''
        return self.history

    def clear_history(self):
        '''clear history function'''
        self.history = []

    def perform_operation(self, operation, a, b):
        '''operations function'''
        plugin_name = f"{operation}_plugin"
        try:
            plugin_module = import_module(f"plugins.{plugin_name}")
            plugin = getattr(plugin_module, f"{operation.capitalize()}Plugin")()
            result = plugin.execute(a, b)
            self.add_to_history(f"{a} {operation} {b} = {result}", result)
            return result
        except ModuleNotFoundError:
            raise ValueError(f"Plugin for {operation} not found")
