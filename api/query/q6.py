from api.database.dbcon import PostgresConnection
import pandas as pd
class Query6:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        select_top3 = "SELECT s.store_key, i.item_name, sum(f.quantity) " \
                      "FROM ecomdb_star_schema.fact_table f " \
                      "JOIN ecomdb_star_schema.store_dim s on s.store_key=f.store_key " \
                      "JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                      "GROUP by CUBE(s.store_key, i.item_name) " \
                      "ORDER by s.store_key, sum(f.quantity) DESC"
        cur.execute(select_top3)
        result = cur.fetchall()
        top3 = pd.DataFrame(list(result), columns=['store_id', 'item', 'quantity'])
        top3 = top3.dropna()
        top3 = top3.groupby('store_id').head(3)
        top3.pop('quantity')
        top3.set_index('store_id', inplace=True)
        # print(pd_data)
        return {top3.columns.get_loc('store_id'):top3['item'].to_list()}
       # return top3.to_dict(orient='records')

if __name__ == '__main__':
    q6 = Query6()
    data = q6.execute()
    print(data)