import ftplib

if __name__ == '__main__':
    ftp = ftplib.FTP('', timeout=10)
    ftp.login(user='', passwd='')

#ftp.mkd('data_ftp')
#переход в папку на сервере
ftp.cwd('data_ftp')
ftp.encoding = 'utf-8'

with open('local_data/file_transfer.txt', 'r', encoding=('utf-8')) as file:
    print(file.read())

with open('local_data/file_transfer.txt', 'rb') as file:
    ftp.storbinary('STOR ' + 'file_transfer.txt', file, 1024)