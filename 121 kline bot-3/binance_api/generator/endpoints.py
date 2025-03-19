import requests
import csv
from bs4 import BeautifulSoup


for e in ('spot', 'futures', 'delivery'):
    endpoint_names = {}
    with open(f'{e}.csv', 'r') as csv_file:
        for row in csv.reader(csv_file):
            endpoint_names[row[0]] = (row[1], row[2])
    url = f'https://binance-docs.github.io/apidocs/{e}/en/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div.content')
    endpoints = []
    endpoint = {}
    all_types = []
    start = False
    for element in content[0]:
        html = str(element)
        html2 = html.replace('\n', '')
        if not start:
            if 'General Info' in html:
                start = True
            else:
                continue
        if '<p><code>GET' in html2 or '<p><code>POST' in html2 or '<p><code>DELETE' in html2 or '<p><code>PUT' in html2:
            if endpoint:
                endpoints.append(endpoint)
                endpoint = {}
            endpoint['method'] = html2.split(' ')[0].split('>')[-1].strip().lower()
            endpoint['url'] = html2[html2.index('/'):].split('<')[0].split('(')[0].strip()
        if '<th>Mandatory</th>' in html and 'params' not in endpoint:
            params = html.split('<tr>')
            endpoint['params'] = []
            if len(params) > 2:
                for param in params[2:]:
                    data = param.replace('\n', '').replace('</td>', '').replace(
                        '<td rowspan="2">', '<td>').split('<td>')
                    if len(data) > 2:
                        param_name = data[1]
                        if param_name == 'from':
                            param_name = '_from'
                        param_type = data[2].split('&')[0].upper()
                        if param_type not in all_types:
                            all_types.append(param_type)
                        param_mandatory = data[3] == 'YES'
                        if ' ' not in param_name and '[' not in param_name:
                            endpoint['params'].append((param_name, param_type, param_mandatory))
    endpoints_result = []
    with open(f'../endpoints/{e}.py', 'w') as file:
        file.write('class Endpoints:\n')
        for endpoint in endpoints:
            url_split = endpoint['url'].lower().split('/')
            endpoint0 = f"{endpoint['method']}-{'-'.join([url_split[1]] + url_split[3:])}"
            if not endpoint0 in endpoint_names:
                print(f'{e} endpoint {endpoint0} not found')
                continue
            endpoint_name = endpoint_names[endpoint0][0]
            signed = endpoint_names[endpoint0][1] == 'True'
            params_mandatory = []
            params_optional = []
            if endpoint['url'].endswith('/test'):
                for endpoint2 in endpoints:
                    if (endpoint2['url'] == endpoint['url'].replace('/test', '') and
                            endpoint2['method'] == endpoint['method']):
                        endpoint['params'] = endpoint2['params']
            if 'params' in endpoint:
                for param in endpoint['params']:
                    if not param[0]:
                        continue
                    if param[1] in ('LONG', 'INT', 'INTEGER'):
                        param_type = 'int'
                    elif param[1] in ('DECIMAL', 'BIGDECIMAL', 'DOUBLE'):
                        param_type = 'float'
                    elif param[1] == 'BOOLEAN':
                        param_type = 'bool'
                    elif param[1] == 'LIST':
                        param_type = 'list'
                    else:
                        param_type = 'str'
                    param_str = f'{param[0]}:{param_type}'
                    if param[2] and param[0] != 'timestamp':
                        params_mandatory.append(param_str)
                    else:
                        params_optional.append(param_str + ('=None' if param_type != 'bool' else '=False'))
            all_params = params_mandatory + params_optional
            args_str = ', '.join(all_params)
            if not args_str.startswith(',') and all_params:
                args_str = ', ' + args_str
            endpoints_result.append(endpoint_name)
            text = (f"    def {endpoint_name}(self{args_str}):\n        return self.request('{endpoint['method']}', "
                    f"'{endpoint['url']}', locals(){', sign=True' if signed else ''})\n\n")
            file.write(text)