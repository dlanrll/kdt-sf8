# import cv2

# # 이미지 읽고 크기 출력
# image = cv2.imread('image.png')
# (h, w) = image.shape[:2]
# print(h, w)

# # 흑백 변환 및 화면 표시
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 50% 크기로 축소하여 새 창에 표시
# scale = 0.5
# resized = cv2.resize(image, None, fx=scale, fy=scale)
# cv2.imshow("50%", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 90도 회전 후 저장
# center = (w // 2, h // 2)
# matrix = cv2.getRotationMatrix2D(center, 90, 1.0)
# rotated = cv2.warpAffine(image, matrix, (w, h))
# cv2.imwrite("/mnt/data/image_rotated.png", rotated)



import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("f.jpg")

# HSV 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 초록색 범위 설정 (조정 필요)
lower_green = np.array([35, 50, 50])   
upper_green = np.array([85, 255, 255])

# 초록색 영역 마스크 생성
mask = cv2.inRange(hsv, lower_green, upper_green)

# **노이즈 제거 (블러 + 모폴로지 연산)**
mask = cv2.GaussianBlur(mask, (5, 5), 0)  # 블러 적용
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))  # 작은 점 제거

# 윤곽선 검출
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# **작은 노이즈 제거**
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]  # 100픽셀 이하 제거

# 초록색 개수 출력
print(f"검출된 초록색 물체 개수: {len(filtered_contours)}")

# 윤곽선 및 바운딩 박스 그리기
output = image.copy()
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 결과 시각화
cv2.imshow("Original", image)
cv2.imshow("Green Mask", mask)
cv2.imshow("Detected Contours", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
