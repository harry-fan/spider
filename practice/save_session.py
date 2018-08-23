# 保存session在本地

def save_session(session):
    with open("xxx.txt", wb) as f:
        cPickle.dump(session.headers, f)
        cPickle.dump(session.cookies.get_dice(), f)
        print('session 文件写入成功')

def load_session():
    with open('xxx.txt', 'rb') as f:
        headers = cPickle.load(f)
        cookies = cPickle.load(f)
        return headers, cookies
