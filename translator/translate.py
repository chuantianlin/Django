
from googletrans import Translator
def translate(text):
        translator =Translator()
        translate_text = translator.translate(text, dest='CN')  
        return translate_text.text
