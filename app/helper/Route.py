class Route:
    """
    클라스: 루트
    기능: 도시간 루트를 관리하는 클래스
    인자: 루트 매니저, 도시 딕셔너리
    함수: __len__,
          __getitem__,
          __setitem__,
          shuffleCities,
          updateCities,
          getCity,
          setCity,
          getFitness,
          getDistance,
          containsCity,
          toString
    """
    
    def __init__(self):
        """
        TODO:
        생성자: Route 객체 초기화
        기능: 루트를 초기화
        인스턴스 변수: 루트 매니저, 도시 딗셔너리, 거리, 피트니스
        
        만약 도시 딕셔너리가 인자에 없다면, 도시 딕셔너리에 루트 매니저의 도시들만큼 랜덤도시 추가
        """
        
    def __len__(self):
        """
        TODO:
        함수: 루트 길이 반환
        기능: 루트의 길이를 반환
        반환: 루트 길이
        """
        
        return

    def __getitem__(self):
        """
        TODO:
        함수: 특정 인덱스의 도시 반환
        인자: 인덱스
        기능: 특정 인덱스의 도시를 반환
        반환: 특정 인덱스의 도시
        """
        
        return
    
    def __setitem__(self):
        """
        TODO:
        함수: 특정 인덱스의 도시 설정
        인자: 인덱스 (Key), 도시 (Value)
        기능: 특정 인덱스의 도시를 설정
        반환: 없음
        """
        
        return
    
    def shuffleCities(self):
        """
        TODO:
        함수: 루트의 도시들을 섞음
        기능: 루트의 도시들을 섞음
        반환: 없음
        """
        
        return
    
    def updateCities(self):
        """
        TODO:
        함수: 루트의 도시들을 업데이트
        기능: 루트의 도시들을 루트 매니저의 도시들로 업데이트
        반환: 불리언 값 (성공 여부)
        """
    
        return
    
    def getCity(self):
        """
        TODO:
        함수: 특정 루트 포지션 의 도시 반환
        인자: 루트 포지션
        기능: 특정 포지션의 도시를 반환
        반환: 특정 포지션의 도시
        """
        
        return
    
    def setCity(self):
        """
        TODO:
        함수: 특정 루트 포지션에 도시 설정
        인자: 루트 포지션, 도시
        기능: 특정 루트 포지션에 도시를 설정하고 피트니스와 거리를 업데이트 (0 으로)
        반환: 어떤 값도 반환하지 않음
        """
    
    def getFitness(self):
        """
        TODO:
        함수: 루트의 피트니스 반환
        기능: 루트의 피트니스를 반환 (만약 피트니스가 0이면 --> 거링의 역수 [1/거리])
        반환: 루트의 피트니스
        """
        
        return
    
    def getDistance(self):
        """
        TODO:
        함수: 루트의 거리 반환
        기능: 루트의 거리를 반환 (루트의 모든 도시들의 거리 합)
        반환: 루트의 거리
        """
        
        return
    
    def containsCity(self):
        """
        TODO:
        함수: 특정 도시 포함 여부 반환
        인자: 도시
        기능: 특정 도시가 루트에 포함되어 있는지 여부를 반환
        반환: 불리언 값 (포함 여부)
        """
        
        return
    
    
        
    
    