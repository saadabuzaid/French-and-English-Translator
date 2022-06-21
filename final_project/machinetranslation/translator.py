'''
This module is to translate between English and French using
IBM's watson language translator API.
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    '''
    A function that translates from English to French
    using IBM's translator API.
    '''

    #Translate from English to French using IBM's translator
    french_text = language_translator.translate(
        text = english_text, model_id='en-fr').get_result()
    #Cast the json object to a dictonary object to extract
    # the value we want
    dictionary = json.loads(json.dumps(french_text, indent = 2))
    french_text = dictionary["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    '''
    A function that translates from French to English
    using IBM's translator API
    '''

    #Translate from French to English using IBM translator
    english_text = language_translator.translate(
        text = french_text, model_id='fr-en').get_result()
    #Cast the json object to a dictionary to extract the value
    # we want
    dictionary = json.loads(json.dumps(english_text, indent= 2))
    english_text = dictionary["translations"][0]["translation"]
    return english_text
