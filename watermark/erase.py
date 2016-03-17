import cv2
import numpy as np
src = cv2.imread('test.jpg')
watermark = cv2.imread('watermark.jpg',0)
watermark_height = watermark.shape[0]
watermark_width = watermark.shape[1]
src_height = src.shape[0]
src_width = src.shape[1]
begin_row = src_height/2 - watermark_height/2
end_row = src_height/2+watermark_height/2
begin_col = src_width/2 - watermark_width/2
end_col = src_width/2 + watermark_width/2
roi = src[begin_row:end_row, begin_col:end_col]
thresh_val, mask = cv2.threshold(watermark, 210, 255, cv2.THRESH_BINARY)
for i in range(3):
    dst = cv2.inpaint(roi, mask, 5, cv2.INPAINT_TELEA)
    roi = dst
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
