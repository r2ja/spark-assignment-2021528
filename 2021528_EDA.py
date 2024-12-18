from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when, year
import matplotlib.pyplot as plt
import pandas as pd

# Create a SparkSession
spark = SparkSession.builder \
    .appName("2021528_EDA") \
    .getOrCreate()

# Load the CSV into a Spark DataFrame
file_path = "netflix_titles.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Display the schema
df.printSchema()

# Show the first few rows
df.show(5)

# Check for missing values
missing_values = df.select([(count(when(col(c).isNull(), c))).alias(c) for c in df.columns])
missing_values.show()

# Basic EDA
# Distribution of shows by type
type_counts = df.groupBy("type").count()
type_counts.show()

# Most common release years
release_year_counts = df.groupBy("release_year").count().orderBy(col("count").desc())
release_year_counts.show()

# Visualize the distribution of ratings
ratings = df.groupBy("rating").count().orderBy(col("count").desc()).toPandas()
ratings.plot(kind="bar", x="rating", y="count", title="Distribution of Ratings")
plt.savefig("ratings_distribution.png")
plt.close()

# Distribution of shows added over time
date_added_distribution = df.select(year(col("date_added")).alias("year")).groupBy("year").count().orderBy("year")
date_added_distribution.show()

# Save results to CSV
type_counts.toPandas().to_csv("type_counts.csv", index=False)
release_year_counts.toPandas().to_csv("release_year_counts.csv", index=False)

# Stop the Spark session
spark.stop()
