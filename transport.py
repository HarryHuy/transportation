import csv
from lxml.etree import fromstring
import requests


INPUT_FILE = 'data/input.csv'
OUTPUT_FILE = 'data/output.csv'
INPUT_DATA = []
OUTPUT_DATA = []

with open(INPUT_FILE, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        INPUT_DATA.append(row)

INPUT_DATA[0].append('Package status')

OUTPUT_DATA.append(INPUT_DATA[0])

# print(OUTPUT_DATA)


class PackageStatusScraper:
    API_url = 'http://www.17track.net/restapi/handlertrack.ashx'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
        'Accept': '* / *',
        'Accept - Language': 'en - US, en;q = 0.5',
        'Accept - Encoding': 'gzip, deflate',
        'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'X - Requested - With': 'XMLHttpRequest'
    }

    def get_package_status(self, package):
        data = {
            'data': [{'num': package[1]}]
        }
        response = requests.post(self.API_url, json=data, headers=self.headers)
        returned_data = response.json()['dat'][0]['track']['e']
        return returned_data

    def run(self):
        for row in INPUT_DATA[1:5]:
            data = self.get_package_status(row)
            row.append(data)
            OUTPUT_DATA.append(row)
        # data = self.get_package_status('LS315575715CN')
        # print(data)


if __name__ == '__main__':
    scraper = PackageStatusScraper()
    scraper.run()
    # print(OUTPUT_DATA)
    with open(OUTPUT_FILE, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(OUTPUT_DATA)
