# SQL for Marekters: Dominate data analytics, data science, and big data

from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext("local", "Simple App")
sqlContext = SQLContext(sc)

df = sqlContext.read.json("big_actions.json")
df.registerTempTable("user_actions")

df2 = sqlContext.sql("SELECT COUNT(*), product FROM user_actions WHERE action = 'purchase' GROUP BY product")

df2.show()
