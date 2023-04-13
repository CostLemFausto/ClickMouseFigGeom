import cv2 as cv

def Retangulo(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.rectangle(img,(x,y),(15+x,35+y),(200,0,0),1) # cria retângulo
        #cv.circle(img=img, center=(x,y), radius=50, color=(0,200,0), thickness=5)

cv.namedWindow(winname='imagem')
cv.setMouseCallback('imagem', Retangulo )
img = cv.imread("/home/takion/Documentos/Pixel/clin2.PNG")

while True:    
    cv.imshow("imagem", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()