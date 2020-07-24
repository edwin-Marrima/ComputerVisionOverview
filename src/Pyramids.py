import  cv2
#import mahotas
from matplotlib import pyplot as plt
import numpy as np
class pyramids:
                def pyramidsTest(self,img):
                    lower_reso = cv2.pyrDown(img)
                    higher_reso2 = cv2.pyrUp(lower_reso)
                    cv2.imshow("pyram",higher_reso2)

                    cv2.waitKey(0)

if __name__=='__main__':
    img = cv2.imread("../img/entrada.jpg");
    obj = pyramids()
    obj.pyramidsTest(img)