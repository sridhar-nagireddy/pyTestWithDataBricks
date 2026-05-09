from chispa.dataframe_comparer import assert_df_equality
import logging
import builtins
import test_context

def test_data_integrity():
    spark = test_context.spark_session
    logger = logging.getLogger(__name__)
    expected_data = [(1, "A"), (2, "B")]
    # Data from Databricks
    actual_df = spark.createDataFrame(expected_data, ["id", "value"])
    
    # Expected data you've defined locally
    
    expected_df = spark.createDataFrame(expected_data, ["id", "value"])
    
    # Chispa comparison
    assert_df_equality(actual_df, expected_df, ignore_row_order=True)