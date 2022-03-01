from database.dbcon import PostgresConnection
import pandas as pd
class Query3:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query =  "SELECT s.district, SUM(f.total_price)" \
                    "FROM ecomdb_star_schema.fact_table f " \
                    "JOIN ecomdb_star_schema.store_dim s on s.store_key = f.store_key " \
                    "WHERE s.district = 'BARISAL' " \
                    "GROUP BY s.district"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Division', 'Total_Sales'])
        pd_data['Total_Sales'] = pd_data['Total_Sales'].astype('float64')
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q3 = Query3()
    data = q3.execute()
    print(data)