import random
import requests


headers = {
    'authority': 'twitter.com',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
    'x-twitter-client-language': 'en',
    'x-csrf-token': 'fb2e731a51b275a801045ee3eb7fd1ce2098930b3dff0dee044933cc7e29bb93f48ea8ea9665ccada7929b86a7d3fffa0305f5a9c8ab0d55b92f5225f925207948fcc878a569fce8ecf4555d4447f995',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'x-twitter-auth-type': 'OAuth2Session',
    'x-twitter-active-user': 'yes',
    'sec-ch-ua-platform': '"Windows"',
    'accept': '*/*',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'dnt=1; _ga=GA1.2.1722587588.1635589408; eu_cn=1; lang=en; kdt=t5j8Fx18a03BnfFGyxZoz9BEEq00xIkdEdqyIGyq; at_check=true; mbox=session#75f0572ba3754e0cb0ed57adeb04de58#1635601385|PC#75f0572ba3754e0cb0ed57adeb04de58.34_0#1698844326; guest_id_marketing=v1%3A163559789608820199; guest_id_ads=v1%3A163559789608820199; _gid=GA1.2.302288954.1637674218; _sl=1; gt=1465182958663438342; personalization_id="v1_gyns80gDuSFSd7v9DIrIIQ=="; guest_id=v1%3A163816328786703468; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCHEfJGp9AToMY3NyZl9p%250AZCIlMTczNTYxYzExMjZlZDRlOWUzYjI0YWQ3NGMyNDY0MzY6B2lkIiU0NmFj%250AZDYxMmE3ZTUxMjljMjI1MmRhODY2MjUzZWE3Ng%253D%253D--b7ece7bab1673d3a0a00b3ca91a84aaf95739c1c; g_state={"i_l":0}; auth_token=25a686a0985f1648f6165acc11112da873a95726; ct0=fb2e731a51b275a801045ee3eb7fd1ce2098930b3dff0dee044933cc7e29bb93f48ea8ea9665ccada7929b86a7d3fffa0305f5a9c8ab0d55b92f5225f925207948fcc878a569fce8ecf4555d4447f995; twid=u%3D1461980982861570049; att=1-pp84QqGkdRr9J652sO7iQJrmcEfKqfo9YoWXP9jR',
}

class Twitter_acc():

    def __init__(self):
        self.headers = {}
        # Тут может быть больше значений...

class Guest_acc():

	def __init__(self):
		self.headers = None
		self.update_guest_token_headers()

	def update_guest_token_headers(self):
		authorization = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
		headers = {
		    'authority': 'twitter.com',
		    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Microsoft Edge";v="96"',
		    'x-twitter-client-language': 'ru',
		    'sec-ch-ua-mobile': '?0',
		    'authorization': authorization,
		    'content-type': 'application/json',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41',
		    'x-twitter-active-user': 'yes',
		    'sec-ch-ua-platform': '"Windows"',
		    'accept': '*/*',
		    'origin': 'https://twitter.com',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-dest': 'empty',
		    'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
		}
		url = 'https://api.twitter.com/1.1/guest/activate.json'
		response = requests.post(url, headers=headers)
		guest_token = response.json()['guest_token']
		self.headers = {'authorization': authorization, 'x-guest-token': guest_token}


class Accounts():

    def __init__(self):
        self.working_accs = []
        self.banned_accs = []
        headers = {
            'authority': 'twitter.com',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'x-twitter-client-language': 'en',
            'x-csrf-token': '83aa68c1dff4a730ea9d7f5584d38fdab79f72ae319ede017e2cea4d3274db2c70e9b7f7d4c08668a328cf576cd2fedf76d27e1c5376818760b9ff5024bf247c6677007526d6a566f5da504fcfe65f73',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-active-user': 'yes',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': 'dnt=1; eu_cn=1; lang=en; kdt=t5j8Fx18a03BnfFGyxZoz9BEEq00xIkdEdqyIGyq; at_check=true; guest_id_marketing=v1%3A163559789608820199; guest_id_ads=v1%3A163559789608820199; mbox=PC#75f0572ba3754e0cb0ed57adeb04de58.37_0#1701790468|session#f66d8bb0bdc340b4b066b30dc0d51be0#1638547470; _ga_BYKEBDM7DS=GS1.1.1638545611.1.1.1638545671.0; _ga=GA1.2.1722587588.1635589408; personalization_id="v1_iIDP/x0ddP7Vofw9CnNf+A=="; guest_id=v1%3A163870275609296645; g_state={"i_l":1,"i_p":1638709963073}; _gid=GA1.2.233141241.1638789929; gt=1467944613138907144; ads_prefs="HBESAAA="; auth_token=832c4bfc39da29b192ecfefbd63e24dfa43f29af; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCFuITIp9AToMY3NyZl9p%250AZCIlNWQ3NTMzMjcwZDE2ZjRkYWQ1N2JmN2M2YWE4ZTYxZTA6B2lkIiVlMDMy%250AZmUwNWYwNjJlMWI4MTRjZTZmNTU3YzY3NjFkNQ%253D%253D--d357448e3746e09bf539e2cb1020353a909870fd; twid=u%3D1372829373171171329; ct0=83aa68c1dff4a730ea9d7f5584d38fdab79f72ae319ede017e2cea4d3274db2c70e9b7f7d4c08668a328cf576cd2fedf76d27e1c5376818760b9ff5024bf247c6677007526d6a566f5da504fcfe65f73',
        }
        self.add_acc(headers)
        #self.add_acc(headers)

    def add_acc(self, headers):
        acc = Twitter_acc()
        acc.headers = headers
        self.working_accs.append(acc)

    def mark_acc(self, acc):
        self.working_accs.remove(acc)
        self.banned_accs.append(acc)
        if len(self.working_accs) == 0:
            exit('No accs')

    def get_random_acc(self):
        acc = random.choice(self.working_accs)
        return acc

