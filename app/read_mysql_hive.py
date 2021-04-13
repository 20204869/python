# -*- coding: utf-8 -*-

import sys
from pyspark.sql import SparkSession

encoding = sys.getfilesystemencoding()


# ======= 配置信息 =======
# 源数据库
originUrl = "jdbc:mysql://localhost:3306/demo?zeroDateTimeBehavior=convertToNull"
originUser = "root"
originPassword = "root"
originProperties = {"user": originUser, "password": originPassword}


# ======= 注册MySQL表 =======
def registDataFrame(spark, url, table, properties):
    spark.read.jdbc(
        url, table, properties=properties).createOrReplaceTempView(table)


if __name__ == '__main__':

    spark = SparkSession \
        .builder \
        .appName("实时数据处理") \
        .enableHiveSupport() \
        .config("spark.sql.crossJoin.enabled", "true") \
        .config("spark.sql.shuffle.partitions", "100") \
        .config("spark.network.timeout", "3600") \
        .config("spark.shuffle.consolidateFiles", "false") \
        .config("spark.speculation", "true") \
        .config("spark.executor.heartbeatInterval", "300") \
        .config("spark.executor.memory", "2g") \
        .config("spark.driver.maxResultSize", "2g") \
        .config("spark.task.maxFailures", "8") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic") \
        .config("hive.exec.dynamic.partition", "true") \
        .config("hive.exec.dynamic.partition.mode", "nonstrict") \
        .getOrCreate()

    originTables = ["person"]

    for originTable in originTables:
        registDataFrame(spark, originUrl, originTable, originProperties)

    # ======= 查询SQL =======
    update_time='2020-10-01'
    sql = f"""
        select * from person where update_time='{update_time}'
    """.format(update_time=update_time)

    sqlResult = spark.sql(sql)
    print(sqlResult)