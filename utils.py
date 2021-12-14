import requests


class User():

    def __init__(self, username, user_id, following_count):
        self.username = username
        self.user_id = user_id
        self.following_count = following_count


class Utils():

    # txt файл, где с каждой новой строки ссылка на акк твиттер
    def get_usernames_from_file(self, filename):
        usernames = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                # Вытаскиваем юзернейм из ссылки
                username = line.replace('\n','').strip().split(
                    'https://twitter.com/')[1].replace('/', '')
                usernames.append(username)
            f.close()
        return usernames

    def get_following(self, user_id, username):
        headers = {
            'authority': 'twitter.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'x-twitter-client-language': 'en',
            'x-csrf-token': '83aa68c1dff4a730ea9d7f5584d38fdab79f72ae319ede017e2cea4d3274db2c70e9b7f7d4c08668a328cf576cd2fedf76d27e1c5376818760b9ff5024bf247c6677007526d6a566f5da504fcfe65f73',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-active-user': 'yes',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://twitter.com/ALafoten/following',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'dnt=1; eu_cn=1; lang=en; kdt=t5j8Fx18a03BnfFGyxZoz9BEEq00xIkdEdqyIGyq; guest_id=v1%3A163870275609296645; g_state={"i_l":1,"i_p":1638709963073}; ads_prefs="HBESAAA="; auth_token=832c4bfc39da29b192ecfefbd63e24dfa43f29af; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFuITIp9AToMY3NyZl9p%250AZCIlNWQ3NTMzMjcwZDE2ZjRkYWQ1N2JmN2M2YWE4ZTYxZTA6B2lkIiVlMDMy%250AZmUwNWYwNjJlMWI4MTRjZTZmNTU3YzY3NjFkNQ%253D%253D--d357448e3746e09bf539e2cb1020353a909870fd; twid=u%3D1372829373171171329; ct0=83aa68c1dff4a730ea9d7f5584d38fdab79f72ae319ede017e2cea4d3274db2c70e9b7f7d4c08668a328cf576cd2fedf76d27e1c5376818760b9ff5024bf247c6677007526d6a566f5da504fcfe65f73; guest_id_marketing=v1%3A163870275609296645; guest_id_ads=v1%3A163870275609296645; personalization_id="v1_rxGMD/EhpYNNKsnDtZ7AIQ=="; _ga=GA1.2.1239908606.1639413156; _gid=GA1.2.1014108608.1639502982',
        }

        params = (
            ('variables', '{"userId":"'+str(user_id)+'","count":20,"withTweetQuoteCount":false,"includePromotedContent":false,"withSuperFollowsUserFields":true,"withUserResults":true,"withBirdwatchPivots":false,"withReactionsMetadata":false,"withReactionsPerspective":false,"withSuperFollowsTweetFields":true}'),
        )
        headers['referer'] = 'https://twitter.com/'+username+'/following'
        response = requests.get('https://twitter.com/i/api/graphql/pHK32L4uCgGxnMCfPoNIAw/Following',
            headers=headers, params=params)

        followings = response.json()['data']['user']['result']['timeline']['timeline']['instructions'][-1]['entries']
        return followings
