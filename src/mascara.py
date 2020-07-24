import  cv2
import numpy as np

class Mascara:

                def mascarra(self):
                        img = cv2.imread("../img/entrada.jpg")
                        cv2.imshow("Original",img)

                        mascara = np.zeros(img.shape[:2], dtype="uint8")
                        (cX,cY) = (img.shape[1]//2,img.shape[0]//2);
                        cv2.circle(mascara, (cX, cY), 180, 255, 70)
                        cv2.circle(mascara,(cX,cY),70,255,-1)
                        img_com_mascara = cv2.bitwise_and(img,img,mask=mascara)
                        cv2.imshow("Mascara aplicada",img_com_mascara)
                        cv2.waitKey(0)


if __name__=='__main__':
       mascara = Mascara();
       mascara.mascarra();
