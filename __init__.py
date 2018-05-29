import sys
import dbus
import glib
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage 

__author__ = 'aix'

LOGGER = getLogger(__name__)

class ImgRecogPlasmaDesktopSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(ImgRecogPlasmaDesktopSkill, self).__init__(name="ImgRecogPlasmaDesktopSkill")
        
    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        imgrecog_general_plasma_skill_intent = IntentBuilder("ImgRecogKeywordIntent").\
            require("ImgRecogKeyword").build()
        self.register_intent(imgrecog_general_plasma_skill_intent, self.handle_imgrecog_general_plasma_skill_intent)
        
    def handle_imgrecog_general_plasma_skill_intent(self, message):
        utterance = message.data.get('utterance')
        utterance = utterance.replace(
                message.data.get('ImgRecogKeyword'), '')
        searchString = utterance
        imgRurl = searchString.replace(searchString[:8], '')
        
        app = ClarifaiApp("gg_0vhbsOoZGq6N85i3yuKKcHj5JvTLrX62KeeyD", "YOKgEUJc6SgikEREgPE3iSkRHd11tY4w2alSghot")
        model = app.models.get('general-v1.3')
        image = ClImage(file_obj=open(imgRurl, 'rb'))
        a = model.predict([image])
        
        b = ''
        for z in a['outputs']:
            for y in z['data']['concepts']:
                if not b :
                    b =  y['name']
                else:
                    b = b + ',' + y['name']

        self.speak_dialog("imgresult.general", data={'GeneralResult': b})
        
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return ImgRecogPlasmaDesktopSkill()
