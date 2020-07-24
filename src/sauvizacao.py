# BLURRRRRRRR
import  cv2
from matplotlib import pyplot as plt
import numpy as np
class Suavizacao:
    #BLUR#
                 def suavizacaoo(self,img):

                     img = img[::2,::2]; #dminui imagem
                     suave = np.vstack([
                     np.hstack([img, cv2.blur(img, ( 3, 3))]),
                     np.hstack([cv2.blur(img, (5, 5)), cv2.blur(img, (7, 7))]),
                     np.hstack([cv2.blur(img, (9, 9)), cv2.blur(img, (11, 11))]),
                     ])
                     sauveSimples = np.vstack([np.hstack([img, cv2.blur(img, ( 3, 3))])])
                     #ss = np.hstack([img, cv2.blur(img, ( 3, 3))])
                     cv2.imshow("IMAGEM suavisadas (Blur)", suave);
                     cv2.imshow("IMAGEM simples (Blur)", sauveSimples);
                     cv2.waitKey(0)

                 def suavizacaoGausianna(self,img):
                     img = img[::2, ::2];  # dminui imagem
                     suave = np.vstack([
                     np.hstack([img,
                                cv2.GaussianBlur(img, (3, 3), 0)]),
                     np.hstack([cv2.GaussianBlur(img, (5, 5), 0),
                                cv2.GaussianBlur(img, (7, 7), 0)]),
                     np.hstack([cv2.GaussianBlur(img, (9, 9), 0),
                                cv2.GaussianBlur(img, (11, 11), 0)]),
                     ])
                     suaveSimples = cv2.GaussianBlur(img,(3,3),0);
                     cv2.imshow("Imagem original e suavisadas pelo filtroGaussiano ", suaveSimples)
                     cv2.waitKey(0)
                 def sauvizacaoDaMediana(self,img):
                     img = img[::2, ::2];  # dminui imagem
                     suave = np.vstack([
                         np.hstack([img,
                                    cv2.medianBlur(img, 3)]),
                         np.hstack([img,
                                    cv2.medianBlur(img, 5)]),
                         np.hstack([img,
                                    cv2.medianBlur(img, 7)]),
                         np.hstack([img,
                                    cv2.medianBlur(img, 9)]),
                         np.hstack([img,
                                    cv2.medianBlur(img, 11)]),
                     ])
                     cv2.imshow("Imagem original e suavisadas pela mediana", suave)
                     cv2.waitKey(0)

                 def filtroBilateral(self,img):#metodo com memos ruido
                     img = img[::2,::2]
                     sauve = np.vstack([
                         np.hstack([img,
                                    cv2.bilateralFilter(img,3,21,21)]),
                         np.hstack([cv2.bilateralFilter(img,5,35,35),
                                    cv2.bilateralFilter(img,7,49,49)]),
                         np.hstack([cv2.bilateralFilter(img,9,63,63),
                                    cv2.bilateralFilter(img,11,77,77)])

                     ])
                     sauveSimples = cv2.bilateralFilter(img,7,49,49)
                     cv2.imshow("Sauvizacao com filtroBilateral",sauveSimples)
                     cv2.waitKey(0)











if __name__ == '__main__':
        img = cv2.imread("../img/entrada.jpg");
        obj = Suavizacao();
        #obj.suavizacaoo(img)
        obj.suavizacaoGausianna(img)
        #obj.sauvizacaoDaMediana(img)
        #obj.filtroBilateral(img)