import requests

class Brewery:
    def __init__(self, id: int, name: str, brewery_type: str, street: str, city: str, state: str, country: str,
                 phone: str, website_url: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.phone = phone
        self.website_url = website_url

    def __str__(self):
        return (f"Brewery ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Type: {self.brewery_type}\n"
                f"Street: {self.street}\n"
                f"City: {self.city}\n"
                f"State: {self.state}\n"
                f"Country: {self.country}\n"
                f"Phone: {self.phone}\n"
                f"Website: {self.website_url}\n")


def fetch_breweries(city=None):
    url = 'https://api.openbrewerydb.org/v1/breweries'
    params = {'per_page': 20}

    if city:
        params['by_city'] = city

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching breweries: {response.status_code}")
        return []


def function_zad7_8(city=None):
    breweries_data = fetch_breweries(city)
    breweries = []
    for brewery_data in breweries_data:
        brewery = Brewery(
            id=brewery_data.get('id'),
            name=brewery_data.get('name'),
            brewery_type=brewery_data.get('brewery_type'),
            street=brewery_data.get('street', 'N/A'),
            city=brewery_data.get('city', 'N/A'),
            state=brewery_data.get('state', 'N/A'),
            country=brewery_data.get('country', 'N/A'),
            phone=brewery_data.get('phone', 'N/A'),
            website_url=brewery_data.get('website_url', 'N/A')
        )
        breweries.append(brewery)

    for brewery in breweries:
        print(brewery)
        print('-' * 40)
