import json

import pymysql


def __init__(self):
    self.conn = pymysql.connect('47.96.111.237', 'damionew', '2018$mysql', 'nsh', charset="utf8", use_unicode=True)
    self.cursor = self.conn.cursor()

with open("./jsonpCallback21895.json",'r',encoding='utf8') as fp:
    json_data = json.load(fp)
    pageHelp = json_data['pageHelp']
    data = pageHelp['data']
    for dic in data:
        STAT_DATE = dic['STAT_DATE']
        ETF_TYPE = dic['ETF_TYPE']
        SEC_CODE = dic['SEC_CODE']
        NUM = dic['NUM']
        SEC_NAME = dic['SEC_NAME']
        TOT_VOL = dic['TOT_VOL']
        sql = 'insert into '
        print(dic)

