import cv2

# 경로찾기
# print(cv2.data.haarcascades)

# # haar cascade xml 파일 로드
# cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# # 사람이미지
# image = cv2.imread("skin2.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # BGR -> GRAY

# # 얼굴감지
# # scaleFactor : 이미지의 크기를 줄여가며서 객체를 찾는 비율(1.1 ~ 1.3)
# # minNeighbors : 객체로 인정하기 위한 최소의 사각형 개수(3, 5, 7)
# # minSize : 감지할 최소 객체 크기(너무작은 객체는 무시)
# # maxSize : 감지할 최대 객체 크기(너무 큰 객체 무시)
# # detectMultiScale() 메서드의 반환값 (x, y, widht, height)
# faces = cascade.detectMultiScale(
#     gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
# )

# # 탐지된 얼굴에 사각형 그리기
# for x, y, w, h in faces:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow("face", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------- 웹캠이용
# # haar cascade xml 파일 로드
# cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("웹캠이 없습니다")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # 그레이스케일로 변환
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # 얼굴탐지
#     faces = cascade.detectMultiScale(
#         gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
#     )

#     for x, y, w, h in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     cv2.imshow("face", frame)

#     # 종료
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

# ----------------------- 눈 검출
# # 얼굴
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )
# # 눈
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


# image = cv2.imread("skin2.png")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # 얼굴탐지
# faces = face_cascade.detectMultiScale(
#     gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
# )

# # 얼굴
# for x, y, w, h in faces:
#     # 얼굴에 사각형
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

#     # 눈탐지
#     # 얼굴roi
#     face_roi = gray[y : y + h, x : x + w]
#     eyes = eye_cascade.detectMultiScale(
#         face_roi, scaleFactor=1.1, minNeighbors=7, minSize=(15, 15)
#     )

#     for ex, ey, ew, eh in eyes:
#         cv2.rectangle(
#             image, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2
#         )


# cv2.imshow("eyes", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------- 웹캠이용
# 얼굴
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
# 눈
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠이 없습니다")
    exit()


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 얼굴탐지
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )

    # 얼굴
    for x, y, w, h in faces:
        # 얼굴에 사각형
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 눈탐지
        # 얼굴roi
        face_roi = gray[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(
            face_roi, scaleFactor=1.1, minNeighbors=7, minSize=(15, 15)
        )

        for ex, ey, ew, eh in eyes:
            cv2.rectangle(
                frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (255, 0, 0), 2
            )

    cv2.imshow("face", frame)

    # 종료
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()