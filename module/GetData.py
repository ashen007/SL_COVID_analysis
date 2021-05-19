import json
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup


def getter():
    return requests.get('https://www.hpb.health.gov.lk/api/get-current-statistical')


def dump_json(responds, path):
    if responds.status_code == 200:
        with open(path, 'w') as file:
            json.dump(responds.json(), file, sort_keys=True, indent=4)
    else:
        return responds.status_code


def get_daily_reports(page, path):
    base_url = page

    if isinstance(base_url, str):
        base_page = urlopen(base_url)
        html = base_page.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        host = 'https://www.epid.gov.lk'
        table = soup.tbody
        report_date = [trs.find_all('td')[0].text for trs in table.find_all('tr')[3:-2]]
        report_url_anchors = [trs.find_all('td')[3].a for trs in table.find_all('tr')[3:-2]]
        report_urls = [host + href['href'] for href in report_url_anchors]

        for i in range(len(report_urls)):
            sub_page = requests.get(report_urls[i])
            file_path = path + '/sitrep{file_name}.pdf'.format(file_name=report_date[i])

            with open(file_path, 'wb') as file:
                file.write(sub_page.content)

    else:
        print('url error')
