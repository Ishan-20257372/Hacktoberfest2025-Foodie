import logging
import sys
from datetime import datetime

# --- Configuration ---
LOG_FILE = 'app_activity.log'

def setup_logger(log_level=logging.INFO, log_to_file=True):
    """
    Configures and returns a root logger instance.

    Args:
        log_level (int): Minimum severity level to log (e.g., logging.DEBUG).
        log_to_file (bool): If True, messages are also written to LOG_FILE.
    """
    # 1. Get the root logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Check if handlers are already set up (prevents duplicate logs)
    if logger.handlers:
        for handler in logger.handlers:
            logger.removeHandler(handler)

    # 2. Define the formatter
    # Includes timestamp, level, logger name, and message
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 3. Setup Console Handler (for output to screen)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 4. Setup File Handler (optional)
    if log_to_file:
        file_handler = logging.FileHandler(LOG_FILE, mode='a') # 'a' for append
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    print(f"Logger set up. Messages being written to console and file: {log_to_file}")

# --- Example Usage ---

# 1. Configure the logger to log DEBUG and higher messages, and use a file
setup_logger(log_level=logging.DEBUG, log_to_file=True)

# 2. Get a named logger instance (useful for identifying where the message came from)
# If you don't use a name, it defaults to the root logger
main_logger = logging.getLogger(__name__)

main_logger.info("Application starting up.")
main_logger.debug("Checking initial configuration files...")

try:
    result = 10 / 0
except ZeroDivisionError:
    # Use logger.exception() inside an except block to automatically log traceback
    main_logger.exception("A critical calculation error occurred!") 

main_logger.warning("Resource utilization is getting high.")
