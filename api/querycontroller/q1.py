
from flask import Flask, render_template, request, url_for, redirect
import os
import psycopg2
import pandas as pd


class PostgresConnection(object):
    def __init__(self):
        self.connection = psycopg2.connect(database="ecomdb",
                                           user="postgres",
                                           password="afra1234",
                                           host="127.0.0.1",
                                           port="5432")

    def getConnection(self):
        print("successfully connected to database")
        return self.connection


conn = PostgresConnection().getConnection()


class Query1:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "SELECT  s.division, SUM(t.total_price) " \
            "FROM ecom_schema.fact_table t " \
            "JOIN ecom_schema.store_dim s on s.store_key = t.store_key " \
            "GROUP BY CUBE(s.division)" \
            "ORDER BY s.division ASC"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['division', 'sales'])
        pd_data['sales'] = pd_data['sales'].astype('float64')
        pd_data = pd_data.dropna()
        ## get data pandas dataframe
        #print(pd_data) 
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q1 = Query1()
    data = q1.execute()
    print(data)
