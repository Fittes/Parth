def get_views(url):
    views = []
    for i in range(1, 10):
        r = requests.get(f'{url}{i}/')
        if r.status_code != 404:
            soup = BeautifulSoup(r.text, 'html.parser')
            all_p = soup.find_all('span', {'class': 'tm-icon-counter__value'})
            text = ''

            for p in all_p:
                text = (p.text.strip() if len(p.text) >= 0 else "")
                if 'K' in text:
                    text = str(float(text[:-1]) * 1000)
                views.append(text)

    return views