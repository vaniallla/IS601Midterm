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
The application supports configuration via environment variables for flexible application configuration. The following environment variable is supported:
- `LOG_LEVEL`: Specifies the log level for logging (default: INFO)

### REPL Interface
The application provides a user-friendly command-line interface (REPL) for interacting with the calculator. Users can perform arithmetic operations, manage history, and configure the application via simple commands.

### Logging
The application uses Python's built-in logging module for logging. You can configure the log level via the LOG_LEVEL environment variable. Supported log levels are DEBUG, INFO, WARNING, ERROR, and CRITICAL.

### Installation
To install the required dependencies, run: pip install -r requirements.txt

### Usage
To start the calculator application, run the following command: python main.py