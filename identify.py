import cv2
import numpy as np
import os
from PIL import Image, ImageTk
import tkinter
import PySimpleGUI as sg
import numpy as np
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
 
layout = [[sg.Text("SISTEMA IDENTIFICAÇÃO DE IMPRESSÕES DIGITAIS")], 
          [sg.Text("ATENÇÃO: ADICIONE O ARQUIVO NA MESMA PASTA DO PROGRAMA")],
          [sg.Text("NOME DO ARQUIVO:"), sg.Input(key='arquivo')],
          [sg.Button('ENVIAR')]]

window = sg.Window('IDENTIFICAÇÃO IMPRESSÕES DIGITAIS', layout)

while True:
    eventos, valores = window.read()
    if eventos == sg.WINDOW_CLOSED :
            break
    if eventos =='ENVIAR':
        
        for k, v in valores.items():
            values = v
        
    print(values)
    break
print('ADCIONE A IMAGEM DA IMPRESSÃO NA MESMA PASTA DO PROGRAMA:')
image = values

test_original = cv2.imread(image)
cv2.imshow("IMPRESSAO DIGITAL", cv2.resize(test_original, None, fx=1, fy=1))
cv2.waitKey(2621440)
cv2.destroyAllWindows()

files = os.listdir("database")
print(files)

for file in files:      
      print(file)
      
      fingerprint_database_image = cv2.imread("./database/" + file)
    
      sift = cv2.xfeatures2d.SIFT_create()
    
      keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
      keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)

      matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),dict()).knnMatch(descriptors_1, descriptors_2, k=2)

      match_points = []
      
      for p, q in matches:
          if p.distance < 0.1*q.distance:
              match_points.append(p)

      keypoints = 0
      
      if len(keypoints_1) <= len(keypoints_2):
          keypoints = len(keypoints_1)            
      
      else: 
          keypoints = len(keypoints_2)

      if (len(match_points) / keypoints)>0.95:
          
          print("% certeza: ", len(match_points) / keypoints * 100)
          certeza = len(match_points) / keypoints * 100
          print("IDENTIFICAÇÃO DA IMPRESSÃO: " + str(file)) 
          result = cv2.drawMatches(test_original, keypoints_1, fingerprint_database_image,  keypoints_2, match_points, None) 
          result = cv2.resize(result, None, fx=1, fy=1)
          horizontal = np.hstack((test_original, result))
          cv2.imshow("ID:" + str(file) + "  PRECISAO:"+ str(certeza)+"%", cv2.resize(horizontal, None, fx=1, fy=1))
          #cv2.imshow("IMPRESSAO DIGITAL",cv2.resize(test_original, None, fx=1, fy=1))
          
          cv2.waitKey(2621440)
          cv2.destroyAllWindows()
          break;
      else:
          print("SEM COMBINAÇÕES")
          
      
          
