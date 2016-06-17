import cv2
import numpy as np
from man_hands import cor_hands
from outer import encContour
img=cor_hands('scaled_mfrontf1.jpg', 'mside.jpg','pri_front.jpg', 'p_side.jpg')
cv2.imwrite('TEST_new.jpg',img)
