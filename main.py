import cv2

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    qcd = cv2.QRCodeDetector()
    decoded_info, points, _ = qcd.detectAndDecode(img)
    
    if decoded_info:
        points = points.astype(int)
        cv2.polylines(img, points, True, (255,0,0), 2)
        cv2.putText(img, decoded_info, (0,30), 1, 2, (255,0,0), 2)

    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()