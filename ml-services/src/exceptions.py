import sys
from src.logger import logging

def error_message_detail(error, error_details:sys):
   _,_,exc_tb = error_details.exc_info()
   fileName = exc_tb.tb_frame.f_code.co_filename
   error_message = "Error occured in python script name: [{0}] \nline number: [{1}] \nerror message: [{2}]".format(
      fileName, exc_tb.tb_lineno, str(error)
   )
   return error_message

class CustomException(Exception):

   def __init__(self, errorMessage, errorDetail:sys):
      super().__init__(errorMessage)
      self.errorMessage = error_message_detail(errorMessage, error_details=errorDetail)
   
   def __str__(self):
      return self.errorMessage