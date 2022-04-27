import pandas as pd
import re
import os

# from wrapper.algorithms.stringmatching import name_matching, fuzzy_matching
# from wrapper.algorithms.stringmatching import PhoneticsMatiching
from stringmatching import name_matching,fuzzy_matching
from stringmatching import PhoneticsMatiching

DIV_THRESHOLD = 89.00
DIST_THRESHOLD = 79.00
UP_THRESHOLD = 79.00
UNION_THRESHOLD = 79.00
PARUSAVA_THRESHOLD = 80.00
MIN_THRESHOLD = 49.00
pd.set_option('mode.chained_assignment', None)

#### A list of join word
JOIN_WORDS = ['para', 'nagar', 'banglanagar', 'pur', 'gonj', 'bazar', 'akhra', 'bagicha', 'khali', 'gate', 'road']


class GeoMapper:
    def __init__(self):
        self.division_id = None
        self.division_name = None
        self.district_id = None
        self.district_name = None
        self.upazila_id = None
        self.upazila_name = None
        self.base_dir = os.path.dirname(os.path.realpath(__file__))
        self.phoneticsMatiching = PhoneticsMatiching()

    def setup(self):
        '''
        setup the geograhic master data
        :return: geographic dimension
        '''
        self.division = pd.read_csv(self.base_dir+ '/data/division.csv')
        self.district = pd.read_csv(self.base_dir + '/data/district.csv')
        self.upazila = pd.read_csv(self.base_dir + '/data/upazila.csv')
        self.union = pd.read_csv(self.base_dir + '/data/union_.csv')
        self.parusava = pd.read_csv(self.base_dir + '/data/parusava.csv')
        # self.dim_geo = pd.merge(self.upazila, self.district, how='inner', left_on=['district_id'], right_on=['district_id'])
        # self.dim_geo = pd.merge(self.dim_geo, self.division, how='inner', left_on=['division_id'], right_on=['division_id'])
        # self.dim_geo = self.dim_geo[['upazila_id', 'name_x', 'name_y', 'name']]
        # self.dim_geo.columns = ['geo_key', 'upazila', 'district', 'division']



    def preprocessing(self, address):
        '''
        Cleaning, stopward removing, tokenization
        :param address: raw
        :return: list of word
        '''
        address = str(address).strip()
        address = re.sub(r'[0-9]+|[-()\"#/@;:<>{}`+=~|.!?,]', ' ', address)
        addr1_list = address.split(' ')
        address_list = list(filter(None, addr1_list))
        ### Join two word based on JOIN_WORDS. e.g. Mugda + para = Mugdapara
        l = len(address_list)-1
        for i in range(0, len(address_list)):
            # print(address_list[i])
            if(address_list[i].lower() in JOIN_WORDS and i>0):
                # print(address_list[i])
                address_list[i-1] = address_list[i-1] + address_list[i]
                address_list[i] = address_list[l]
                address_list[l] = ' '
                l-=1
                i-=1
        # end of word joining
        return [x for x in address_list if x is not len(x) > 3]  ### Remove the small word (less then 3 letter)

    def adjust_query_input(self, dict_, x, THRESHOLD):
        '''
        Remove the matched element from the list x
        :param dict_: ditionary
        :param x: list
        :param THRESHOLD: DIV/DIST/UP
        :return: list
        '''
        if(dict_ and self.is_above_thereshold(dict_['confidence'], THRESHOLD)):
            x.remove(dict_['matched_word'])
            return x
        else:
            return x

    def scoring_matrix(self, df, address_list):
        '''
        Constract a matrix based on the soundex score (0 or 1) and calculate the row wise max score
        Row contain a document (e.g for division-> Dhaka is a row of a matrix) which matches with the list of the query doc (address_list)
        :param df: Documents (Query space)
        :param address_list: Query
        :return: A matrix (dataframe) with score
        '''
        for addr in address_list:
            # print(addr)
            df[addr] = df.apply(lambda x: fuzzy_matching(str(x['name']), str(addr)), axis=1)
            # df[addr] = df.apply(lambda x: self.phoneticsMatiching.test(x['name'], addr), axis=1)
        df["max_score"] = df[address_list].max(axis=1)
        return df


    def similarity_query(self, addr_lst, docs, type, threshold = MIN_THRESHOLD):
        '''
        Get the matched doc from the documents dataframe
        :param addr_lst: list of the words in the address
        :param docs: query sapce
        :param type: division/district/upazila/union/parusava
        :return: type, which_word, type_id, type_name, confidence
        '''
        if(len(addr_lst)):
            id = type+'_id'
            df = self.scoring_matrix(docs[[id, 'name']], addr_lst)
            # print(df)
            selected_df = df.iloc[df["max_score"].idxmax()]
            # print(selected_df)
            if (selected_df['max_score'] > threshold):
                which_word = None
                for addr in addr_lst:
                    if(selected_df[addr] == selected_df['max_score']): # Get the max scored query word
                        which_word = addr
                id, name, confidence = selected_df[id], selected_df['name'], selected_df['max_score']
                return {'type': type, 'matched_word': which_word, 'geocode': id, 'name': name, 'confidence': confidence }
            del df
        return False


    def get_division_from_geocode(self, geokey):
        # print(geokey, type(geokey))
        id = str(geokey)[:2] ### First two digit of the geokey is div id
        # print(self.division.dtypes)
        # print(self.division.loc[self.division["division_id"] == int(id)])
        return self.division.loc[self.division["division_id"] == int(id)]['name'].values[0]

    def get_district_from_geocode(self, geokey):
        # print(geokey, type(geokey))
        id = str(geokey)[:4] ### First two digit of the geokey is div id
        # print(self.division.dtypes)
        # print(self.division.loc[self.division["division_id"] == int(id)])
        return self.district.loc[self.district["district_id"] == int(id)]['name'].values[0]

    def get_upazila_from_geocode(self, geokey):
        # print(geokey, type(geokey))
        id = str(geokey)[:6] ### First two digit of the geokey is div id
        # self.upazila['upazila_id'] = self.upazila.upazila_id.astype(int)
        return self.upazila.loc[self.upazila["upazila_id"] == int(id)]['name'].values[0]

    def get_districts_by_div(self, div_id):
        '''
        Filter district dataframe by div id and return the district df
        :param div_id: division id
        :return: district df
        '''
        return self.district.loc[self.district['division_id'] == div_id]

    def get_upazilas_by_dist(self, dist_id):
        '''
        Filter upazila dataframe by dist id and return the upazila df
        :param dist_id: district id
        :return: upazila df
        '''
        return self.upazila.loc[self.upazila['district_id'] == dist_id]

    def get_unions_by_dist(self, dist_id):
        '''
        Filter union dataframe by dist id and return the union df
        :param div_id: division id
        :return: union df
        '''
        # upazila = self.get_upazilas_by_dist(dist_id)
        self.union['union_id'] = self.union.union_id.astype(str)
        filtered =  self.union[self.union['union_id'].str.startswith(str(dist_id))]
        self.union['union_id'] = self.union.union_id.astype(int)
        return filtered

    def get_upazilas_by_div(self, div_id):
        '''
        Filter upazila dataframe by division id and return the upazila df
        :param div_id: division id
        :return: upazila df
        '''
        # upazila = self.get_upazilas_by_dist(dist_id)
        self.upazila['upazila_id'] = self.upazila.upazila_id.astype(str)
        filtered = self.upazila[self.upazila['upazila_id'].str.startswith(str(div_id))]
        self.upazila['upazila_id'] = self.upazila.upazila_id.astype(int)
        return filtered

    def get_unions_by_div(self, div_id):
        '''
        Filter union dataframe by division id and return the union df
        :param div_id: division id
        :return: union df
        '''
        # upazila = self.get_upazilas_by_dist(dist_id)
        self.union['union_id'] = self.union.union_id.astype(str)
        filtered = self.union[self.union['union_id'].str.startswith(str(div_id))]
        self.union['union_id'] = self.union.union_id.astype(int)
        return filtered

    def is_above_thereshold(self, confidence, thresholds):
        '''
        :param confidence: Matching ratio
        :param thresholds: Fixed
        :return: Boolean
        '''
        return confidence >= thresholds

    def is_satisfy_hierarchy(self, upper, lower):
        '''
        Hierarchy: DIVISION->DISTRICT->UPAZILA
        :param upper:  geocode
        :param lower:  geocode
        :return: Boolean
        '''
        common_len = len(str(upper))
        return (str(upper) == str(lower)[:common_len])



    def case1_matching_scenario(self, upazila, district, division):
        '''
        Any of two confidence greater than THRESHOLD and satifsy hierarchy or the case only upazila above the threshold
        Target-> Upazila Level
        :param upazila: ['upazila', which_word, upazila_id, upazila_name, confidence]
        :param district: ['district', which_word, district_id, district_id, confidence]
        :param div: ['division', which_word, division_id, division_name, confidence]
        :return: boolean
        '''
        if(upazila and district): # Up and Dist matched and satisfy threshold
            if(self.is_above_thereshold(upazila['confidence'], UP_THRESHOLD) and
                    self.is_above_thereshold(district['confidence'], DIST_THRESHOLD) and
                        self.is_satisfy_hierarchy(district['geocode'], upazila['geocode'])):
                return True
            else: pass
        if (upazila and division): # Up and Div matched and satisfy threshold
            if (self.is_above_thereshold(upazila['confidence'], UP_THRESHOLD) and
                    self.is_above_thereshold(division['confidence'], DIV_THRESHOLD) and
                    self.is_satisfy_hierarchy(division['geocode'], upazila['geocode'])):
                return True
            else: pass
        if (upazila and district and division):  # UP matching threshold statisfy but other not
            if (self.is_above_thereshold(upazila['confidence'], UP_THRESHOLD) and
                    not self.is_above_thereshold(district['confidence'], DIST_THRESHOLD) and
                        not self.is_above_thereshold(division['confidence'], DIV_THRESHOLD)):
                return True
            else:
                pass
        if (upazila and district and not division): # UP and DIST mactched and UP matching threshold statisfy but other not
            if (self.is_above_thereshold(upazila['confidence'], UP_THRESHOLD) and
                    not self.is_above_thereshold(district['confidence'], DIST_THRESHOLD)):
                return True
            else:
                pass
        if (upazila and division and not district): # UP and DIV mactched and UP matching threshold statisfy but other not
            if (self.is_above_thereshold(upazila['confidence'], UP_THRESHOLD) and
                    not self.is_above_thereshold(division['confidence'], DIV_THRESHOLD)):
                return True
            else:
                pass
        if (upazila and not division and not district): # Only UP matched
            return True
        return False

    def case2_matching_scenario(self, district):
        '''
        Only matched District above the threshold
        Target-> District
        :param district: ['district', which_word, district_id, district_id, confidence]
        :return: Boolean
        '''
        if(district):
            if(self.is_above_thereshold(district['confidence'], DIST_THRESHOLD)):
                return True
            else: return False
        return False

    def case3_matching_scenario(self, division):
        '''
        Only matched Division above the threshold
        Target-> Division
        :param div: ['division', which_word, division_id, division_name, confidence]
        :return: Boolean
        '''
        if(division):
            if(self.is_above_thereshold(division['confidence'], DIV_THRESHOLD)):
                return True
            else: return False
        return False

    def upazila_or_union(self, up, union):
        if (up and union):
            if (up['confidence'] >= union['confidence']):
                # print('case2: ', up['geocode'], up['name'], dist['name'], self.get_division_from_geocode(up['geocode']))
                return up['geocode'], up['name'], self.get_division_from_geocode(up['geocode']), self.get_division_from_geocode(up['geocode'])
            else:
                geocode = union['geocode'][:6]
                # print('case2:union- ', geocode, self.get_upazila_from_geocode(geocode), self.get_district_from_geocode(geocode), self.get_division_from_geocode(geocode))
                return int(geocode), self.get_upazila_from_geocode(geocode), self.get_district_from_geocode(
                    geocode), self.get_division_from_geocode(geocode)
        if (union):
            geocode = union['geocode'][:6]
            # print(geocode)
            # print('case2:union- ', geocode, self.get_upazila_from_geocode(geocode),
            #       self.get_district_from_geocode(geocode), self.get_division_from_geocode(geocode))
            return int(geocode), self.get_upazila_from_geocode(geocode), self.get_district_from_geocode(
                geocode), self.get_division_from_geocode(geocode)
        if (up):
            # print('case2: ', up['geocode'], up['name'], dist['name'],
            #       self.get_division_from_geocode(up['geocode']))
            return up['geocode'], up['name'], self.get_division_from_geocode(up['geocode']), self.get_division_from_geocode(up['geocode'])
        return False

    def get_geo_hierarchy(self, address):
        '''
        A bottomup approch to get the geocode from the address (upazila level and above)
        :param address: Raw
        :return: 6-digit geocode (302612 -> 30: div code, 3026: dsitrict code, 302612: upazila code), upazila_name, district_name, division_name
        '''
        # print(address)
        geo_key, division, district, upazila = None, None, None, None # Initialization
        if (address and address!='nan'):
            #### Preprocessing
            cleaned_list = self.preprocessing(address=address)
            # print('####', cleaned_list)
            if (cleaned_list):
                temp = cleaned_list[:] ## Copy to temp
                div = self.similarity_query(addr_lst=temp,
                                            docs=self.division,
                                            type='division') # Get matched division
                #### Remove the matched word (with division) from the query input
                # adjust_list = self.adjust_query_input(dict_=div, x=temp, THRESHOLD=DIV_THRESHOLD)
                dist = self.similarity_query(addr_lst=temp,
                                             docs=self.district,
                                             type='district') # Get matched district
                #### Remove the matched word (with district) from the query input
                adjust_list = self.adjust_query_input(dict_=dist, x=temp, THRESHOLD=DIST_THRESHOLD)
                up = self.similarity_query(addr_lst=adjust_list,
                                           docs=self.upazila,
                                           type='upazila') ## return [type, which_word, id, name, confidence]
                # Best matching scenario #
                if(self.case1_matching_scenario(upazila=up, district=dist, division=div)):
                    # print('case1: ', up['geocode'], up['name'], self.get_district_from_geocode(up['geocode']), self.get_division_from_geocode(up['geocode']))
                    return up['geocode'], up['name'], self.get_district_from_geocode(up['geocode']), self.get_division_from_geocode(up['geocode'])
                del temp
                temp = cleaned_list[:] ### Back the original query input list
                ## 2nd scenario ###
                if(self.case2_matching_scenario(district=dist)):
                    del up # remove previous upazila dictionary
                    adjust_list = self.adjust_query_input(dict_=dist, x=temp, THRESHOLD=DIST_THRESHOLD)
                    up_query_space = self.get_upazilas_by_dist(dist_id=dist['geocode']).reset_index(drop=True)
                    up = self.similarity_query(addr_lst=adjust_list,
                                               docs= up_query_space,
                                               type='upazila',
                                               threshold=30)  ## return [type, which_word, id, name, confidence]
                    # print(up)
                    union_query_space = self.get_unions_by_dist(dist_id=dist['geocode']).reset_index(drop=True)
                    union = self.similarity_query(addr_lst=adjust_list,
                                               docs=union_query_space,
                                               type='union',
                                               threshold=30)  ## return [type, which_word, id, name, confidence]
                    # print(union)
                    #### Get the max matched result from union and upazila match
                    up_or_union = self.upazila_or_union(up, union)
                    if(up_or_union): return up_or_union
                    else:
                        upazila_id = str(up_query_space.iloc[0]['upazila_id']) # get the first upazila of this district
                        return upazila_id, self.get_upazila_from_geocode(geokey=upazila_id), \
                               dist['name'], self.get_division_from_geocode(geokey=upazila_id)
                    # if(dist['confidence'])
                ## 3nd but not last scenario ###
                del temp
                temp = cleaned_list[:]  ### Back the original query input list
                if (self.case3_matching_scenario(division=div)):
                    # print(cleaned_list)
                    del up # remove previous upazila and district dictionary
                    adjust_list = self.adjust_query_input(dict_=div, x=temp, THRESHOLD=DIST_THRESHOLD) # Remove matched div from query
                    up_query_space = self.get_upazilas_by_div(div['geocode']).reset_index(drop=True)
                    union_query_space = self.get_unions_by_div(div['geocode']).reset_index(drop=True)
                    up = self.similarity_query(addr_lst=adjust_list,
                                                 docs=up_query_space,
                                                 type='upazila')  # Get matched district
                    union = self.similarity_query(addr_lst=adjust_list,
                                                  docs=union_query_space,
                                                  type='union')  ## return [type, which_word, id, name, confidence]
                    # print(up)
                    # print(union)
                    #### Get the max matched result from union and upazila match
                    up_or_union = self.upazila_or_union(up, union)
                    # print(up_or_union)
                    if (up_or_union): return up_or_union
                    else:
                        # SPECIAL CASE
                        if(div['name'] == 'DHAKA'): ## If the division DHAKA-> Randomly select from DHAKA City
                            up_query_space = self.get_upazilas_by_dist(3026).reset_index(drop=True) # Geocode of DHAKA District-> 3026
                            upazila_id = str(up_query_space.sample(n=1)['upazila_id'].values[0])
                            return upazila_id, self.get_upazila_from_geocode(geokey=upazila_id), 'DHAKA', div['name']
                        upazila_id = str(up_query_space.iloc[0]['upazila_id']) # Select the most populate area from the upazila
                        return upazila_id, self.get_upazila_from_geocode(geokey=upazila_id), \
                               self.get_district_from_geocode(geokey=upazila_id), \
                               div['name']
        #### Address is empty or not statisfy any case of matching

        ### Return Hospital Geo Location as the Patient Address
        return geo_key, division, district, upazila

if __name__ == '__main__':
    g = GeoMapper()
    g.setup()
    # print(g.get_unions_by_dist('3026'))
    geo = g.get_geo_hierarchy(address="NORSINGPUR, ZIRABO , ASHULIA. SAVAR")
    print(geo)
    # import pandas as pd
    # df = pd.read_csv('C:/Users/Administrator/HDA Intern/Prescription-Data-integration-master/wrapper/dataset/anonymized_prescription_dataset_mysoft.csv')
    # # print(df.columns)
    # ad = df.ADDRESS
    # add = []
    # n = 2
    # for i in range(9100):
    #     g = GeoMapper()
    #     g.setup()
    #     # print(g.get_unions_by_dist('3026'))
    #     geo = g.get_geo_hierarchy(address=ad[i])
    #     print(geo,":    :",ad[i],"    : ",n)
    #     n=n+1
    #     add.append(geo)
    # ad.head()
    # # print(add_csv)
    # address_data = pd.DataFrame(list(add), columns=['Geocode','Upazial','Division','District'])
    # # print(address_data)
    # address_data.to_dict(orient='records')
    # # print(address_data)
    # address_data.to_csv('constructed.csv',index=False)
    # #
