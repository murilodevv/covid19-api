import requests

class Covid19:
    
    def __init__(self, **kwargs) -> None:
        self.country = kwargs.get('country')
        self.date = kwargs.get('date')
        self.api_key = kwargs.get('api_key')

    def get_data(self):
        url = f"https://api.api-ninjas.com/v1/covid19?country={self.country}?date={self.date}"
        page = requests.request('GET', url, headers={f'X-Api-Key':f'{self.api_key}'})
        print(page.json())


if __name__ == '__main__':
    
    api_key = input("Enter your API Ninjas API key (api-ninjas.com): ")
    country = input("Enter your choice: ")
    date = input("Enter your choice (YYYY-MM-DD): ")

    covid19 = Covid19(country=country, date=date, api_key=api_key)
    covid19.get_data()

