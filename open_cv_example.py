import cv2 as cv
card = "card.png"

# To open image in gray mode
# img = cv.imread(card, 0)
img = cv.imread(card)


def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


resize_img = rescaleFrame(img)
font = cv.FONT_HERSHEY_SIMPLEX
org = (0, 50)
fontScale = 1
color = (255, 0, 0)
cv.putText(resize_img, "Borko", org, font,
           fontScale, color, 2, cv.LINE_AA)
cv.imshow("Card", resize_img)

cv.waitKey(0)
cv.destroyAllWindows()
