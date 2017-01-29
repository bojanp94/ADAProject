from pyspark import SparkContext
import pyspark.sql
#import pandas as pd
import json
import numpy as np

def is_json(myjson):
  try:
    json_object = json.loads(str(myjson))
  except (ValueError, Exception):
    return False
  return True

def has_category(x):
  try:
    a = x['categories']
  except (ValueError, Exception, KeyError):
    return False
  return True

def has_brand(x):
  try:
    a = x['brand']
  except (ValueError, Exception, KeyError):
    return False
  return True

rdd = sc.textFile("hdfs:///datasets/amazon-reviews")
rdd = rdd.filter(is_json)
rdd = rdd.map(lambda x: json.loads(str(x)))
rdd = rdd.map(lambda x: (x['asin'], (x['helpful'], x['reviewText'], x['overall'], x['summary'], x['reviewTime'])))
rdd.cache()

metaRdd = sc.textFile("hdfs:///datasets/amazon-reviews/metadata.json")
metaRdd = metaRdd.map(lambda x: eval(x))
metaRdd = metaRdd.filter(has_category)
metaRdd = metaRdd.filter(has_brand)
metaRdd = metaRdd.filter(lambda x: x['brand'] in US)
metaRdd = metaRdd.map(lambda x: (x['asin'], (x['categories'], x['brand'])))
metaRdd.cache()


joindSample = rdd.join(metaRdd)
joindSample.coalesce(1).saveAsTextFile("hdfs:///user/lmonnin/US.csv")


