import pyspark
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

AWS_ACCESS_KEY = "<snip>"
AWS_SECRET_KEY = "<snip>"

# create a context including the cassandra connector and hadoop-aws
conf = pyspark.SparkConf().set('spark.jars.packages', 'datastax:spark-cassandra-connector:2.4.0-s_2.11,org.apache.hadoop:hadoop-aws:2.7.0')\
                          .set("spark.executor.memory", "512m").setAppName('CrimeTest').setMaster('local[*]')
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)

# Demo - Write to s3, need to use credentials for the training account
sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", AWS_ACCESS_KEY)
sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", AWS_SECRET_KEY)
sc._jsc.hadoopConfiguration().set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

# as a demo we're only writing 1000 rows
mySparkDf.write\
  .format("csv").option("header","true").mode("Overwrite")\
  .save("s3a://allstate-program2-keys-654321/test_dir/mySparkDfData.csv")
