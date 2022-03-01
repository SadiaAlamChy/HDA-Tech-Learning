from database.dbcon import PostgresConnection
import pandas as pd
class Query4:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query =  " SELECT t.year,SUM(f.total_price)" \
              " From ecomdb_star_schema.fact_table f " \
              "JOIN ecomdb_star_schema.time_dim t on t.time_key=f.time_key" \
              " Where t.year ='2015'" \
              " GROUP BY t.year "
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Year', 'Total_Sales'])
        pd_data['Total_Sales'] = pd_data['Total_Sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q4 = Query4()
    data = q4.execute()
    print(data)