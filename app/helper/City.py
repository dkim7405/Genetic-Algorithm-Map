import random
import math

class City:
    """
    클라스: 도시
    인자: (x, y)
    함수: constructor, getX, getY, calculateDistanceTo, toString
    """
    
    # 인스턴스 변수 만들때 self 를 붙여야함 (Ex. self.number = 0)
    def __init__(self, x=None, y=None):
        """
        DONE:
        생성자: 인스턴스화된 특정 클래스 객체
        인자: X, Y 값 (객체 만들때 X 랑 Y 값을 받아서 인스턴스 변수에 저장해야함)
        만약에 X 랑 Y 값이 None 이라면 1 부터 200 까지 랜덤 돌려서 X 랑 Y 저장
        """
        if x == None and y == None:
            self.x = random.randint(1,200)
            self.y = random.randint(1,200)
        else:
            self.x = x
            self.y = y
        
    def getX(self):
        """
        DONE:
        함수: X 좌표 반환
        반환: 도시의 X 좌표 (정수)
        """
        
        return self.x

    def getY(self):
        """
        DONE:
        함수: Y 좌표 반환
        반환: 도시의 Y 좌표 (정수)
        """
        return self.y

    def calculateDistanceTo(self, other_city):
        """
        DONE:
        함수: 다른 도시와의 거리 계산
        인자: other_city (City 객체)
        반환: 현재 도시와 other_city 사이의 유클리드 거리 (실수)
        """
        
        distance = math.sqrt((self.x - other_city.x)**2 + (self.y - other_city.y)**2)
        return distance

    def toString(self):
        """
        함수: 도시 정보를 문자열로 반환
        반환: 도시의 X와 Y 좌표를 포함한 문자열
        """
        
        return f"[ City : (${self.x}, ${self.y}) ]"