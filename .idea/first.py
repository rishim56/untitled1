from pyspark.sql import SparkSession

spark=SparkSession.builder.appName("intellij").master("local").getOrCreate()

spark.read.format("csv").load("data.csv").show()