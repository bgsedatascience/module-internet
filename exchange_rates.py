import numpy as np
import pandas as pd
import requests
import json

def get_current_rates():
    import requests
    import json

    res = requests.get('https://api.exchangeratesapi.io/latest')
    rates = json.loads(res.content)

    return rates

def get_value_eur(path_to_file):
    import pandas as pd

    assets = pd.read_csv(path_to_file)

    rates = get_current_rates()
    rates = rates['rates']
    rates = pd.DataFrame.from_dict(rates, orient='index').reset_index()

    rates.columns = ['curr', 'fx']

    assets = pd.merge(assets, rates, how='left', on='curr')

    assets['value_eur'] = assets['value'] * assets['fx']
    assets.drop(['fx'], axis=1, inplace=True)

    return assets

new_assets = get_value_eur('assets.csv')


