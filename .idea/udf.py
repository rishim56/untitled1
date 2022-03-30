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
#df.show(truncate=False)
convertUdf = udf(lambda z: convertCase(z))
df.select(col("ID"),convertUdf(col("Name")).alias("name")).show()
