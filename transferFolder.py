import os
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                    
                local_path = os.path.join(root, filename)

                    
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = "oSIMcfs8yVQAAAAAAAAAAQ4Y0waoPfw_UO-DfPDksozMXJAkGe4_pJ4iF_ILqa7o"
    transferData = TransferData(access_token)
    file_from = input("enter the file path to transfer: ")
    file_to = input("enter the path to upload: ")
    transferData.upload_file(file_from, file_to)
    print("your file has been uploaded")

main()
    
    