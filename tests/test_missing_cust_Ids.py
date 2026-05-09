import builtins
from pyspark.sql.window import Window
from pyspark.sql import functions as F
import test_context

def test_find_sequence_gaps():
    spark = test_context.spark_session
    df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load('dbfs:/Volumes/sriunitycatalog/default/srivolume/taxi_zone_lookup.csv')
    assert df.count() > 0

    # Define window sorted by ID
    window_spec = Window.orderBy("LocationID")

    # Lead gets the value of the NEXT row
    df_with_next = df.withColumn("next_id", F.lead("LocationID").over(window_spec))

    last5 = spark.createDataFrame(df_with_next.tail(5))
    last5.show()

    
    # Find where (Next ID - Current ID) is not 1
    gaps = df_with_next.filter(
        (F.col("next_id").isNotNull()) & 
        (F.col("next_id") - F.col("LocationID") != 1)
    )

    assert gaps.count() == 0, f"Gaps found at: {gaps.collect()}"
