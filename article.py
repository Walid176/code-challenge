class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []   

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            print("Name must be a string with more than zero chars.")

    def articles(self):
        return self._articles  

    def magazines(self):
       
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
       
        article = Article(self, magazine, title)
        self._articles.append(article)
        magazine._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            print("Name must be a string between 2 and 16 chars.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            print("Category must be a string with more than zero chars.")

    def articles(self):
        return self._articles 

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None


class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and 0 < len(title) <= 50:
            self._title = title
        else:
            print("Title must be a string between 1 and 50 characters")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            print("Author must be an Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            print("Magazine must be a Magazine.")
        self._magazine = new_magazine


author1 = Author("John Doe")
author2 = Author("Doe John")

mag1 = Magazine("MAg1", "Politics")
mag2 = Magazine("MAG2", "History")

a1 = author1.add_article(mag1, "AI")
print(a1)