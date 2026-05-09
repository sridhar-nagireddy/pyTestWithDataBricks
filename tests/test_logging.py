import logging
import test_context



logger = logging.getLogger(__name__)

def test_logs():
    spark = test_context.spark_session
    logger.info("Starting the test.for logs..")
    logger.debug("This is a debug message")
    assert True
    logger.info("This is a info message.")
    logger.error("This is a error message.")
    logger.warning("This is a warning message.")
