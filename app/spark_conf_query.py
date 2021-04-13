from pyspark.sql import SparkSession
from os.path import abspath
'''
spark 查询hive 参数配置
'''

if __name__ == '__main__':
    warehouse_location = abspath('spark-warehouse')
    sc = SparkSession \
        .builder \
        .appName("任务名称") \
        .config("spark.sql.warehouse.dir", warehouse_location) \
        .enableHiveSupport() \
        .config("spark.sql.crossJoin.enabled", "true") \
        .config("spark.sql.shuffle.partitions", "100") \
        .config("spark.network.timeout","3600") \
        .config("spark.shuffle.consolidateFiles","false") \
        .config("spark.speculation","true")  \
        .config("spark.executor.heartbeatInterval","300") \
        .config("spark.executor.memory","2g") \
        .config("spark.driver.maxResultSize","2g") \
        .config("spark.task.maxFailures","8")  \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.sql.sources.partitionOverwriteMode", "dynamic") \
        .config("hive.exec.dynamic.partition", "true") \
        .config("hive.exec.dynamic.partition.mode", "nonstrict") \
        .getOrCreate()

    # 结果数据
    data = sc.sql("""
            SELECT * FROM test limit 10;
    """)
    print(data)