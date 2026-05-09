from databricks.connect import DatabricksSession

# 1. Initialize the session
# This automatically uses your local config (~/.databrickscfg)
spark = DatabricksSession.builder.getOrCreate()

# 2. Define your Unity Catalog path
# Format: /Volumes/<catalog>/<schema>/<volume_name>/<file_path>
csv_path = "/Volumes/sriunitycatalog/default/srivolume/taxi_zone_lookup.csv"

# 3. Read the CSV file into a Spark DataFrame
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(csv_path)

# 4. Show the first 5 rows
df.show(5)

# 5. (Optional) Convert to Pandas for local analysis
# local_df = df.toPandas()
# print(local_df.head())
