class Population:
    """
    클라스: 포퓰레이션 (루트 학습 매니저)
    인자: 루트 매니저, 포퓰레이션 사이즈, 초기화 여부
    함수: __setitem__,
          __getitem__,
          saveRoute,
          getFittest,
          populationSize,
    """
    
    def __init__(self):
        """
        TODO:
        생성자: 인스턴스화된 특정 클래스 객체
        인자: 루트 매니저 (Route Manager), 포퓰레이션 사이즈 (Integer), 초기화 여부 (boolean)
        인스턴스 변수: 루트 리스트 (Route 객체 리스트)
        
        만약에 초기화 여부가 True 라면 포퓰레이션 사이즈 만큼 Route 객체를 만들어서 저장
        """

    def __setitem__(self, key, value):
        """
        TODO:
        함수: 루트 리스트에 Route 객체 추가
        인자: key (Integer), value (Route 객체)
        """
        
    def __getitem__(self, key):
        """
        TODO:
        함수: 루트 리스트에서 Route 객체 반환
        인자: key (Integer) / index
        반환: 루트 리스트에서 key 번째 Route 객체 반환
        """
        
        return
    
    def saveRoute(self, index, route):
        """
        TODO:
        함수: 루트 리스트에 Route 객체 추가
        인자: index (Integer), route (Route 객체)
        반환: 불리언 (성공 여부)
        """
        
        return

    def getFittest(self):
        """
        TODO:
        함수: 루트 리스트에서 가장 적합한 (피트니스가 가장 낮은) Route 객체 반환
        반환: Route 객체
        """
        
        return
    
    def populationSize(self):
        """
        TODO:
        함수: 루트 리스트의 길이 반환
        반환: 루트 리스트의 길이 (Integer)
        """
        
        return

    
    
        
        
