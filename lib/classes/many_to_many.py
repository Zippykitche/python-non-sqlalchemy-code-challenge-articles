class Article:
    all = []
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise TypeError("Author must be an instance of the Author class.")

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if isinstance(value, Magazine):
            self._magazine = value
        else:
            raise TypeError("Magazine must be an instance of the Magazine class.")

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
    

        
class Author:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    def articles(self):
         return [article for article in Article.all if article.author == self]

    def magazines(self):
         return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)
    
    def topic_areas(self):
        if not self.articles():
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        articles = [article.title for article in Article.all if article.magazine == self]
        return articles if articles else None
    
    def contributing_authors(self):
        author_counts = {}
        for article in Article.all:
            if article.magazine == self:
                author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None