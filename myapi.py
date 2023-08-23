import paralleldots
# Setting your API key

class API:

    def __init__(self):
        paralleldots.set_api_key('fCoqlPsE1UKrLrnwh2b4pnRAcDXkDdrz5KXLQV6p0ZA')

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def ner(self,text):
        paralleldots.ner(text)

    def emotion_prediction(self,text):
        paralleldots.emotion(text)