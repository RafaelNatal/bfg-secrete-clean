def get_user():
    return 'user_fixed'


def get_pass():
    return 'user_pass'


user = get_user()
passwd = get_pass()


if __name__ == "__main__":
    print("================================")
    print("Hello")
    print("================================")
    print(f'user: {user}')
    print(f'pass: {passwd}')
