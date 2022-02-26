from db.postgres import PostgresConnection


class Query3:
    def __init__(self):
        self.con = PostgresConnection().get_connection()

    @staticmethod
    def execute():
        con = PostgresConnection().get_connection()
        cur = con.cursor()
        query = "select sum(t.total_price) " \
                "from star_schema.fact_table t " \
                "join star_schema.store_dim s on s.store_key=t.store_key where s.division='BARISAL'"
        cur.execute(query)
        result = cur.fetchall()[0][0]
        return {"total": result}


if __name__ == '__main__':
    q = Query3()
    data = q.execute()
