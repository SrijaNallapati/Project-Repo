import os
from PIL import Image
from gtts import gTTS
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
image="C:\\Users\\nalla\\OneDrive\\Desktop\\coding\\Image1.jpg"
# image="C:\\Users\\nalla\\OneDrive\\Desktop\\coding\\Image2.jpg"

def ImageToSound(image):
    try:
        open_image=Image.open(image)
        text=pytesseract.image_to_string(open_image)
        textfile=" ".join(text.split("\n"))
        print(textfile)
        sound=gTTS(textfile)
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except:
        print("Error while runnning")
        return
    
ImageToSound(image)