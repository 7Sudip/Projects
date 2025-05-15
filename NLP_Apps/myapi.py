import nlpcloud
from langcodes import Language




# Setting your API key

class API:

    def sentiment_analysis(self,text):
        # Initialize the NLPCloud client with your API key and model
        client = nlpcloud.Client("finetuned-llama-3-70b", "cdabccf1b2cd6d7e60f4f0c6f4307b684fe5178c", gpu=True)
        # Perform sentiment analysis
        response = client.sentiment(text)
        l = []
        for i in response['scored_labels']:
            l.append(i['score'])

        index = sorted(list(enumerate(l)), key=lambda x: x[1], reverse=True)[0][0]
        result = response['scored_labels'][index]['label']

        return result
    

    def ner_analysis(self,text,entity):
       
        client = nlpcloud.Client("finetuned-llama-3-70b", "cdabccf1b2cd6d7e60f4f0c6f4307b684fe5178c", gpu=True)
        response = client.entities( text,searched_entity=entity)
       
        return response

    def language_detection(self,text):
        # Initialize the NLPCloud client with your API key and model
        # Perform language detection
        client = nlpcloud.Client("python-langdetect", "cdabccf1b2cd6d7e60f4f0c6f4307b684fe5178c", gpu=False)
        Response = client.langdetection(text)
        l =[]
        for i in Response['languages']:
            l.append(list(i.values())[0])

        index = sorted(list(enumerate(l)), key=lambda x: x[1], reverse=True)[0][0]
        lang = list(Response['languages'][index].keys())[0]
        language_name = Language.get(lang).display_name()
        return language_name 