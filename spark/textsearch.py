from pyspark import SparkConf, SparkContext

conf = (SparkConf()
        .setMaster("local")
        .setAppName("Error finder")
        .set("spark.executor.memory", "1g"))
sc = SparkContext(conf=conf)

file = sc.textFile("input_file.txt")
errors = file.filter(lambda line: "ERROR" in line)

# count all errors
errors.count()
# find all MySQL errors
mysql_errors = errors.filter(lambda line: "MySQL" in line)
# count all MySQL errors
mysql_errors.count()
# fetch all MySQL errors as array
mysql_errors.collect()
