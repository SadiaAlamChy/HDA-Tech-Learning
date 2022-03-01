from database.dbcon import PostgresConnection
import pandas as pd
class Query7:
    def __init__(self,days):
        self.days = days
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        days = int(input('Enter no. of days for the query: '))
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        query = " SELECT i.item_name, tr.trans_type ,SUM(f.quantity) as Quantity" \
                " From ecomdb_star_schema.fact_table f " \
                " JOIN ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                " JOIN ecomdb_star_schema.time_dim tim on tim.time_key=f.time_key " \
                " JOIN ecomdb_star_schema.trans_dim tr on tr.payment_key=f.payment_key " \
                " Where (tr.trans_type = 'card' or tr.trans_type = 'mobile' or tr.trans_type = 'cash') " \
                " and tim.date > (CURRENT_DATE - integer '{}')" \
                " GROUP BY (i.item_name ,tr.trans_type)" \
                "Order by Quantity DESC ".format(days)
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Item_name','Trans_type','Total_Quantity'])
        pd_data['Total_Quantity'] = pd_data['Total_Quantity'].astype('int64')
        pd_data = pd_data.head(10)
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data.to_dict(orient='list')

if __name__ == '__main__':
    q7 = Query7()
    data = q7.execute()
    print(data)