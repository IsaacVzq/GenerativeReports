import requests
import openpyxl
import os
import smtplib
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
#Env Variables
load_dotenv()
# Email Sent
SENDER_EMAIL = str(os.environ.get('SENDER_EMAIL'))
APP_PASSWORD = str(os.environ.get('PASSWORD_EMAIL'))
RECIVER_EMAIL =str(os.environ.get('RECIVER_EMAIL')) 

def send_mail_with_excel(recipient_email, subject, content, excel_file):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content(content)

    with open(excel_file, 'rb') as f:
        file_data = f.read()
    msg.add_attachment(file_data, maintype="application", subtype="xlsx", filename=excel_file)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

EXCEL_FILE_NAME = 'ReportAssets.xlsx'



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
    print("Assets Evaluated: ", total_asset)
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
wb.save(EXCEL_FILE_NAME)



subject = 'OpenSea Owership Report '
to = RECIVER_EMAIL

body = 'Email Automatizado no responder\n\n'
print(SENDER_EMAIL,APP_PASSWORD)
try:
    send_mail_with_excel(to,subject,body,EXCEL_FILE_NAME)
    print ("Report was send successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)
        
        
