import requests
from bs4 import BeautifulSoup, Tag


def get_html(url: str) -> str:
    headers = {
        'authority': 'vk.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=headers)
    return response.text


def get_posts(html: str) -> list[Tag]:
    soup = BeautifulSoup(html, 'html.parser')
    page_wall = soup.find('div', id='page_wall_posts')
    items = list(page_wall.find_all('div', class_='post'))
    return items


def main():
    html = get_html('https://vk.com/shvt')
    posts = get_posts(html)
    print(posts)


if __name__ == "__main__":
    main()
