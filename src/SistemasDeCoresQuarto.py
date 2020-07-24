import  cv2
import numpy as np
class sistemasCores:
                    def altCores(self):
                        imagem = cv2.imread("../img/entrada.jpg")
                        cv2.imshow("Original",imagem)

                        gray = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
                        cv2.imshow("GRAY",gray)

                        hsv = cv2.cvtColor(imagem,cv2.COLOR_BGR2HSV);
                        cv2.imshow("HSV",hsv)

                        lab = cv2.cvtColor(imagem,cv2.COLOR_BGR2LAB)
                        cv2.imshow("L*a*b",lab)
                        cv2.waitKey(0)

                    def canaisSeparar(self):
#Como já sabemos uma imagem colorida no formato RGB possui 3 canais, um para
#cada cor. Existem funções do OpenCV que permitem separar e visualizar esses canais
#individualmente
                        imagem = cv2.imread("../img/entrada.jpg")
                        (canalAzul,canalVerde,canalVermelho) = cv2.split(imagem);
                        cv2.imshow("CanalAzul",canalAzul);
                        cv2.imshow("CanalVerde",canalVerde)
                        cv2.imshow("CanalVermelho",canalVermelho)

                        resultado = cv2.merge([canalAzul,canalVerde,canalVermelho])
                        cv2.imshow("Resultado",resultado);
                        cv2.waitKey(0)
                    def CanaisNasCoresOriginais(self):
                        img = cv2.imread("../img/entrada.jpg")
                        (canalAzul, canalVerde, canalVermelho) = cv2.split(img)
                        zeros = np.zeros(img.shape[:2], dtype="uint8")
                        cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))
                        cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))
                        cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))
                        cv2.imshow("Original", img)
                        cv2.waitKey(0)


if __name__ == '__main__':
        obj = sistemasCores();
        #obj.altCores();
        #obj.canaisSeparar()
        obj.CanaisNasCoresOriginais()

