from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import os
import sys
import urllib

# recaptcha libraries
import pydub
import speech_recognition as sr

service=Service("C:\\browserdrivers\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver=webdriver.Chrome(service=service,options=options)
# driver.maximize_window()

driver.get("https://www.yahoo.com")

driver.find_element_by_xpath('//*[@id="ysignin"]/div').click()

driver.find_element_by_xpath('//*[@id="login-username"]').send_keys('cutiekaura@gmail.com')

driver.find_element_by_xpath('//*[@id="login-signin"]').click()

frames = driver.find_elements_by_tag_name("iframe")
time.sleep(3)
recaptcha_control_frame = None
recaptcha_challenge_frame = None
for index, frame in enumerate(frames):
        if frame.get_attribute("title") == "reCAPTCHA":
            recaptcha_control_frame = frame
            time.sleep(1)
        if frame.get_attribute("title") == "recaptcha challenge":
            recaptcha_challenge_frame = frame
            time.sleep(1)
if not (recaptcha_control_frame and recaptcha_challenge_frame):
        print("[ERR] Unable to find recaptcha. Abort solver.")
        exit()
    # switch to recaptcha frame
time.sleep(3)
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(recaptcha_control_frame)

    # click on checkbox to activate recaptcha
time.sleep(3)
driver.find_element_by_class_name("recaptcha-checkbox-border").click()

    # switch to recaptcha audio control frame
time.sleep(3)
driver.switch_to.default_content()
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(recaptcha_challenge_frame)

    # click on audio challenge
driver.find_element_by_id("recaptcha-audio-button").click()

    # switch to recaptcha audio challenge frame
time.sleep(3)
driver.switch_to.default_content()
frames = driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(recaptcha_challenge_frame)

    # get the mp3 audio file
time.sleep(3)
src = driver.find_element_by_id("audio-source").get_attribute("src")
print(f"[INFO] Audio src: {src}")
time.sleep(3)
path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), "sample.mp3"))
path_to_wav = os.path.normpath(os.path.join(os.getcwd(), "sample.wav"))

    # download the mp3 audio file from the source
time.sleep(3)
urllib.request.urlretrieve(src, path_to_mp3)

    # load downloaded mp3 audio file as .wav
try:
    sound = pydub.AudioSegment.from_mp3(path_to_mp3)
    sound.export(path_to_wav, format="wav")
    sample_audio = sr.AudioFile(path_to_wav)
except Exception:
    sys.exit(
            "[ERR] Please run program as administrator or download ffmpeg manually, "
            "https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"
        )

    # translate audio to text with google voice recognition
r = sr.Recognizer()
with sample_audio as source:
    audio = r.record(source)
key = r.recognize_google(audio)
print(f"[INFO] Recaptcha Passcode: {key}")

    # key in results and submit
driver.find_element_by_id("audio-response").send_keys(key.lower())
driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
driver.switch_to.default_content()
driver.find_element_by_id("recaptcha-demo-submit").click()

#recaptcha-anchor > div.recaptcha-checkbox-border