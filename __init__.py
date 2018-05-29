import sys
import pytesseract
import enchant
import re
from nltk import word_tokenize
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
from PIL import Image, ImageEnhance, ImageFilter
 
__author__ = 'aix'

LOGGER = getLogger(__name__)

class ImgOcrPlasmaDesktopSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ImgOcrPlasmaDesktopSkill, self).__init__(name="ImgOcrPlasmaDesktopSkill")
        
    @intent_handler(IntentBuilder("ImgOcrKeywordIntent").require("ImgOcrKeyword").build())
    def handle_imgocr_general_plasma_skill_intent(self, message):
        utterance = message.data.get('utterance')
        utterance = utterance.replace(message.data.get('ImgOcrKeyword'), '')
        searchString = utterance
        imgRurl = searchString.replace(searchString[:8], '')
        im = Image.open(imgRurl)
        enhancer = ImageEnhance.Contrast(im)
        im = im.filter(ImageFilter.SHARPEN)
        im = im.filter(ImageFilter.EDGE_ENHANCE)
        im.save('/tmp/image.jpg')
        getOCR = Image.open('/tmp/image.jpg')
        ocrtext = pytesseract.image_to_string(getOCR)
        self.speak(ocrtext)
    
    def extract_words(self, s):
        return [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in s.split()]

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return ImgOcrPlasmaDesktopSkill()
