import logging
import os

# Configuracion del logging
#
# NOTE: Configuramos el logging para que solo muestre mensajes de nivel INFO o superior
#       y que oculte los mensajes de librerias externas como matplotlib, PIL, tensorflow, torch y sklearn
#       https://docs.python.org/3/library/logging.html#logging.basicConfig
#       https://docs.python.org/3/library/logging.html#logging.Logger.setLevel
#       https://docs.python.org/3/library/logging.html#levels
#
def set_logging(log_file="exercise.log"):
    """ 
    Set up logging configuration to display messages of level INFO and above,
    while suppressing less critical messages from certain external libraries.

    This function configures the logging module to show messages of level INFO or higher.
    It also sets the logging level of specific external libraries to WARNING to reduce verbosity.
    """
    # Ensure the log directory exists
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove all handlers associated with the root logger (avoid duplicates)
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a file handler and set its level and formatter
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Reduce verbosity from external libraries
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    logging.getLogger('PIL').setLevel(logging.WARNING)
    logging.getLogger('tensorflow').setLevel(logging.WARNING)
    logging.getLogger('torch').setLevel(logging.WARNING)
    logging.getLogger('sklearn').setLevel(logging.WARNING)
    
def plog(message, level=logging.INFO, eol=False):                          
    """
    Print log messages with color coding based on severity level.
    
    Args:
        message (str): The log message to be printed.
        level (int):  The severity level of the log message. Defaults to logging.INFO.
                        Possible values: logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR.
        eol (bool):   If True, adds an extra newline after the message for better readability. Defaults to False.
    """

    # ANSI escape codes for colors
    color = ""
    reset = "\033[0m"
    
    # Log the message using the logging module and set color based on level
    if level == logging.DEBUG:
        logging.info(message if not eol else message + "\n")
        color = "\033[36m"   # Cyan
    elif level == logging.INFO:
        logging.info(message if not eol else message + "\n")
        color = "\033[32m"   # Green
    elif level == logging.WARNING:
        logging.warning(message if not eol else message + "\n")
        color = "\033[33m"   # Yellow
    elif level == logging.ERROR:
        logging.error(message if not eol else message + "\n")
        color = "\033[31m"   # Red
    else:
        color = ""
        
    # Deploy colored message to console
    print(f"{color}{message}{reset}" if not eol else f"{color}{message}{reset}\n")