  
from ntpath import realpath
import dropbox
import os
from dropbox.files import WriteMode



class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token


    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f :
                    dbx.files_upload(f.read(),dropbox_path, mode=dropbox.files.WriteMode.overwrite)


def main():
        access_token = 'sl.A6SDHJ3ZoxlFVCy_7rKKgWRrAkn75LOesRYH-4M0m3tmqCQRsjxW9tnrTNXHXuCiC8gDfYcSipoAtkAAPVJJ6SnSvvyMgi3ZfHcI3xd06N-qPlOOueaj3E-sHaN3dwvFxOjPKzk'
        transferData = TransferData(access_token)

        file_from = str(input("Enter the file to transfer:"))
        file_to = "/BackUp101/" + (file_from)

    # API v2
        transferData.upload_file(file_from, file_to)
        print("File has been moved")

main()