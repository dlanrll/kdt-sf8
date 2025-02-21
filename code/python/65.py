import cv2
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------실습
plt.ion()  # matplotlib 인터렉티브 모드 활성화(실시간 업데이트)

# 종료 플래그
quit_cap = False


# matplotlib 이벤트 핸들러
def on_key(e):
    global quit_cap
    if e.key == "q":
        quit_cap = True


plt.figure(figsize=(12, 4))
# 키이벤트 연결
plt.gcf().canvas.mpl_connect("key_press_event", on_key)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("웹캠을 열수없습니다.")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # matplotlib 3개의 영상 실시간 업데이트
    plt.clf()  # 기존의 그래프 초기화

    # 원본
    original = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 예시로 이미지를 제출할때
    cv2.imwrite("orginal.jpg", cv2.cvtColor(original, cv2.COLOR_RGB2BGR))

    plt.subplot(1, 3, 1)
    plt.imshow(original)
    plt.title("original")
    plt.axis("off")

    # 손 윤곽선 검출
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 그레이스케일 변환
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 이진화처리
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )  # 컨투어탐지
    contour_img = frame.copy()  # 원본을 복사해서 사용
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)  # 컨투어 그리기
    contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

    plt.subplot(1, 3, 2)
    plt.imshow(contour_img)
    plt.title("contour")
    plt.axis("off")

    # 샤프닝 필터 적용
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    sharpened = cv2.filter2D(contour_img, -1, kernel)

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened)
    plt.title("sharp")
    plt.axis("off")

    # 업데이트 간격을 조절
    plt.pause(0.01)
    plt.show()

    # # 종료
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break
    if quit_cap:
        print("종료합니다")
        break

cap.release()
cv2.destroyAllWindows()
plt.close("all")  # 모든 matplotlib 닫기