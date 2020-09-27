# SQL for Marekters: Dominate data analytics, data science, and big data

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)

df = sqlContext.read.json("data.json")

# Displays the content of the DataFrame to stdout
df.show()