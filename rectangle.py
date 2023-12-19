# rectangle.py
import cv2
import numpy as np

def tile(img, temp, color, size):
    tmpx = 0
    tmpy = 0
    w, h = temp.shape[:-1]
    res = cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where(res >= threshold)

    result_dict = {}

    print("SIZE: %s" % size)
    for pt in zip(*loc):
        x = pt[0] - 33
        y = pt[1]
        if ((x + 40 >= tmpx and x - 40 <= tmpx) and (y + 40 >= tmpy and y - 40 <= tmpy)):
            continue
        tmpx = x
        tmpy = y
        cv2.rectangle(img, (pt[1], pt[0] - 33), (pt[1] + h, pt[0] + w), color, 1)
        print("x: %s y: %s" % (pt[1], (pt[0] - 33)))
        print("x: %s y: %s" % ((pt[1] + h) // 45, (pt[0] + w) // 45))

        key = f"SIZE {size}"
        value = ((pt[1] + h) // 45, (pt[0] + w) // 45)

        if key not in result_dict:
            result_dict[key] = []

        result_dict[key].append(value)

    return result_dict
