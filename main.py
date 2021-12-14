from twitter_parser.twitter import Twitter_parser
from utils import Utils, User
import time
import telebot
from config import TOKEN, CHAT_ID, REPORT_CHAT_ID

utils = Utils()
parser = Twitter_parser()
bot = telebot.TeleBot(TOKEN)


class Monitoring():

    def __init__(self, usenames):
        self.users = []

        for usename in usenames:
            info = parser.account_from_username(usename, dict_view=False)
            following_count = info.following_count
            user_id = info.user_id
            user = User(usename, user_id, following_count)
            self.users.append(user)

    def monitor_users(self):
        for user in self.users:
            username = user.username
            user_id = user.user_id
            old_following_count = user.following_count

            new_following_count = parser.account_from_username(username,
                dict_view=False).following_count

            # Значит пользователль на кого-то подписался
            if new_following_count > old_following_count:
                # Сколько новых подписчиков
                offset = new_following_count - old_following_count
                followings = utils.get_following(user_id, username)
                # Обновляем кол-во подписок
                user.following_count = new_following_count

                new_followings = []
                for i in range(offset):
                    u = followings[i]['content']['itemContent']['user_results']['result']['legacy']['screen_name']
                    new_followings.append(u)

                users_string = '\n'.join(f'[{str(el)}](https://twitter.com/{str(el)})' for el in new_followings)
                message = f'У пользователя {username} {offset} новых подписок. Он подписался на:\n{users_string}'
                bot.send_message(CHAT_ID, text=message, parse_mode='Markdown', disable_web_page_preview=True)


usernames = utils.get_usernames_from_file('data/users.txt')
m = Monitoring(usernames)

while True:
    try:
        m.monitor_users()
    except Exception as ex:
        message = 'New error: '+str(ex)
        bot.send_message(REPORT_CHAT_ID, text=message)

    time.sleep(5)
