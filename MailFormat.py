from GetNews import GetNews

class MailFormat:
    finalStr = ''

    def __init__(self):
        getNews = GetNews()
        newsStr = getNews.getNews()
        for i in newsStr:
            self.finalStr += '* '+i + '\n \n'

    def mailFormatter(self):
        return self.finalStr.encode('utf-8').strip()
