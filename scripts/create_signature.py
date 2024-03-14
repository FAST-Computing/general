import pandas as pd
import urllib.request

URL_ANAGRAFICA="https://raw.githubusercontent.com/FAST-Computing/general/main/anagrafica.csv"
URL_TEMPLATE_SIGNATURE="https://raw.githubusercontent.com/FAST-Computing/general/main/templates/signature.html"

# Download the file from `url` and save it locally under `file_name`:
response = urllib.request.urlopen(URL_TEMPLATE_SIGNATURE)
template_signature = response.read().decode('utf-8')

people = pd.read_csv(URL_ANAGRAFICA)
for index, person in people.iterrows():
    print(person)
    import copy
    current_signature = copy.deepcopy(template_signature)
    current_signature = current_signature.replace(r"{NAME}", person['NAME'])
    current_signature = current_signature.replace(r"{ROLE}", person['ROLE'])
    current_signature = current_signature.replace(r"{MAIL}", person['MAIL'])
    current_signature = current_signature.replace(r"{PHONE}", person['PHONE'])
    current_signature = current_signature.replace(r"{PICTURE}", person['PICTURE'])

    with open(f'signatures/{person["NAME"]}.html', 'w') as f:
        f.write(current_signature)
