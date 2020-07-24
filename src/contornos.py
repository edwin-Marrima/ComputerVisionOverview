import  cv2
#import mahotas
from matplotlib import pyplot as plt
import numpy as np
class Contornos:
                def contornos(self,img):
                    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    suave = cv2.GaussianBlur(imgray, (7, 7), 0)  # aplica blur
                    (T, img2) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
                    ret2, th3 = cv2.threshold(suave, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                    canny1 = cv2.Canny(th3, 20, 120)
                    (image,contours) = cv2.findContours(canny1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                    img = cv2.drawContours(img,image,-1,(0,255,0),3)
                    cv2.imshow("Contornos",img)
                    cv2.waitKey(0)
if __name__ == '__main__':
    img = cv2.imread("../img/tabela1.jpg");  # 257
    obj = Contornos()
    obj.contornos(img)