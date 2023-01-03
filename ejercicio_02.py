import cv2

cap = cv2.VideoCapture(0) # VideoCapture me activa la camara correspondiente :(o) cero para la cardinalidad de las camaras instaladas

while True: # bucle infinito
    ret, frame = cap.read() # leyendo la informacion  de la webcam (ref = audio ,  frame = video),  se declara ref pero no se va a utilizar
    cv2.imshow("video", frame)   
    key = cv2.waitKey(1) # espera 1 segundo  cuando se presione una tecla

    if key == 27: #  27 es escape en ascii
        break # el bucle infinito se rompe
    
cap.release() # es para apagar la camara
cv2.destroyAllWindows() # cierra todas las ventanas creadas
