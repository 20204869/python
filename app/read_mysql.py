# -*- coding: utf-8 -*-
import pandas as pd
from pandas import DataFrame
from sqlalchemy import create_engine

if __name__ == '__main__':
    #mysql 配置
    engine = create_engine('mysql+pymysql://root:root@localhost:3306/demo')
    #sql查询
    sql_1 = f"""
        select * from person;
    """

    df_1 = pd.read_sql_query(sql_1,engine)

    result_data_1 = DataFrame.from_records(df_1)
    print(result_data_1)