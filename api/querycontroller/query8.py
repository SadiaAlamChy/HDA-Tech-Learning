from database.dbcon import PostgresConnection
import pandas as pd
class Query8:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = "select i.item_name, tim.quarter, sum(f.total_price) " \
                "from ecomdb_star_schema.fact_table f " \
                "join ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                "join ecomdb_star_schema.time_dim tim on tim.time_key = f.time_key " \
                "group by i.item_name, tim.quarter " \
                "order by i.item_name, sum(f.total_price)"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item_name', 'Quarter','Total_Sales'])
        pd_data = pd_data.dropna()
        pd_data = pd_data.groupby('Item_name').head(1)
        pd_data = pd_data.set_index('Item_name')
        pd_data['Worst'] = pd_data['Quarter']
        pd_data=pd_data['Worst']
        return pd_data.to_dict()

if __name__ == '__main__':
    q8 = Query8()
    data = q8.execute()
    print(data)