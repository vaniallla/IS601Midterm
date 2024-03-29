# IS601Midterm

This is a simple calculator application that allows users to perform basic arithmetic operations and manage calculation history. It provides a user-friendly command-line interface (CLI) for interaction.

## Functionality

### Calculator Operations
The calculator supports the following basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

### History Management
The application effectively manages calculation history using Pandas DataFrame. Users can perform the following actions:
- View calculation history
- Clear calculation history
- Save calculation history to a CSV file
- Load calculation history from a CSV file

### Configuration via Environment Variables
The application supports configuration via environment variables for flexible application configuration. This allows for runtime configuration without modifying the code. The following environment variable is supported:
- The LOG_LEVEL environment variable is used to specify the desired logging level (e.g., DEBUG, INFO, WARNING, ERROR).
- The os.getenv() function is used to retrieve the value of the LOG_LEVEL environment variable.
- If the LOG_LEVEL environment variable is not set, it defaults to 'INFO'.

### REPL Interface
The application provides a user-friendly command-line interface (REPL) for interacting with the calculator. Users can perform arithmetic operations, manage history, and configure the application via simple commands.

### Logging
The application uses Python's built-in logging module for logging. You can configure the log level via the LOG_LEVEL environment variable. Supported log levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL. Logging is used throughout the implementation to record information, errors, and debugging messages. It provides insights into the program's behavior and aids in troubleshooting issues.
- The logging module is imported to set up logging configuration.
- The basicConfig() function is called to configure the root logger with a specified log level (retrieved from environment variables).
- Logging messages are emitted using various logging methods (info(), error(), etc.) throughout the codebase.
- See calculator.py under #configure logging

### Try/Except (Exceptions Usage):
Try/except blocks are utilized for error handling, following both the "Look Before You Leap" (LBYL) and "Easier to Ask for Forgiveness than Permission" (EAFP) paradigms.
- Try/except blocks are used to catch exceptions that may occur during critical operations, such as performing arithmetic calculations or loading plugins.
- LBYL: In some cases, such as dynamically loading plugins, the code checks for potential errors (e.g., missing plugin files) before attempting to execute the operation.
- EAFP: In other cases, such as performing arithmetic calculations, the code attempts the operation first and handles any exceptions that arise during execution.

### Installation
To install the required dependencies, run: pip install -r requirements.txt

### Usage
To start the calculator application, run the following command: python main.py