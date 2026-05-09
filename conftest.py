import os
import yaml
import pytest
import logging
import inspect
from pyspark.sql import SparkSession


# from databricks.connect import DatabricksSession

# @pytest.fixture(scope="session")
# def spark():
#     """Provides a remote Spark session for testing."""
#     return DatabricksSession.builder.getOrCreate()

logger = logging.getLogger(__name__)

def pytest_addoption(parser):
     # Register the command line flag
    parser.addoption("--env", action="store", default="dev")
   

def pytest_configure(config):
    # This runs immediately after command line args are parsed
    env_name = config.getoption("--env")
    print(f"Environment that has been passed through command line is {env_name}")
    config_path = f"configs/{env_name}_env_config.yaml"
    #Open and Load Yaml file that contains env configs
    with open(config_path,"r") as file:
        sri_config = yaml.safe_load(file)
    # Attach it to the config object so all tests can see it
    config.sri_config = sri_config
    print(f" Environment that has been selected is {sri_config['environment_indicator']}")
    # Dynamically set the log level based on env
    level = "DEBUG" if env_name == "dev" else "WARNING"
    config.option.log_cli_level = level
    print(f" Log Level that has been configured is {level}")
   
   
def pytest_sessionstart(session):
  # This hook runs after the logging system is fully initialized.
    env_name = session.config.getoption("--env")
    # This will now appear in BOTH the console and the log file
    logger.info(f"--- PyTest Session Started TEST RUN STARTED ---")
    logger.info(f"Target Environment: {env_name}")
    logger.info(f"########### Target Environment Config Variables START ##########)")
    logger.info(yaml.dump(session.config.sri_config))
    logger.info(f"########### Target Environment Config Variables END ##########)")

@pytest.fixture(scope="session")
def spark():
    # 1. Set Python-side logging for the py4j gateway
    logging.getLogger("py4j").setLevel(logging.ERROR)
    spark = SparkSession.builder.getOrCreate()
    # This silences the noisy internal JVM logs
    # spark.sparkContext.setLogLevel("ERROR") 
    yield spark
    spark.stop()
