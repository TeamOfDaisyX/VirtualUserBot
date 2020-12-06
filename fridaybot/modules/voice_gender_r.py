from fridaybot.utils import admin_cmd
from pydub import AudioSegment
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import PCA
import numpy as np
import pickle
import subprocess
import os

sedpath = "./starkgangz/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
    
svm = pickle.load(open("resources/voicer/svm.sav", 'rb'))
lr = pickle.load(open("resources/voicer/lr.sav", 'rb'))

@friday.on(admin_cmd(pattern="vr"))
async def ok(event):
      hmm = await event.get_reply_message()
      seddl = await borg.download_media(hmm.media, sedpath)
      sound = AudioSegment.from_ogg(seddl)
      sound.export("voice.wav", format="wav")
      FNULL = open(os.devnull, 'w')
      subprocess.call(('Rscript', "resources/extract_feature.r"), stdout=FNULL, stderr=subprocess.STDOUT)
      sample = open("my_voice.csv", "r").read().split("\n")[1].split(",")
      sample = [sample]
      text = ""
      if int(svm.predict(sample)[0]) == 0:
        text += "for <b>SVM</b> you are <b>male</b>"
      else:
        text += "for <b>SVM</b> you are <b>female</b>"
      text += "\n"
      if int(lr.predict(np.float64(sample))[0]) == 0:
        text += "for <b>LR</b> you are <b>male</b>"
      else:
        text += "for <b>LR</b> you are <b>female</b>"
      await event.edit("We apply two algorithms:\n"+text, parse_mode='HTML')      
    
