import requests
from bs4 import BeautifulSoup

def fetch_india_trends_trends24():
    url = "https://trends24.in/india/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to retrieve data: Status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # On inspection, trending topics are inside <ol class="trend-card__list"> as <li> elements
    ol = soup.find('ol', class_='trend-card__list')
    if not ol:
        print("Couldn't find the trends list on the page.")
        return []

    trends = []
    for li in ol.find_all('li')[:5]:
        trend_text = li.get_text(strip=True)
        trends.append(trend_text)

    return trends

if __name__ == "__main__":
    top_trends = fetch_india_trends_trends24()
    if top_trends:
        print("Top 5 Twitter Trending Topics in India (from trends24.in):")
        for i, trend in enumerate(top_trends, 1):
            print(f"{i}. {trend}")
    else:
        print("No trends found.")

