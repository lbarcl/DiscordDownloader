import progress
import threading
import requests
import time
import os

class download:
    def __init__(self, files, path):
        self.files = files
        self.path = path
        self.session = requests.Session()

        for index, file in enumerate(self.files):
            #print(index, file.get('content_type'))
            if file.get('content_type') != None:
                fType = file.get('content_type').split('/')[0]
                file['content_type'] = fType
            
            f = file.get('filename')
            if 'unknown' in f:
                filename = f.replace('unknown', str(file.get('id')))
                file['filename'] = filename
            else:
                file['filename'] = str(file.get('id')) + '.' + f

            self.files[index] = file

    def Start(self):
        self.progress = progress.Bar(50, 'Download in process')
        self.download()

    def download(self):
        for index, file in enumerate(self.files):
            #print("Downloading file: " + file['filename'])
            try:
                Fbytes = self.session.get(file['url'])
            except:
                time.sleep(20)
                try:
                    Fbytes = self.session.get(file['url'])
                except:
                    continue
                
            if Fbytes.status_code != 200:
                print(Fbytes.content)
                continue
            bytes = Fbytes.content 

            SaveThread = threading.Thread(target=self.save, args=(file.get('content_type'), file.get('filename'), bytes))
            SaveThread.start()
            SaveThread.join()
            self.progress.print_percent_done(index, len(self.files))

        self.DownloadQue = None    

    def save(self, content_type, filename, bytes):
        if bytes == None:
            retur
        if content_type != None:
            if not os.path.exists(os.path.join(self.path, content_type)):
                os.makedirs(os.path.join(self.path, content_type))
            with open(os.path.join(self.path, content_type, filename), 'wb') as f:
                f.write(bytes)
                f.close()
        else:
            with open(os.path.join(self.path, filename), 'wb') as f:
                f.write(bytes)
                f.close()