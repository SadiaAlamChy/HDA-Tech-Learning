from api.database.dbcon import PostgresConnection
import pandas as pd
import datetime


class Query10:
    def __init__(self):
        # self.con = PostgresConnection.get_connection()
        print(" constructor called")

    def convert_number_to_month_name(self, month_num):
        datetime_object = datetime.datetime.strptime(month_num, "%m")
        # return datetime_object.strftime("%b") # for shorter name
        return datetime_object.strftime("%B")

    def formate_dictionary(self, Full_dict):
        final_list = []
        new_inner_dict = {"Sales": []}
        i = 1
        for one_dict in Full_dict:
            if i == 13:
                # print(new_iner_dict,'\n\n')
                final_list.append(new_inner_dict)
                new_inner_dict = {"Sales": []}
                i = 1

            if i == 1:
                new_inner_dict["Item"] = one_dict['Item']

            if i <= 12:
                new_inner_dict['Sales'].append({'Month': one_dict['Month_name'], 'Total Sales': one_dict['Total Sales']})

            i = i + 1

        return final_list

    def execute(self):
        select_stmt = "select i.item_name, t.month, sum(f.total_price) " \
                      "from ecomdb_star_schema.fact_table f " \
                      "join ecomdb_star_schema.item_dim i on i.item_key=f.item_key " \
                      "join ecomdb_star_schema.time_dim t on t.time_key = f.time_key " \
                      "group by i.item_name,t.month "

        records = PostgresConnection.retrive_data_from_table(select_stmt)
        df = pd.DataFrame(list(records), columns=['Item', 'Month', 'Total Sales'])

        df['Month_name'] = df['Month'].astype('str')
        df['Month_name'] = df['Month_name'].apply(lambda x: self.convert_number_to_month_name(x))
        df['Total Sales'] = df['Total Sales'].astype('float64')
        df.drop('Month', axis=1, inplace=True)

        data_dict = df.to_dict(orient='records') ## MAking Dictonary

        ## Call the function to make required formate
        arranged_dict = self.formate_dictionary(data_dict)
        return arranged_dict


