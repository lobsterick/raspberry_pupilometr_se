##### Setup section
# 1. Loading tools
import numpy #przetwarzanie obrazów
import cv2 #przetwarzanie obrazów
import math #obliczenia matematyczne
import re #wyrażenia regularne
import pylab #tworzenie wykresów
import pygame #obsługa dźwięku
import io #obsługa strumienia danych
import picamera #obsługa kamery
import RPi.GPIO as GPIO #obsługa portów GPIO
import time #operacje związane z czasem
import datetime #operacje związane z czasem
import os #współpraca z systemem
import random #wprowadzanie losowości
import sys #współpraca z systemem
from xlwt import Workbook #zapis do pliku Excel

def pixelsToMm(pixels):
    mm = pixels/73
    return mm

class SplitFrames(object):
    def __init__(self):
        self.frame_number = 0
        self.output = None

    def write(self, buf):
        if buf.startswith(b'\xff\xd8'):
            if self.output:
                self.output.close()
            self.frame_number += 1
            self.output = io.open(os.path.join(mypath,'Frame%02d.jpg' % self.frame_number), 'wb')
        self.output.write(buf)


# 2. Setup Section
soundPath = "/home/pi/Desktop/Pupilometr/Sounds"
IADS2path = "/home/pi/Desktop/Pupilometr/Sounds/IADS2"
warmupTime = 5 # czas rozgrzewania układu kamery
debugSwitch = 0 #przełącznik trybu podglądu etapów przetwarzania obrazów
blinkRepairSwitch = 1 #przełącznik usuwania z wykresu mrugnięć
plotingSwitch = 1 #przełącznik tworzenia wykresów

noStimulationTime = 0
registerBeforeTime = 0
registerAfterTime = 0
supriseTimeRangeStart = 0
supriseTimeRangeStop = 0
durationOfLight = 0
lengthOfStimulation = 0
lengthOfWhiteNoise = 0

# 3. Reading Arguments
patientName = sys.argv[1]
stimulationType = sys.argv[2]
if stimulationType == "nostimulation" and len(sys.argv) == 4 and int(sys.argv[3]) > 0:
    noStimulationTime = int(sys.argv[3])
elif stimulationType == "mysound" and len(sys.argv) == 6:
    soundName = sys.argv[3]
    registerBeforeTime = int(sys.argv[4])
    registerAfterTime = int(sys.argv[5])
elif stimulationType == "randomsound" and len(sys.argv) == 5:
    registerBeforeTime = int(sys.argv[3])
    registerAfterTime = int(sys.argv[4])
elif stimulationType == "startle" and len(sys.argv) == 6:
    supriseTimeRangeStart = int(sys.argv[3])
    supriseTimeRangeStop = int(sys.argv[4])
    registerAfterTime = int(sys.argv[5])
elif stimulationType == "light" and len(sys.argv) == 6:
    registerBeforeTime = int(sys.argv[3])
    durationOfLight = int(sys.argv[4])
    registerAfterTime = int(sys.argv[5])
else:
    print("\033[31m","\nNie podano prawidłowej opcji uruchomienia pupilometru - proszę zapoznać się z dokumentacją!\n", "\033[0m")
    sys.exit(0)
                      
# 4. Preparing Directory
today = datetime.date.today()
todaystr = time.strftime("/home/pi/Desktop/Pupilometr/Photos/%Y.%m.%d/%H:%M:%S")
mypath = (todaystr+"_"+patientName+"_"+stimulationType)
os.makedirs(mypath)

# 5. Preparing Light System
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
if str(stimulationType == "light"):
    GPIO.setup(23,GPIO.OUT)

# 6.Preparing Audio System
if stimulationType == "mysound" or stimulationType == "randomsound" or stimulationType == "startle":
    pygame.mixer.init()       
    if str(stimulationType) == "randomsound":
        IADS2audio = [ f for f in os.listdir(IADS2path) if os.path.isfile(os.path.join(IADS2path,f))]
        randomAudioFromIADS2 = random.choice(IADS2audio)
        stimulationSoundPath = os.path.join(IADS2path, randomAudioFromIADS2)
        whiteNoiseSoundPath = os.path.join(soundPath, "whitenoise4s.wav")
        whiteNoiseSound = pygame.mixer.Sound(whiteNoiseSoundPath)      
        lengthOfWhiteNoise = 4
    elif str(stimulationType) == "mysound":
        IADS2audio = [ f for f in os.listdir(IADS2path) if os.path.isfile(os.path.join(IADS2path,f))]
        if soundName in IADS2audio:
            stimulationSoundPath = os.path.join(IADS2path, soundName)
        else:
            print("\033[31m","Nie odnaleziono takiego pliku dźwiękowego w bazie!\n", "\033[0m")
            sys.exit(0)
        whiteNoiseSoundPath = os.path.join(soundPath, "whitenoise4s.wav")
        whiteNoiseSound = pygame.mixer.Sound(whiteNoiseSoundPath)   
        lengthOfWhiteNoise = 4
    elif str(stimulationType) == "startle":
        stimulationSoundPath = os.path.join(soundPath, "startlescream.wav")
        registerBeforeTime = random.randint(supriseTimeRangeStart, supriseTimeRangeStop)
        print("Opóźnienie straszenia w sekundach: ", registerBeforeTime)
    stimulationSound = pygame.mixer.Sound(stimulationSoundPath)        
    lengthOfStimulation = stimulationSound.get_length()       
       
       
##### Recording Section
print("\n-----------------------------")
print("\033[35m", "Uruchomiono pupilometrię!", "\033[0m")
print("-----------------------------\n")

with picamera.PiCamera(resolution='1280x720', framerate=60) as camera:
    # 7. Camera setup
    GPIO.output(18,GPIO.HIGH) #uruchomienie diody doświetlającej
    camera.rotation=270 #obrót obrazu z kamery o 270 stopnii
    camera.start_preview() #uruchomienie podglądu obrazu
    print("Rozgrzewanie kamery przez ", warmupTime, "sekund.")
    time.sleep(int(warmupTime)) #podgląd obrazu przez 5 sekund     
    print("Rozpoczęcie rejestracji.")
    output = SplitFrames()
    start = time.time() #zapis czasu rozpoczęcia badania
    camera.start_recording(output, format='mjpeg') #rozpoczęcie rejestracji
        
    # 8. Stimulation-driven behaviours
    if str(stimulationType) == "nostimulation":
        print("Wybrano brak stymulacji, rejestruje ", noStimulationTime, " sekund.")
        camera.wait_recording(noStimulationTime)
        lengthOfStimulation = noStimulationTime
    elif str(stimulationType) == "startle":
        print("Wybrano tryb straszenia, czekaj na bodziec...")
        camera.wait_recording(registerBeforeTime)    
        stimulationSound.play();
        print("Bodziec odtworzony!")
        camera.wait_recording(registerAfterTime+lengthOfStimulation)     
    elif str(stimulationType) == "randomsound" or str(stimulationType) == "mysound":
        camera.wait_recording(registerBeforeTime)    
        print("Odtwarzanie białego szumu.")
        whiteNoiseSound.play();
        camera.wait_recording(lengthOfWhiteNoise)
        print("Odtwarzanie stymulacji.")
        stimulationSound.play();
        camera.wait_recording(lengthOfStimulation+registerAfterTime)
    elif str(stimulationType) == "light":
        camera.wait_recording(registerBeforeTime)
        print("Uruchomiono stymulację świetlną!")
        GPIO.output(23,GPIO.HIGH)
        print("Światło włączone.")
        camera.wait_recording(durationOfLight)
        GPIO.output(23,GPIO.LOW)
        print("Światło wyłączone.")
        camera.wait_recording(registerAfterTime)
        lengthOfStimulation = durationOfLight
        GPIO.output(23,GPIO.LOW)
        blinkRepairSwitch = 0
    camera.stop_recording()
    finish = time.time()
    GPIO.output(18,GPIO.LOW)

timeOfMeasurement = finish - start
numberOfFrames = output.frame_number
fps = numberOfFrames / timeOfMeasurement

print("\n-----------------------------")
print("\033[35m", "Uruchomiono sekcję pomiarową!", "\033[0m")
print("-----------------------------\n")
   
# 9. Probability Settings Section
probabilityTresholdMin = 1
probabilityTresholdMax = 8
probabilityGoodCounter = 0
probabilityBadCounter = 0
area = []
diameter = []
    
# 10. Indexing Files
startCalculationTime = time.time()
onlyfiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
onlyfiles = sorted(onlyfiles, key=lambda x: (int(re.sub('\D', ' ',x)), x))
images = numpy.empty(len(onlyfiles), dtype=object)
    
# 11. Morfological operation and pupil size finding
print("Kolejne pomiary źrenicy w mm: ")
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread( os.path.join(mypath,onlyfiles[n]), cv2.IMREAD_GRAYSCALE )
    image_in = images[n]
    th, image_th = cv2.threshold(image_in, 50, 255, cv2.THRESH_BINARY_INV);   
    image_floodfill = image_th.copy()
    h, w = image_th.shape[:2]
    mask = numpy.zeros((h+2, w+2), numpy.uint8)
    cv2.floodFill(image_floodfill, mask, (0,0), 255);
    image_floodfill_inv = cv2.bitwise_not(image_floodfill)
    image_out = image_th | image_floodfill_inv
        
    # 12. Display images Section
    if debugSwitch == 1:
            cv2.imshow("Oryginalny obraz w skali szarości - klatka nr %d" % n, image_in)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow("Obraz po odwróconej binaryzacji - klatka nr %d" % n, image_th)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow("Obraz obszaru odbicia diody - klatka nr %d" % n, image_floodfill)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            cv2.imshow("Wykryta źrenica  - klatka nr %d" % n, image_out)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    
    area_temp = numpy.count_nonzero(image_out)
    area.append(float(area_temp))
    diameter_temp = pixelsToMm((math.sqrt(area_temp/math.pi))*2)
    diameter.append(float(diameter_temp))
       
    if probabilityTresholdMin <= diameter_temp <= probabilityTresholdMax:
        print("\033[32m", "Klatka nr %d: " % n, "%.2f mm. OK!" % diameter_temp, "\033[0m")
        probabilityGoodCounter +=1
    else:
        print("\033[31m", "Klatka nr %d:" % n, "%.2f mm. Możliwy błąd!" % diameter_temp, "\033[0m")
        probabilityBadCounter +=1

stopCalculationTime = time.time()
timeOfCalculatios = stopCalculationTime - startCalculationTime
meanPupilSize = sum(diameter, 0.0) / len(diameter)

print("\n-----------------------")
print("Prawidłowo wykrytych: ", probabilityGoodCounter)
print("Źle wykrytych: ", probabilityBadCounter)
print("-----------------------\n")
         
## 13. Save to Excel WorkSheet
wb = Workbook()
measurementsheet = wb.add_sheet('Sheet 1')
measurementsheet.write(0,0,"Sciezka")
measurementsheet.write(0,1,mypath)
measurementsheet.write(1,0,"Data")
measurementsheet.write(1,1,today)
measurementsheet.write(2,0,"Badany")
measurementsheet.write(2,1,patientName)
measurementsheet.write(3,0,"Typ stymulacji: ")
measurementsheet.write(3,1,stimulationType)
measurementsheet.write(4,0,"Czas rejestracji przed")
measurementsheet.write(4,1,registerBeforeTime)
measurementsheet.write(5,0,"Czas białego szumu")
measurementsheet.write(5,1,lengthOfWhiteNoise)
measurementsheet.write(6,0,"Czas stymulacji")
measurementsheet.write(6,1,lengthOfStimulation)
measurementsheet.write(7,0,"Czas rejestracji po")
measurementsheet.write(7,1,registerAfterTime)

for items in range(len(onlyfiles)):
    measurementsheet.write(items+8,0,items/fps)
for items in range(len(diameter)):
    measurementsheet.write(items+8,1,diameter[items])

wb.save(os.path.join(mypath,"Pomiary.xls"))
        
# Blinking Repair
if blinkRepairSwitch == 1: 
    for i in range(1, len(diameter)):
        if not meanPupilSize*1.25 > diameter[i] > meanPupilSize*0.85:
            diameter[i]=numpy.nan
            print("\033[33m", "Naprawiono klatke nr: %d" % i, "\033[0m")
    
# 14. Summary
print("\nRodzaj stymulacji: %s" % stimulationType)
if stimulationType == "randomsound":
    print("Wybrany dźwięk: %s" % randomAudioFromIADS2)
if stimulationType == "mysound":
    print("Wybrany dźwięk: %s" % soundName)
print("Ilość zarejestrowanych klatek: %d" % numberOfFrames)
print("Łączny czasu pomiaru: %d sekund" % timeOfMeasurement)
print("Czas rejestracji przedpomiarowej: %d sekund" % registerBeforeTime)
if lengthOfStimulation != 0:
    print("Czas stymulacji: %d sekund" % lengthOfStimulation)
if lengthOfWhiteNoise != 0:
    print("Długość trwania białego szumu: %d sekund" % lengthOfWhiteNoise)
print("Czas rejestracji popomiarowej: %d sekund" % registerAfterTime)
print("Szybkość rejestracji: %.2f klatek na sekundę" % fps)
print("Ścieżka zapisu zdjęć: %s" % mypath)
print("Czas obliczeń: %d sekund" % timeOfCalculatios)
    
# 15. Ploting
if plotingSwitch == 1:
    x=list(range(len(onlyfiles)))
    for iterator in range(0,len(x)):
        x[iterator] = x[iterator]/fps
    y=diameter
    pylab.plot(x,y)
    pylab.ylabel("Średnica źrenicy [mm]")
    pylab.xlabel("Czas badania [s]")
    pylab.plot([registerBeforeTime,registerBeforeTime],
                [0.8*meanPupilSize,1.2*meanPupilSize])
    pylab.plot([int(lengthOfWhiteNoise)+int(lengthOfStimulation)+int(registerBeforeTime), int(lengthOfWhiteNoise)+int(lengthOfStimulation)+int(registerBeforeTime)],
                [0.8*meanPupilSize,1.2*meanPupilSize])
    if lengthOfWhiteNoise != 0:
        pylab.plot([int(lengthOfWhiteNoise)+int(registerBeforeTime), int(lengthOfWhiteNoise)+int(registerBeforeTime)],
                [0.8*meanPupilSize,1.2*meanPupilSize])
    pylab.savefig(os.path.join(mypath,"Wykres"))
    pylab.show()
