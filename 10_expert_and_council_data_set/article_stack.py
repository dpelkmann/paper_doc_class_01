#!/bin/python
# ---------------------------------------------------------
# article_stack.py
#
# David Pelkmann <david.pelkmann@fh-bielefeld.de>
#       Department of Engineering Sciences and Mathematics
#       University of Applied Sciences Bielefeld
#
# 10. February 2020 (dp)
# ---------------------------------------------------------
# Info
# ----
# In this file the classes for an article and article stack are stored
# ---

class Article: 
    def __init__(   self, cnt=None, data=None, newspaper_name=None, label=None,
                    html_code=None, article_title=None, article_text=None):

        self.__newspaper_name = newspaper_name
        self.__html_code = html_code
        self.__data = data
        self.__article_title = article_title
        self.__article_text = article_text
        if label != None:
            self.__label = label
        else:
            self.__label = {    "nat-politik": False,
                                "int-politik": False,
                                "wirtschaft" : False,
                                "sport" : False,
                                "ungluecke" : False,
                                "recht" : False,
                                "wissenschaft" : False,
                                "soziales" : False,
                                "familie" : False,
                                "religion" : False,
                                "umwelt" : False,
                                "verkehrssysteme" : False,
                                "krieg" : False,
                                "sicherheit" : False,
                                "kultur" : False,
                                "digitales" : False,
                                "human-interest" : False,
                                "other" : False}
        self.__topics = [   "nat-politik",      # Nationale Politik (DE)
                            "int-politik",      # Internationale Politik 
                            "wirtschaft",       # Wirtschaft
                            "sport",            # Sport
                            "ungluecke",        # Ungluecke / Unfaelle
                            "recht",            # Recht / Kriminalität
                            "wissenschaft",     # Wissenscahft, Technik, Forschung
                            "soziales",         # Gesundheit, Soziales
                            "familie",          # Familie, Bildung, Erziehung, ...
                            "religion",         # Religion
                            "umwelt",           # Umwelt, Natur, ...
                            "verkehrssysteme",  # Verkehrssysteme
                            "krieg",            # Krieg, Terror
                            "sicherheit",       # Terrsitoriale Fragen, Sicherheit, Verteidigung
                            "kultur",           # Kultur
                            "digitales",        # Digitales, Medien
                            "human-interest",   # Human-Interest (Prominenz, Essen, Sexualität, ...)
                            "other"]            # Alles was nicht als Ueberthema beachtet wurde
        self.__cnt = cnt
        self.__token = []

    def get_data(self): return self.__data
    def set_data(self, data): self.__data = data
    def get_newspaper_name(self): return self.__newspaper_name
    def set_newspaper_name(self, newspaper_name): self.__newspaper_name = newspaper_name
    def get_html_code(self): return self.__html_code
    def set_html_code(self, html_code): self.__html_code = html_code
    def get_topics(self): return self.__topics
    def get_label(self): return self.__label
    def set_one_label(self, topic, status=True): self.__label[topic] = status
    def set_label(self, label): self.__label = label
    def unset_label(self, topic, status=False): self.__label[topic] = status
    def get_article_text(self): return self.__article_text
    def set_article_text(self, text): self.__article_text = text
    def get_article_title(self): return self.__article_title
    def set_article_title(self, title): self.__article_title = title
    def get_article_token(self): return self.__token
    def set_article_token(self, token): self.__token = token
    

class ArticleStack():
    def __init__(self):
        self.__counter_article = 0
        self.__Stack = []  # an instance attribute
        self.__cnt_label = {    "nat-politik": 0,
                                "int-politik": 0,
                                "wirtschaft" : 0,
                                "sport" : 0,
                                "ungluecke" : 0,
                                "recht" : 0,
                                "wissenschaft" : 0,
                                "soziales" : 0,
                                "familie" : 0,
                                "religion" : 0,
                                "umwelt" : 0,
                                "verkehrssysteme" : 0,
                                "krieg" : 0,
                                "sicherheit" : 0,
                                "kultur" : 0,
                                "digitales" : 0,
                                "human-interest" : 0,
                                "other" : 0}

    def appendArticle(self, object):
        __metaclass__= Article
        self.__Stack.append(object)
        self.__counter_article = self.__counter_article + 1

    def get_stack(self): return self.__Stack
    def set_stack(self, stack): self.__Stack = stack
    def get_cnt_label(self): return self.__cnt_label
    def set_cnt_label(self, name, cnt): self.__cnt_label[name] = self.__cnt_label[name] + cnt
    def get_cnt_article(self): return self.__counter_article
    
    def printArticle(self, index):
        try:
            print(self.__Stack[index].get_tweetID())
        except:
            print("WRONG INDEX!")
        
