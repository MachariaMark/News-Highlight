class Headline  :
    """
    Headline class to define headline objects
    """

    def __init__(self,title,description,content,urlToImage,url,category,id):
        self.title = title
        self.description = description
        self.content = content
        self.urlToImage = urlToImage
        self.url = url
        self.category = category
        self.id = id

class Sources :
    """
    Sources class to define sources objects
    """

    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language 
        self.country = country

class Article:
    """
    Article class to define Article objects
    """

    def __init__(self,id,name,title,description,url,urlToImage,publishedAt,content):
        self.id = id
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt 
        self.content = content
