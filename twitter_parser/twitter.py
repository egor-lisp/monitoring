import requests
from datetime import datetime
from twitter_parser.twit_manage import Accounts
from twitter_parser.twitter_api import Twitter_api


class Profile():

    def __init__(self):
        self.status = 'active' # active/suspended/missing
        self.url = None
        self.site_url = None
        self.user_id = None
        self.is_ava = None
        self.ava_url = None
        self.created_time = None
        self.description = None
        self.followers_count = None
        self.following_count = None
        self.posts_count = None

class Post():

    def __init__(self):
        self.url = None
        self.creator_url = None
        self.created_time = None
        self.likes_count = None
        self.retweet_count = None
        self.comment_count = None
        self.text = None
        self.hashtags = []
        self.is_picture = None
        self.is_retweet = None
        self.is_quote = None
        self.quote_post_url = ''


class Twitter_parser():

    def __init__(self):
        self.acc_manager = Accounts()
        self.api = Twitter_api()
        self.update_session()

    def update_session(self):
        # Устаанавливаем кукисы для запросов
        self.account = self.acc_manager.get_random_acc()
        self.headers = self.account.headers

    def dict_from_class(self, class_):
        data = {}
        elems = class_.__dict__.keys()
        for elem in elems:
            data[elem] = class_.__dict__[elem]

        return data

    def to_iso(self, time_str):
        'Tue Jan 02 03:44:34 +0000 2018'
        date = datetime.strptime(time_str, '%a %b %d %H:%M:%S +0000 %Y')
        return date.isoformat()

    def post_id_by_url(self, url):
        post_id = url.split('/status/')[1].replace('/', '')
        return post_id

    # Возвращает True, если ответ правильный, и False если нет
    def check_response_valid(self, response):
        return_info = True
        if response.text == '' or response.status_code != 200:
            return_info = False
        return return_info

    def smart_get_request(self, url, params):
        while True:
            response = requests.get(
                url,
                headers=self.headers, params=params)

            if not self.check_response_valid(response):
                self.acc_manager.mark_acc(self.account)
                self.update_session()
            else:
                return response

    def account_from_username(self, username, dict_view=True):
        # Класс профиля (см. выше)
        profile = Profile()

        # Параметры
        params = self.api.get_profile_info_params(username)

        response = self.smart_get_request(self.api.profile_info_url,
            params=params)
        json = response.json()

        # Проверяем, удален ли профиль
        if not json['data']:
            profile.status = 'missing'
            return self.dict_from_class(profile)

        user = json['data']['user']['result']
        if user['__typename'] == 'UserUnavailable':
            profile.status = 'suspended'
            return self.dict_from_class(profile)
        else:
            user = user['legacy']

        profile.url = 'https://twitter.com/'+username
        profile.user_id = json['data']['user']['result']['rest_id']
        profile.is_ava = not user['default_profile_image']
        profile.ava_url = user['profile_image_url_https']
        profile.created_time = self.to_iso(user['created_at'])
        profile.description = user['description']
        profile.followers_count = user['followers_count']
        profile.following_count = user['friends_count']
        profile.posts_count = user['statuses_count']

        # Ссылка на сайт
        profile.site_url = ''
        entities = user['entities']
        if 'url' in entities.keys():
            url = entities['url']['urls'][0]['expanded_url']
            profile.site_url = url

        if dict_view:
            profile = self.dict_from_class(profile)

        return profile

    def get_post_info(self, url, dict_view=True):
        post = Post()
        
        post_id = self.post_id_by_url(url)
        params = self.api.get_post_info_params(post_id)

        response = self.smart_get_request(self.api.post_info_url,
            params=params)
        json = response.json()

        block_info = json['data']['threaded_conversation_with_injections']['instructions'][0]['entries'][0]['content']['itemContent']['tweet_results']['result']
        content = block_info['legacy']

        username = block_info['core']['user_results']['result']['legacy']['screen_name']

        post.url = 'https://twitter.com/'+username+'/status/'+str(post_id)
        post.creator_url = 'https://twitter.com/'+username
        post.created_time = self.to_iso(content['created_at'])
        post.likes_count = content['favorite_count']
        post.retweet_count = content['retweet_count']
        post.comment_count = content['reply_count']
        post.text = content['full_text']
        post.is_quote = content['is_quote_status']
        if post.is_quote:
            post.quote_post_url = content['quoted_status_permalink']['expanded']

        # Хэштеги
        for h in content['entities']['hashtags']:
            post.hashtags.append(h['text'])

        # Проверяем, есть ли картника
        post.is_picture = False
        if 'media' in content['entities'].keys():
            if len(content['entities']['media']) > 0:
                post.is_picture = True

        # Проверяем, ретвит или нет
        post.is_retweet = False
        if 'retweeted_status_result' in content.keys():
            post.is_retweet = True

        if dict_view:
            post = self.dict_from_class(post)
        
        return post

    def get_posts(self, user_id, max_count=100, dict_view=True):
        # Список постов
        posts = []
        work = True
        cursor = None
        username = None

        while work:
            # Параметры
            params = self.api.get_posts_params(user_id, cursor=cursor)

            # Делаем запрос
            response = self.smart_get_request(self.api.posts_url,
                params=params)
            json = response.json()

            piece_posts = json['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']
            cursor = piece_posts[-1]['content']['value']

            if len(piece_posts) <= 2:
                work = False

            for post in piece_posts:
                publication = Post()

                if 'tweet' in post['entryId']:
                    try:
                        info_block = post['content']['itemContent']['tweet_results']['result']
                        content = info_block['legacy']
                    except:
                        continue

                    if not username:
                        username = info_block['core']['user_results']['result']['legacy']['screen_name']

                    publication.url = 'https://twitter.com/' + username + '/status/' + content['id_str']
                    publication.creator_url = 'https://twitter.com/' + username
                    publication.created_time = self.to_iso(content['created_at'])
                    publication.likes_count = content['favorite_count']
                    publication.retweet_count = content['retweet_count']
                    publication.comment_count = content['reply_count']
                    publication.text = content['full_text']
                    publication.is_quote = content['is_quote_status']
                    if publication.is_quote:
                        publication.quote_post_url = content['quoted_status_permalink']['expanded']

                    # Хэштеги
                    for h in content['entities']['hashtags']:
                        publication.hashtags.append(h['text'])

                    # Проверяем, есть ли картника
                    publication.is_picture = False
                    if 'media' in content['entities'].keys():
                        if len(content['entities']['media']) > 0:
                            publication.is_picture = True

                    # Проверяем, ретвит или нет
                    publication.is_retweet = False
                    if 'retweeted_status_result' in content.keys():
                        publication.is_retweet = True

                    if dict_view:
                        publication = self.dict_from_class(publication)

                    posts.append(publication)

                    if len(posts) >= max_count:
                        work = False
                        break

        return posts

    def retrieve_by_username(self, username, max_count=100):
        data = {'user': None, 'posts': None}

        user_info = self.account_from_username(username, dict_view=True)
        data['user'] = user_info
        if user_info['status'] == 'missing' or user_info['status'] == 'suspended':
            return data

        data['posts'] = self.get_posts(
            data['user']['user_id'],
            max_count=max_count, dict_view=True)

        return data
