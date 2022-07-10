from filestack import Client

class FileSharer:
    def __init__(self, filepath , api_key='AoiR0ZinVQz6zrkDEaCCtz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        print(new_filelink)
        return new_filelink.url
