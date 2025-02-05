import requests
from bs4 import BeautifulSoup
from tkinter import Tk, Label, Entry, Button, Text, END

def get_lotto_numbers(round_number):
    try:
        # 로또 회차 정보 URL
        url = f"https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round_number}"
        response = requests.get(url)
        response.raise_for_status()  # HTTP 에러 체크
        data = response.json()

        # 번호 파싱
        if data['returnValue'] == 'success':
            winning_numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]
            bonus_number = data['bnusNo']
            return winning_numbers, bonus_number
        else:
            return None, None
    except Exception as e:
        return None, None

def show_result():
    round_number = entry.get()
    if not round_number.isdigit():
        result_text.delete('1.0', END)
        result_text.insert(END, "올바른 회차를 입력하세요!")
        return

    winning_numbers, bonus_number = get_lotto_numbers(round_number)
    result_text.delete('1.0', END)

    if winning_numbers:
        result_text.insert(END, f"당첨 번호: {winning_numbers}\n")
        result_text.insert(END, f"보너스 번호: {bonus_number}")
    else:
        result_text.insert(END, "해당 회차 정보를 찾을 수 없습니다!")

root = Tk()
root.title("로또 당첨 확인")

Label(root, text="당첨 회차 입력").grid(row=0, column=0)
entry = Entry(root)
entry.grid(row=0, column=1)
Button(root, text="당첨 번호 확인", command=show_result).grid(row=0, column=2)

result_text = Text(root, height=5, width=50)
result_text.grid(row=1, column=0, columnspan=3)

root.mainloop()
