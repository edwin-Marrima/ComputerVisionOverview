import  cv2

class testePrimeiro:

                    def testeUM(self):
                                print("ola");
                                #Leitura de uma imagem com a funcao iamread()
                                imagem = cv2.imread('../entrada.jpg');
                                print("Largura em pixels:", end='')
                                print(imagem.shape[1]);#largura da imagem
                                print("Altura em Pixels:", end='')
                                print(imagem.shape[0]) #altura da imagem
                                print("Qtde de canais:", end='')
                                print(imagem.shape[2])


                                #Mostrar a imagem com a funcao iamshow
                                cv2.imshow("Mostra imagem",imagem)
                                cv2.waitKey(0) #espera pressionar qualquer tecla

                                #salvar a imagem no disco
                                cv2.imwrite("sss.jpg",imagem)
                                print("done")

                    def manipulacaoPixels(self):
                                # Leitura de uma imagem com a funcao iamread()
                                imagem = cv2.imread('../img/azul.jpg');
                                (b,g,r) = imagem[0,0];
                                print("O pexel (0,0) tem as seguintes corres:")
                                print('Vermelho:', r, 'Vede:',g, 'Azul:',b)
                    def alterarCorDeImagem(self):
                                imagem = cv2.imread("../img/azul.jpg")
                                for y in range(0,imagem.shape[0],10) :#linhas, esse 10 eh pra djampar 10-10 linhas
                                    for x in range(0,imagem.shape[1],10): #colunas
                                        imagem[y,x] = (0,255,255);
                                cv2.imshow("Imagem modificada",imagem);
                                cv2.waitKey(0);
                    def fatiamentoDesenhoSobreImagem(self):
                                # fatiamento e desenho sobre imagem
                                    imagem = cv2.imread("../img/entrada.jpg")
                                    foto = imagem;
                                    foto1 = imagem;
                                    imagem[100:150,:] = (0,255,0);
                                    foto[100:190, 50:100] = (255, 255, 255);
                                    #foto1[:,200:220] = (0,255,0);
                                    cv2.imshow("Imagem modificada",imagem);
                                    cv2.waitKey(0);

                    def desenhoLinhasCirculos(self):
                                    red = (0,0,255)
                                    verde = (0,255,0)
                                    azul = (255,0,0)
                                    imagem=cv2.imread("../img/entrada.jpg")
                                    cv2.line(imagem,(60,40),(60,400),verde,5)
                                    cv2.line(imagem,(300,200),(150,150),red,3)
                                    cv2.rectangle(imagem,(20,20),(150,50),azul)
                                    cv2.circle(imagem,(100,120),50,red)
                                    (x, y) = (imagem.shape[1] // 2, imagem.shape[0] // 2);
                                    for raio in range(0, 175, 15):
                                        cv2.circle(imagem, (x, y), raio,azul,3)
                                    # x=30//2; valor medio
                                    # cv2.line(imagem,(x,y)(x1,y1),cor,grossura);



                                    cv2.imshow("Desenho",imagem)
                                    cv2.waitKey(0);
                    def escreverTextos(self):
                                    imagem = cv2.imread("../img/entrada.jpg")
                                    fonte = cv2.FONT_HERSHEY_SIMPLEX
                                    cv2.putText(imagem, 'OpenCV', (15, 65), fonte, 2, (255, 0, 255), 2, cv2.LINE_AA)
                                    cv2.imshow("Ponte",imagem)
                                    cv2.waitKey(0)





if __name__ == '__main__':
        testeprimeiro = testePrimeiro();
       # testeprimeiro.testeUM();
        #testeprimeiro.manipulacaoPixels()
        #testeprimeiro.alterarCorDeImagem();
        testeprimeiro.fatiamentoDesenhoSobreImagem();
        #testeprimeiro.desenhoLinhasCirculos();
        #testeprimeiro.escreverTextos();