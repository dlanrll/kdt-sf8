import cv2
import numpy as np

# ----------------------------------------------
# 기본창 띄우기
# image = cv2.imread("Cat03.jpg", cv2.IMREAD_COLOR)  # cv2.IMREAD_COLOR : 기본값(생략가능)
# gray_image = cv2.imread("Cat03.jpg", cv2.IMREAD_GRAYSCALE)

# cv2.imshow("Color Image", image)
# cv2.imshow("Gray Image", gray_image)

# # cv2.waitKey(0)  # 0: 창을 무한대기
# key = cv2.waitKey(0)
# if key == ord("q"):  # ord() : 문자의 아스키코드값 획득
#     print(chr(key))  # chr() : 아스키코드값을 문자로 변경


# cv2.destroyAllWindows()  # 모든창 종료
# -------------------------------------------------
# # 도형그리기
# width = 500
# height = 500
# canvas = np.zeros((height, width, 3), dtype=np.uint8)

# # 직선그리기(그릴캔버스, 시작점, 끝점, 색상, 두께)
# cv2.line(canvas, (50, 50), (450, 50), (0, 255, 0), 3)

# # 사작형그리기(캔버스, 왼쪽상단, 오른쪽하단, 색상, 두께)
# cv2.rectangle(canvas, (50, 100), (200, 250), (255, 0, 0), 2)

# # 원 그리기(캔버스, 중심좌료, 반지름, 색상, 두께)
# cv2.circle(canvas, (350, 350), 50, (0, 0, 255), -1)  # -1: 내부를 채운 원

# # 다각형 그리기
# pts = np.array([[250, 300], [350, 350], [150, 400], [100, 350]])  # (3, 2)
# # reshape : 배열의 형태를 변경
# pts = pts.reshape((-1, 1, 2))  # -1 :자동맞춤 -> (3, 1, 2)
# # -1로 써주는이유: 점 개수의 상관없이 자동으로 크기를 조절
# cv2.polylines(canvas, [pts], isClosed=True, color=(255, 255, 0), thickness=2)

# # 텍스트추가
# cv2.putText(
#     canvas,
#     "Hello OpenCV",
#     (120, 450),
#     cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
#     1,
#     (255, 255, 255),
#     2,
# )

# # FONT_HERSHEY_SIMPLEX: 기본값, 산세리프 폰트 san-serif
# # FONT_HERSHEY_PLAIN : 작은크기의 산세리프 폰트
# # FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체


# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ---------------------------------------------------------------
# # 이미지 색상, 사이즈 변경
# image = cv2.imread("Cat03.jpg")

# gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # resized = cv2.resize(image, (400, 300)) # 고정값으로 변경
# scale = 0.5  # 50%
# resized = cv2.resize(image, None, fx=scale, fy=scale)

# # cv2.imwrite("CatResize.jpg", resized) # 저장


# cv2.imshow("Gray", gray)
# # cv2.imshow("HSV", hsv)
# # cv2.imshow("Resize", resized)
# roi = image[200:400, 200:400].copy()
# cv2.imshow("Roi", roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)
# -----------------------------------------------------
# # x값, y값 찾기, 영역설정
# start, end = None, None


# def mouse_click(e, x, y, flag, param):
#     global start, end
#     if e == cv2.EVENT_LBUTTONDOWN:  # 클릭을 누른상태
#         print(f"마우스 누른상태 : x={x}, y={y}")
#         start = (x, y)
#     elif e == cv2.EVENT_LBUTTONUP:  # 클릭을 뗀 상태
#         print(f"마우스 뗀 상태 : x={x}, y={y}")
#         end = (x, y)
#         # 영역표시
#         roi = image[start[1] : end[1], start[0] : end[0]]
#         cv2.imshow("select", roi)


# image = cv2.imread("Cat03.jpg")
# cv2.imshow("image", image)

# # 마우스 콜백함수
# cv2.setMouseCallback("image", mouse_click)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# ---------------------------------------------------
# 회전, 이동
image = cv2.imread("Cat03.jpg")

# 중심좌표
(h, w) = image.shape[:2]
center = (w // 2, h // 2)
print(center)

# 회전
# matrix = cv2.getRotationMatrix2D(
#     center, 180.0, 1.0
# )  # 이미지 회전, 이동을 위해 사용하는 메서드
# rotated = cv2.warpAffine(image, matrix, (w, h))

# 이동
matrix = np.float32([[1, 0, 100], [0, 1, 50]])
move = cv2.warpAffine(image, matrix, (w, h))


# cv2.imshow("rotate", rotated)
cv2.imshow("move", move)
cv2.waitKey(0)
cv2.destroyAllWindows()

