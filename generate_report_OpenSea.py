import requests
import openpyxl

wb = openpyxl.Workbook()
hoja = wb.active
hoja.title = "Assets Report"
# Crea la fila del encabezado con los títulos
# hoja.append(('Id', 'Name', 'Collection', 'Owner','Owner Wallet','Last Sale','Tocken Id','Contract Addres','Contract Name','Contract Owner'))
hoja.append(('Id','Collection','Owner Wallet','NFT Type'))
products= []
url = "https://testnets-api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&include_orders=false"
response = requests.get(url)
data = response.json()
# print(data['assets'])
if data['assets']:
    total_asset = len(data['assets'])
    print(total_asset)
    for asset in list(data['assets']):
        products.append((
        asset["id"],
        asset["collection"]["name"],
        # print("Owner: ", asset["owner"]
        # asset["owner"]["user"],
        asset["owner"]["address"],
        # asset['asset_contract']["address"],
        # asset['asset_contract']["name"],
        # asset['asset_contract']["owner"]
        ))
for producto in products:
    # producto es una tupla con los valores de un producto 
    hoja.append(producto)    
wb.save('productos.xlsx')