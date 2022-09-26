import requests
import json
from rich.console import Console
from dotenv import load_dotenv
import os

console = Console()

# loads api token
load_dotenv() 
API_TOKEN = os.getenv('API_TOKEN')


from_currency = input('From what currency? ')
to_currency = input('To what currency? ')
value = input('How much do you want to exchange? ')

url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={value}"

payload = {}
headers = {
    "apikey": API_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

converted = response.json()['result']
console.print(
    f'[bold red]The exchange is:[/bold red] {converted} [bold cyan]{to_currency}[/bold cyan]')
