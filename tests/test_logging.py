import logging

logger = logging.getLogger(__name__)

def test_logs():
    logger.info("Starting the test.for logs..")
    logger.debug("This is a debug message")
    assert True
    logger.info("This is a info message.")
    logger.error("This is a error message.")
    logger.warning("This is a warning message.")
