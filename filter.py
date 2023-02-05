import cv2
import numpy as np
from math import ceil




def noise_canceling(path, k = 4):
    read_img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    result_img = np.zeros(read_img.shape, dtype=np.uint8)
    for i in range(0, read_img.shape[0]):
        for j in range(0, read_img.shape[1]):
            if k < j and k < read_img.shape[1]-k:
                sorted_list = np.sort(read_img[i][j-k:j+k+1])
                mid = ceil(sorted_list.shape[0]/2)
                result_img[i][j] = sorted_list[mid]
            elif k > j:
                sorted_list = np.sort(read_img[i][0:j+k+1])
                mid = ceil(sorted_list.shape[0]/2)
                result_img[i][j] = sorted_list[mid]
            elif k > read_img.shape[1]-k:
                sorted_list = np.sort(read_img[i][j-k:read_img.shape[1]])
                mid = ceil(sorted_list.shape[0]/2)
                result_img[i][j] = sorted_list[mid]



    return result_img






 
cv2.imshow('resualt', noise_canceling("path", 5))
cv2.waitKey(0)
cv2.destroyAllWindows()