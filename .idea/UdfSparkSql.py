from pyspark.sql import SparkSession
from pyspark.sql.functions import  col
from pyspark.sql.functions import udf

spark=SparkSession.builder.appName("intellij").master("local").getOrCreate()

def convertCase(x):
    new_data=""
    data=x.split(",")
    for i in data:
        new_data=new_data + i[0:1].upper() + i[1:len(i)] + " "
    return new_data
columns=["ID","Name"]
data=[("1","rishi"),("2","raj"),("3","yash")]

df=spark.createDataFrame(data=data,schema=columns)

""" Using UDF on SQL """
spark.udf.register("convertUDF", convertCase)
df.createOrReplaceTempView("NAME_TABLE")
spark.sql("select ID, convertUDF(Name) as Name from NAME_TABLE") \
    .show(truncate=False)