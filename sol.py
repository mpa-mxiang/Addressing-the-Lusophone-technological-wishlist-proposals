import requests
import csv

input_file = 'Task 2 - Intern.csv'

def get_status_code(url):
    try:
        response = requests.head(url)
        return response.status_code
    except requests.ConnectionError:
        return "Connection Error"
    except requests.Timeout:
        return "Timeout Error"
    except requests.RequestException:
        return "Request Error"

with open(input_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader, None)
    
    for row in csv_reader:
        url = row[0]
        status_code = get_status_code(url)
        
        print(f"({status_code}) {url}")
