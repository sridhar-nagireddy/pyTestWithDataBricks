import builtins
import test_context

def test_file_exists_in_volume():
    spark = test_context.spark_session
    # Testing a table in Unity Catalog or Hive Metastore
    df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load('dbfs:/Volumes/sriunitycatalog/default/srivolume/taxi_zone_lookup.csv')
    assert df.count() > 0
    df.show(5)

