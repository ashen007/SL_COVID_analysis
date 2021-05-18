import pprint
from module import GetData

if __name__ == '__main__':
    respond = GetData.getter()
    GetData.dump_json(respond, 'data/case_data.json')
