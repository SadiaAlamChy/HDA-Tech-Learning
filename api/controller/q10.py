from db.postgres import PostgresConnection
import pandas as pd


class Query10:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select s.store_key, t.month, round(avg(f.total_price)::numeric,2) " \
                "from star_schema.fact_table f " \
                "join star_schema.store_dim s on s.store_key = f.store_key " \
                "join star_schema.time_dim t on t.time_key = f.time_key " \
                "group by s.store_key, t.month " \
                "order by s.store_key, t.month"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['Store', 'Month', 'Avg. Sales'])
        pd_data['Avg. Sales'] = pd_data['Avg. Sales'].astype('float64')
        return pd_data.to_dict(orient='records')


if __name__ == '__main__':
    q = Query10()
    data = q.execute()
