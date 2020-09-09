import logging
#look at python documentation for logging.basicConfig
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# by default errors are going to root. so we need to create a file to do logging. In this example we use helper.py

# import helper

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler()
file_h = Logging.Filehandler('file.log')

#level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(Loggin.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')
