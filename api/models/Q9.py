from api.database.dbcon import PostgresConnection
import pandas as pd


class Query9:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def formate_dictionary(self, Full_dict):
        final_list = []
        new_inner_dict = {"Sales": []}
        i = 1
        for one_dict in Full_dict:
            if i == 8:
                # print(new_iner_dict,'\n\n')
                final_list.append(new_inner_dict)
                new_inner_dict = {"Sales": []}
                i = 1

            if i == 1:
                new_inner_dict["Item"] = one_dict['Item']
                # new_inner_dict["Item"].append(one_dict['Item'])
            if i <= 7:
                new_inner_dict['Sales'].append({'Division': one_dict['Division'], 'Total Sales': one_dict['Total Sales']})
            i = i + 1

        return final_list

    def execute(self):
        select_stmt = "select i.item_name, s.division, sum(f.total_price) " \
                      "from ecomdb_star_schema.fact_table f " \
                      "join ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                      "join ecomdb_star_schema.store_dim s on s.store_key = f.store_key " \
                      "group by i.item_name, s.division "

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['Item', 'Division', 'Total Sales'])
        df['Total Sales'] = df['Total Sales'].astype('float64')
        data_dict = df.to_dict(orient='records')

        ## Call the function to make required formate
        arranged_dict = self. formate_dictionary(data_dict)
        return arranged_dict

