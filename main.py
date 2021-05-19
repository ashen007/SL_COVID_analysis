from module import GetData

if __name__ == '__main__':
    respond = GetData.getter()
    GetData.dump_json(respond, 'data/case_data.json')
    GetData.get_daily_reports(
        'https://www.epid.gov.lk/web/index.php?option=com_content&view=article&id=225&Itemid=518&lang=en',
        path='data/daily_report')
