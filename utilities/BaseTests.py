import inspect
import logging
import pytest
from datetime import datetime
import base64
import configparser

@pytest.mark.usefixtures("setup_and_teardown")
class BaseTests:
    logger = None

    @classmethod
    def setup_class(cls):
        cls.logger = cls.getLogger()
        cls.config = configparser.ConfigParser()
        cls.config.read('../configurations/config.ini')

        # Retrieve credentials and settings
        cls.username = cls.config.get('credentials', 'username')
        cls.password = cls.config.get('credentials', 'password')

    def create_emailAddress(self):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        dummy_email = f"user{timestamp}@example.com"
        return "oneup"+dummy_email


    @classmethod
    def getLogger(cls):
        if cls.logger is None:
            logger_name = inspect.stack()[1][3]
            logger = logging.getLogger(logger_name)
            if not logger.handlers:
                file_handler = logging.FileHandler('/Users/gojacketz/PycharmProjects/POMFramework/logfiles/logfile.log')
                formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.setLevel(logging.INFO)
            cls.logger = logger
        return cls.logger
    # def getLogger(cls):
    #     loggerName = inspect.stack()[1][3]
    #     logger = logging.getLogger(loggerName)#file name
    #     fileHandler = logging.FileHandler('/Users/gojacketz/PycharmProjects/POMFramework/logfiles/logfile.log')#location of log files
    #     formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")#levelname - debut, info, error, etc
    #     fileHandler.setFormatter(formatter)
    #     logger.addHandler(fileHandler)#accepts filehandler object, file location
    #
    #     #must set logging level
    #     #if debug, see all, if info you see info, warning, error, critical
    #
    #     logger.setLevel(logging.INFO)
    #     return logger

    def unencode(self,todecode):

        mydecode  = todecode.encode("utf-8")
        mydecode = base64.decodebytes(mydecode).decode('ascii')
        return mydecode





    @classmethod
    def encodeplaintext(cls, toencode):
        return base64.b64encode(toencode.encode()).decode('ascii')
