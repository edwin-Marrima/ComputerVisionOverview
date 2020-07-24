#Thresholding pode ser traduzido por limiarização e no caso de processamento de
#imagens na maior parte das vezes utilizamos para binarização da imagem. Normalmente
#convertemos imagens em tons de cinza para imagens preto e branco onde todos os pixels
#possuem 0 ou 255 como valores de intensidade.
import  cv2

#import mahotas
from matplotlib import pyplot as plt
import numpy as np
class Binarizacao:
                  def binarizacaoComLimiar(self,img):
                            img = img[::2,::2];
                            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            suave = cv2.GaussianBlur(img,(7,7),0) #aplica blur
                            (T,bin) = cv2.threshold(suave,160,255,cv2.THRESH_BINARY)
                            (T,binI) = cv2.threshold(suave,160,255,cv2.THRESH_BINARY_INV)
                            resultado = np.vstack([
                                np.hstack([suave,bin]),
                                np.hstack([binI,cv2.bitwise_and(img,img,mask=binI)])
                            ])

                            cv2.imshow("Binarizacao da Imagem",binI)
                            cv2.waitKey(0)
                  def threholdAdaptativo(self,img):
                            img = img[::2,::2]
                            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            suave = cv2.GaussianBlur(img,(7,7),0)
                            bin1 = cv2.adaptiveThreshold(suave,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                                         cv2.THRESH_BINARY_INV,21,5)
                            bin2 = cv2.adaptiveThreshold(suave,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                         cv2.THRESH_BINARY_INV,21,5) #elimina melhor ruidos
                            resultado = np.vstack([
                                np.hstack([img,suave]),
                                np.hstack([bin1,bin2])
                            ])
                            cv2.imshow("Binarizacao adaptativa da img",bin2)
                            cv2.waitKey(0)
                  def binarizacaoOtsu(self,img):
                      img = img[::2,::2]
                      img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                      #otsu's  binarizacao ou limiar
                      ret,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU);
                      # otsu's  binarizacao ou limiar depois de suavizacao Gaussiana
                      suave = cv2.GaussianBlur(img,(5,5),0)
                      ret2,th3 = cv2.threshold(suave,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                      resultado = np.vstack([th2,th3])
                      cv2.imshow("Binarizacao com OTSU", resultado)
                      cv2.waitKey(0)




if __name__ == '__main__':
    img = cv2.imread("../img/dados1.jpg");
    obj = Binarizacao();
    obj.binarizacaoComLimiar(img)
    obj.threholdAdaptativo(img)
    obj.binarizacaoOtsu(img)