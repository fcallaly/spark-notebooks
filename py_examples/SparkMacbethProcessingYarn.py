import pyspark
from pyspark import SparkContext

# configure the spark context
conf = pyspark.SparkConf().setMaster('yarn').setAppName("Spark_Macbeth")
sc = SparkContext(conf=conf)

# Load the Macbeth.txt file into a spark rdd
inputFile = sc.textFile("Macbeth.txt")

# Get the number of characters in each line

# the "non-lambda" version looks like this:
#
# def get_length(line):
#     return len(line)
# lineLengths = inputFile.map(getLength)

# same as above, but using a lambda
lineLengths = inputFile.map(lambda line: len(line))


# print the sum of all characters in the entire dataset
print('Total number of characters:', lineLengths.sum())


def count_words(line):
    return len(line.split(' '))

# transform the inputFile rdd through the count_words function
word_count_rdd = inputFile.map(count_words)

print('Total number of words: ', word_count_rdd.sum())
print('Mean number of words per line', word_count_rdd.mean())

