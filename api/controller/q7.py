import pandas as pd

from db.postgres import PostgresConnection


class Query7:
    def __init__(self, days):
        self.days = days
        self.con = PostgresConnection().get_connection()

    def execute(self):
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select i.item_name " \
                "from star_schema.fact_table f " \
                "join star_schema.trans_dim t on t.payment_key=f.payment_key " \
                "join star_schema.item_dim i on i.item_key=f.item_key " \
                "join star_schema.time_dim td on td.time_key = f.time_key " \
                "where (t.trans_type='card' or t.trans_type='mobile') and " \
                "td.t_date > (CURRENT_DATE - INTERVAL '{} days')".format(self.days)
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Items'])
        print(pd_data)
        return pd_data['Items'].to_dict()
