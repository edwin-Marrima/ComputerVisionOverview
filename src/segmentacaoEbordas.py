#     Quando falamos em segmentação e detecção de bordas, os algoritmos mais comuns
#   são o Canny, Sobel e variações destes. Basicamente nestes e em outros métodos a detecção de
#   bordas se faz através de identificação do gradiente, ou, neste caso, de variações abruptas na
#   intensidade dos pixels de uma região da imagem.
import  cv2
#import mahotas
from matplotlib import pyplot as plt
import numpy as np
class SegmentacaoEbordas:
                        def sobelMetodo(self,img):
                            img = img[::2,::2]
                            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                            sobelX = cv2.Sobel(img,cv2.CV_64F,1,0)
                            sobelY = cv2.Sobel(img,cv2.CV_64F,0,1)
                            sobelX = np.uint8(np.absolute(sobelX))
                            sobelY = np.uint8(np.absolute(sobelY))

                            sobel = cv2.bitwise_or(sobelX,sobelY)

                            resultado = np.vstack([
                                np.hstack([img,sobelX]),
                                np.hstack([sobelY,sobel])
                            ])

                            cv2.imshow("Sobel",resultado)
                            cv2.waitKey(0)

    # O filtro Laplaciano não exige processamento individual horizontal e vertical como o
# Sobel. Um único passo é necessário para gerar a imagem abaixo. Contudo, também é
# necessário trabalhar com a representação do pixel em ponto flutuant de 64 bits com sinal para
    #depois converter novamente para inteiro sem sinal de 8 bits.
                        def filtroLaplaciano(self,img):

                            img = img[::2,::2]
                            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            lap = cv2.Laplacian(img,cv2.CV_64F)
                            lap = np.uint8(np.absolute(lap))
                            resultado = np.vstack([img,lap])
                            resultado_2 =np.hstack([img,lap])

                            cv2.imshow("Filtro Laplaciano",lap)
                            cv2.waitKey(0)

                        def cannyy(self,img):
                            img = img[::2,::2]

                            img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            suave = cv2.GaussianBlur(img,(7,7),0)
                            ret2, th3 = cv2.threshold(suave, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
                            canny1 = cv2.Canny(suave,20,120)
                            canny2 = cv2.Canny(th3,70,200)
                            canny3 = cv2.Canny(suave, 70, 200)

                            cv2.imshow("Detector de bordas CANNY",canny2)
                            cv2.waitKey(0)


if __name__ == '__main__':
    img = cv2.imread("../img/dados.jpg");#257
    obj = SegmentacaoEbordas();
    #obj.sobelMetodo(img)
    obj.filtroLaplaciano(img)
    obj.cannyy(img);