import sys
import logging
import traceback
from src.logger import logging 
def error_message_detail(error, error_detail: sys):
    """
    Extract detailed error message from exception info.
    """
    # Get the traceback object from sys.exc_info()
    _, _, exc_tb = error_detail.exc_info()  # Correct way to get traceback
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    error_message = f"Error occurred in script [{file_name}] line number [{line_no}] error message [{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        # Generate detailed error message
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    


