import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass  # to have the class empty
    def get_logging(self):
        logger_name = inspect.stack()[1][3]
        # returns logger with the given logger name, name is the name of the test, that will be
        # passed to the log object.
        # name will run the class (this class) name methods
        # even if the methods are ran from the child class
        # .test() is a function
        log = logging.getLogger(logger_name)

        # creates the log file with the name provided as an argument
        file_handler = logging.FileHandler("logs.log")

        # adds file handler to the log object
        log.addHandler(file_handler)

        # custom error message
        # log.error("This is error statement")

        # custom format asctime is the runtime
        set_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # set the format of the log file to set_format format
        file_handler.setFormatter(set_format)

        # sets the lowest level of logging (debug -> critical)
        log.setLevel(logging.INFO)

        # logging messages by default only, warning and error logs are shown
        # log.debug("This is a debug statement")
        # log.info("This is an info statement")
        # log.debug("This is a debug statement")
        # log.error("This is error statement")
        # log.warning("This is a waning statement")
        # log.critical("This is a CRITICAL Error!")