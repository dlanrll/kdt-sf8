# 실습1. 상속과 오버라이딩
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, change):
        self.stock += change
        action = "추가" if change > 0 else "감소"
        print(f"{self.name}의 재고가 {abs(change)}개 {action}되었습니다. 현재 재고: {self.stock}개")

    def show_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.stock}개")


class Electronic(Product):
    def __init__(self, name, price, stock, warranty=12):
        super().__init__(name, price, stock)
        self.warranty = warranty

    def extend_warranty(self, additional_months):
        self.warranty += additional_months
        print(f"{self.name}의 보증 기간이 {additional_months}개월 연장되었습니다. 현재 보증 기간: {self.warranty}개월")

    def show_info(self):
        super().show_info()
        print(f"보증 기간: {self.warranty}개월")


class Food(Product):
    def __init__(self, name, price, stock, expiry_date):
        super().__init__(name, price, stock)
        self.expiry_date = expiry_date

    def check_expiry(self, today):
        today_year, today_month, today_day = map(int, today.split('-'))
        expiry_year, expiry_month, expiry_day = map(int, self.expiry_date.split('-'))
        if (today_year, today_month, today_day) > (expiry_year, expiry_month, expiry_day):
            print(f"{self.name}는 유통기한이 지났습니다.")
        else:
            print(f"{self.name}는 유통기한이 지나지 않았습니다.")

    def show_info(self):
        super().show_info()
        print(f"유통기한: {self.expiry_date}")


electronic_item = Electronic("스마트폰", 1000000, 10, 24)
electronic_item.show_info()
electronic_item.extend_warranty(12)
electronic_item.show_info()

food_item = Food("바나나", 5000, 100, "2025-02-01")
food_item.check_expiry("2025-01-14")
food_item.show_info()


# 실습2. 클래스종합 프로그래밍

# 부모 클래스: ElectricityData
class ElectricityData:
    def __init__(self):
        self.usage_data = []
        self.total_usage = 0.0

    # 총 전력 사용량 계산 (소숫점 두 번째 자리 반올림)
    def calculate_total_usage(self):
        self.total_usage = round(sum(item['usage'] for item in self.usage_data), 2)
        return self.total_usage

    # 특정 날짜의 사용량 반환
    def get_usage_on_date(self, date):
        for item in self.usage_data:
            if item['date'] == date:
                return item['usage']
        return None

    # 새로운 사용량 추가
    def add_usage(self, date, usage):
        self.usage_data.append({'date': date, 'usage': usage})
        self.calculate_total_usage()

    # 특정 날짜의 사용량 삭제
    def remove_usage(self, date):
        self.usage_data = [item for item in self.usage_data if item['date'] != date]
        self.calculate_total_usage()


# 자식 클래스: HomeElectricityData
class HomeElectricityData(ElectricityData):
    # 특정 날짜 범위 내 데이터 필터링
    def filter_usage_by_date_range(self, start_date, end_date):
        return [
            item for item in self.usage_data
            if start_date <= item['date'] <= end_date
        ]

    # 가장 높은 사용량과 해당 날짜 반환
    def get_max_usage(self):
        if not self.usage_data:
            return None
        max_usage_item = max(self.usage_data, key=lambda x: x['usage'])
        return max_usage_item


# 테스트 코드
if __name__ == "__main__":
    # 객체 생성
    home_data = HomeElectricityData()
    
    # 데이터 추가
    home_data.add_usage("2024-11-01", 12.5)
    home_data.add_usage("2024-11-02", 15.3)
    home_data.add_usage("2024-11-03", 10.8)
    home_data.add_usage("2024-11-04", 14.2)
    home_data.add_usage("2024-11-05", 13.6)

    # 총 전력 사용량 출력
    print("총 전력 사용량:", home_data.calculate_total_usage())

    # 특정 날짜의 사용량 조회
    print("2024-11-03의 사용량:", home_data.get_usage_on_date("2024-11-03"))

    # 새로운 데이터 추가 및 총 사용량 갱신 확인
    home_data.add_usage("2024-11-06", 16.4)
    print("2024-11-06 추가 후 총 전력 사용량:", home_data.calculate_total_usage())

    # 특정 날짜 범위 내 사용량 출력
    print("특정 날짜 범위 내 사용량:", home_data.filter_usage_by_date_range("2024-11-02", "2024-11-04"))

    # 가장 높은 사용량 및 해당 날짜 출력
    print("가장 높은 사용량:", home_data.get_max_usage())
