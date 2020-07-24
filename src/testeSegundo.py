import  cv2
import numpy as np

class TesteSEGUNDO:

                        def cortarImagem(self):
                             imagem = cv2.imread("../img/entrada.jpg")
                             recorte = imagem[100:200,100:200]
                             cv2.imshow("Imagemm cortada",recorte);
                             cv2.waitKey(0);
                        def redimensionar(self):
                            imagem = cv2.imread("../img/entrada.jpg")
                            cv2.imshow("OriginalImage",imagem);
                            largura = imagem.shape[1];
                            altura = imagem.shape[0];
                            proporcao = float(altura/largura)
                            largura_nova = 320 #em pixels
                            altura_nova = int(largura_nova*proporcao);
                            tamanho_novo=(largura_nova,altura_nova);
                            img_redimensionada = cv2.resize(imagem,tamanho_novo,interpolation=cv2.INTER_AREA)
                            cv2.imshow("resultado",img_redimensionada);
                            cv2.waitKey(0)
                        def redimensionarMetodoDois(self):
                            imagem = cv2.imread("../img/entrada.jpg")
                            cv2.imshow("Original",imagem)
                            img_redimesionada = imagem[::2,::2];
                            cv2.imshow("Nova",img_redimesionada);
                            cv2.waitKey(0)
                        def espelharImagem(self):
                            imagem = cv2.imread("../img/entrada.jpg")
                            cv2.imshow("Original", imagem)
         #HORIZONTAL
                            flip_horizontal = imagem[::-1,:] #comando equivaleente abaixo
                            #flip_horizontal = cv2.flip(imagem,1);
                            cv2.imshow("Invertida_horizontal",flip_horizontal);
        #VERTICAL
                            flip_vertical = imagem[:,::-1] #comando equivalente abaixo
                            #flip_vertical=cv2.flip(imagem,0);
                            cv2.imshow("Invertida_veritical", flip_vertical);
        #VERTICAL/HORIZONTAL
                            flip_hv = imagem[::-1,::-1] #comando equivalente abaixo
                            flip_hv = cv2.flip(imagem,-1)
                            cv2.imshow("Horizontal vertical",flip_hv);

                            cv2.waitKey(0)
                        def rodar(self):
                            imagem = cv2.imread("../img/entrada.jpg")
                            cv2.imshow("Original", imagem)
                            (alt,lar) = imagem.shape[:2] # caputra altur e alg
                            centro = (lar//2,alt//2)  #acha o centro
                            M = cv2.getRotationMatrix2D(centro,30,1.0) #30graus
                            img_rodada = cv2.warpAffine(imagem,M,(lar,alt));
                            cv2.imshow("imagem rotacionada",img_rodada);
                            cv2.waitKey(0)

if __name__=='__main__':
        testesegundo = TesteSEGUNDO();
        #testesegundo.cortarImagem();
        #testesegundo.redimensionar();
        testesegundo.redimensionarMetodoDois()
        #testesegundo.espelharImagem();
        #testesegundo.rodar()
