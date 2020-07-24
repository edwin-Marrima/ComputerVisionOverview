#Um histograma é um gráfico de colunas ou de linhas que representa a distribuição dos
#valores dos pixels de uma imagem, ou seja, a quantidade de pixeis mais claros (próximos de
#255) e a quantidade de pixels mais escuros (próximos de 0).
import  cv2
from matplotlib import pyplot as plt
import numpy as np
class histo:
                def histogramaa(self):
                       img = cv2.imread("../img/entrada.jpg")
                       img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                       cv2.imshow("Imagem P&B",img)
                       #Função calcHist para calcular o hisograma da imagem
                       h = cv2.calcHist([img], [0], None, [256], [0,256])
                       plt.figure();
                       plt.title("Histograma P&B")
                       plt.xlabel("Intensidade")
                       plt.ylabel("Qtde de Pixels")
                       plt.plot(h)
                       plt.xlim([0,256])
                       #plt.hist(img.ravel(), 256, [0, 256]) #Também é possível plotar o histograma de outra forma, com a ajuda da função ‘ravel()’. Neste caso o eixo X avança o valor 255 indo até 300, espaço que não existem pixels.
                       plt.show()
                       cv2.waitKey(0)
                def histrogramaColorida(self):
                    #pag 28
                        img = cv2.imread("../img/entrada.jpg")
                        cv2.imshow("Imagem Colorida", img)

                        # Separa os canais
                        canais = cv2.split(img)
                        cores = ("b", "g", "r")
                        plt.figure()
                        plt.title("'Histograma Colorido")
                        plt.xlabel("Intensidade")
                        plt.ylabel("Número de Pixels")
                        for (canal, cor) in zip(canais, cores):
                                    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
                                    plt.plot(hist)
                                    plt.xlim([0, 256])
                        plt.show()
 #É possível realizar um cálculo matemático sobre a distribuição de pixels para
 #aumentar o contraste da imagem. A intenção neste caso é distribuir de forma mais uniforme as
 #intensidades dos pixels sobre a imagem. No histograma é possível identificar a diferença pois
 #o acumulo de pixels próximo a alguns valores é suavizado. Veja a diferença entre o
 #histograma original e o equalizado abaixo:
                def equalizacaoHistograma(self):
                        #ajustar contraste
                        img = cv2.imread("../img/entrada.jpg")
                        cv2.imshow("Imagem Colorida", img)
                        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        h_eq = cv2.equalizeHist(img)

                        plt.figure()
                        plt.title("Histograma equalizado");
                        plt.xlabel("Intensidade")
                        plt.ylabel("Qtde de Pixels")
                        #plt.hist(h_eq.ravel(),256,[0,256])
                        plt.xlim([0,256])
                        plt.show()
                        cv2.imshow("Imagem equllizada", img)
                        plt.figure()
                        plt.title("Histograma Original")
                        plt.xlabel("Intensidade")
                        plt.ylabel("Qtde de Pixels")
                        plt.hist(img.ravel(), 256, [0, 256])
                        plt.xlim([0, 256])
                        plt.show()
                        cv2.waitKey(0)









if __name__ == '__main__':
        obj = histo();
        #obj.histogramaa()
        #obj.histrogramaColorida()
        obj.equalizacaoHistograma()

