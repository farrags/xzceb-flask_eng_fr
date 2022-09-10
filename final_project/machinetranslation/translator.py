"""this is translator
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(F'{apikey}')
language_translator = LanguageTranslatorV3(
    version=F'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    if english_text =='' :
        return ''
    french_text = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return french_text["translations"][0]["translation"]

def frenchToEnglish (french_text):
    if french_text =='' :
        return ''
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text["translations"][0]["translation"]
