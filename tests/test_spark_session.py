def test_file_exists_in_volume(spark):
    # Testing a table in Unity Catalog or Hive Metastore
    df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("D:/44.44_PythonProjects/DataRepoForPracticse/taxi_zone_lookup.csv")
    assert df.count() > 0
    df.show(5)

