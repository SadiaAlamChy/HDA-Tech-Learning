from api.database.dbcon import PostgresConnection
import pandas as pd
class Query7:
    def __init__(self,data):
        self.data =data
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        #data=410
        #data = input('Enter days')
        con = PostgresConnection().getConnection()
        cur = con.cursor()
        s1 = "SELECT i.item_name, trans.trans_type "\
            "FROM ecomdb_star_schema.fact_table f "\
            "JOIN ecomdb_star_schema.trans_dim trans ON trans.payment_key=f.payment_key "\
            "JOIN ecomdb_star_schema.item_dim i ON i.item_key=f.item_key "\
            "JOIN ecomdb_star_schema.time_dim t ON t.time_key = f.time_key " \
            "Where (trans.trans_type='card' or trans.trans_type='mobile') and t.dates > (CURRENT_DATE - integer '{}')".format(self.data)
        cur.execute(s1)
        records_card = cur.fetchall()
        card = pd.DataFrame(list(records_card), columns=['item_name', 'trans_type'])
        #card = card.groupby('trans_type')
        # print(pd_data)
        return {"items": card['item_name'].to_list()}

if __name__ == '__main__':
    q7 = Query7()
    data = q7.execute()
    print(data)