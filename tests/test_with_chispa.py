from chispa.dataframe_comparer import assert_df_equality
import logging

def test_data_integrity(spark):
 
    logger = logging.getLogger(__name__)
    # Data from Databricks
    actual_df = spark.read.table("main.default.my_table")
    
    # Expected data you've defined locally
    expected_data = [(1, "A"), (2, "B")]
    expected_df = spark.createDataFrame(expected_data, ["id", "value"])
    
    # Chispa comparison
    assert_df_equality(actual_df, expected_df, ignore_row_order=True)