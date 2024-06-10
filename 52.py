import zipfile
def creg_pw(passwpord_list, archive):
    a52=0
    with open(passwpord_list, 'rb') as file:
        for line in file:
            for word in line.split():
                try:
                    a52 += 1
                    archive.extractall(pwd=word)
                    print('', a52)
                    print('', word.decode())
                    return True
                except:
                    print(word.decode())
                    continue
        return False
password_list = 'rockyou.txt'
archive = input('введите название архива')
og = zipfile.ZipFile(archive)
homik = len(list(open(password_list, 'rb')))

if creg_pw(password_list, og) == False:
    print('v fale', password_list, 'ne nashel')
