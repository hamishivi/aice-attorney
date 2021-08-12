from textblob import TextBlob
from collections import Counter
import random

class Analizer:
    def __init__(self):
        self.language_counter = Counter()
        self.official_api = False
    
    def get_sentiment(self, text):
        try:
            try:
                language = self.detect_language_heuristic(text)
            except UnknownLanguage:
                language = self.detect_language_heuristic(text)

            self.language_counter.update({language: 1})
            # print(self.language_counter)
            
            if (language == 'en'):
                return self.proccess_eng(text)

            if (language == 'google'):
                return self.process_google(text)
            
            try:
                return self.process_poly(text)
            except ZeroDivisionError:
                return 'N'
            except Exception as e:
                print(e)
                return self.process_google(text)
        except Exception as e:
            print(e)
            return self.proccess_eng(text)
        

    def process_google(self, text):
        return self.proccess_eng(str(TextBlob(text)))
        

    
    def proccess_eng(self, text):
        blob = TextBlob(text)
        if (blob.sentiment.polarity > 0.05):
            return '+'
        if (blob.sentiment.polarity < -0.05):
            return '-'
        return 'N'

    def process_poly(self, text):
        poly_text = Text(text)
        if (poly_text.polarity > 0.35):
            return '+'
        # If polarity is -1 there isn't enough information to determine if it's negative therefore we introduce randomness
        if (poly_text.polarity < -0.35 and (poly_text.polarity > -1 or random.random() > 0.25)):
            return '-'
        return 'N'

    def detect_language_heuristic(self, text):
        if (len(text) <=2):
            language = 'en'
        else:
            language = 'google'
        return language
