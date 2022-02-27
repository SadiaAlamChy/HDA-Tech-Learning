from database.dbcon import PostgresConnection
import pandas as pd
class Query2:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = '''SELECT tt.trans_type,SUM(ft.total_price)
                    FROM ecomdb_star_schema.fact_table ft 
                    JOIN ecomdb_star_schema.item_dim i ON i.item_key=ft.item_key 
                    JOIN ecomdb_star_schema.trans_dim tt ON tt.payment_key=ft.payment_key 
                    JOIN ecomdb_star_schema.time_dim tim ON tim.time_key=ft.time_key
                    GROUP BY ROLLUP(trans_type);'''
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['trans_type', 'sum'])
        pd_data['sum'] = pd_data['sum'].astype('float64')
        pd_data = pd_data.dropna()
        print(pd_data)
        return pd_data.to_dict(orient='records')

if __name__ == '__main__':
    q2 = Query2()
    data2 = q2.execute()
    print(data2)