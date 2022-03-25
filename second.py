from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast
spark = SparkSession.builder.appName("intellij").master("local").getOrCreate()

data1 = spark.read.option("header","true").csv("Source1.csv")
data2 = spark.read.option("header","true").csv("Source2.csv")
data1Broadcast = broadcast(data1)
JoinData = data1Broadcast.join(data2,data1Broadcast.COUNTRY_CODE == data2.COUNTRY_CODE)
JoinData.explain()
