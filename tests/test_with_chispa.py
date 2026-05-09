from chispa.dataframe_comparer import assert_df_equality
import logging

def test_data_integrity(spark_session):
 
    logger = logging.getLogger(__name__)
    expected_data = [(1, "A"), (2, "B")]
    # Data from Databricks
    actual_df = spark_session.createDataFrame(expected_data, ["id", "value"])
    
    # Expected data you've defined locally
    
    expected_df = spark_session.createDataFrame(expected_data, ["id", "value"])
    
    # Chispa comparison
    assert_df_equality(actual_df, expected_df, ignore_row_order=True)