def get_user(url):
    all_users = []
    for i in range(1, 10):
        r = requests.get(f'{url}{i}/')
        if r.status_code != 404:
            soup = BeautifulSoup(r.text, 'html.parser')
            all_p = soup.find_all('a', {'class': 'tm-user-info__username'})
            text = ''

            for p in all_p:
                text = (p.text.strip() if len(p.text) >= 0 else "")
                all_users.append(text)

    return all_users