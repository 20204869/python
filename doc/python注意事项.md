#####python实现查询spark sql并将查询结果写入excel 多sheet，发送到企业微信群
```
time ${SPARK_HOME}/bin/spark-submit --master yarn --deploy-mode client --executor-memory 2G sql2excel.py
```
#####企业微信访问API接口参考如下：
```
https://work.weixin.qq.com/api/doc/90000/90135/90248
SDK 参考：https://work.weixin.qq.com/api/doc/90000/90136/91770#%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%8E%A5%E5%8F%A3
```

####PS：执行存在问题记录
###1.spark 无法访问hive 配置信息
说明：spark 无法读取到hive-site.xml
解决方案有如下三种：
```
a.将hive-site.xml 复制到spark配置目录下
b.将hive-site.xml 放入项目内
c.提交执行命令时，指出hive-site.xml文件位置
```
####2.区分pandas.DataFrame 与spark DataFrame 
```
例如：copy()、to_excel 是pandas.DataFrame中方法，不是spark DataFrame方法，需将Spark DataFrame 转成pandas.DataFrame 才可使用。
```

###3.无法发送中文文件名
```
原因：files = {'file': open(path, 'rb')}
    r = requests.post(file_url, files=files) 中post方法不支持中文文件传输
解决方案：修改requests库所引用的urllib3库的源文件fields.py
修改内容如下：
    value = email.utils.encode_rfc2231(value, "utf-8")
    value = '%s*=%s' % (name, value)
更改为:注释掉
    #value = email.utils.encode_rfc2231(value, "utf-8")
    value = '%s="%s"' % (name, value)
```