import vk
import requests
import getpass

APP_ID = 6430213


def get_user_login():
    return input('Please, enter your login: ')


def get_user_password():
    return getpass.getpass('Please, enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session, v='5.35')
    friends_online = api.friends.getOnline()
    frinds_info = api.users.get(user_ids=friends_online)
    return frinds_info


def output_friends_to_console(friends_online):
    print('Hi, this is your friends who is currently online:')
    print('-'*40)
    for friend_online in friends_online:
        print(friend_online['first_name'], friend_online['last_name'])
    print('-'*40)

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
