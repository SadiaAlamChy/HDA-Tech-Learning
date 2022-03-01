from database.dbcon import PostgresConnection
import pandas as pd
class Query5:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query =  " SELECT t.year,s.division,SUM(f.total_price)" \
              " From ecomdb_star_schema.fact_table f " \
              " JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
              "JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key" \
              " Where t.year ='2015' and s.division='BARISAL'" \
              " GROUP BY ROLLUP(t.year,s.division) "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Year', 'Division','Total_Sales'])
        pd_data['Total_Sales'] = pd_data['Total_Sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q5 = Query5()
    data = q5.execute()
    print(data)