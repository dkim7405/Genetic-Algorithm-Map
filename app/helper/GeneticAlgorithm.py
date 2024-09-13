class GeneticAlgorithm:
    """
    클라스: 유전 알고리즘
    인자: 루트 매니저, 유전 알고리즘 설정들 (돌연변이율, 토너먼트 크기, 엘리티즘 사용 여부)
    함수: evolvePopulation, crossover, mutate, tournamentSelection
    
    탐색 알고리즘으로, 자연 선택과 유전학의 개념을 모방합니다
    """
    
    def __init__(self):
        """
        TODO:
        생성자: 인스턴스화된 특정 클래스 객체
        인자: 루트 매니저 (Route Manager), 유전 알고리즘 설정들 (돌연변이율 Float, 토너먼트 크기 Integer, 엘리티즘 사용 여부, Boolean)
        기본값: 돌연변이율 = 0.005 ~ 0.015, 토너먼트 크기 = 5, 엘리티즘 사용 여부 = True
        인스턴스 변수: 루트 매니저 (Route Manager), 돌연변이율 (Float), 토너먼트 크기 (Integer), 엘리티즘 사용 여부 (Boolean)
        """
        
    def evolvePopulation(self):
        """
        TODO:
        함수: 포퓰레이션 진화
        인자: Population 객체 / 루트들
        반환: 새로운 포퓰레이션 (Population 객체 / 루트들)
        
        self.crossover() 함수를 사용해서 루트들을 교차시키기
        self.mutate() 함수를 사용해서 루트들을 변이시키기
        
        마지막으로 하는거 추천
        """
        
        return
    
    def crossover(self):
        """
        TODO:
        함수: 루트 교차
        인자: parent1 (Route 객체), parent2 (Route 객체)
        반환: child (Route 객체)
        
        루트 교차는 두 루트를 사용해서 새로운 루트를 만드는 함수
        스타트 포지션이랑 엔드 포지션을 랜덤으로 정해서, 그 사이에 부모 루트를 넣음
        """
        
        return

    def mutate(self):
        """
        TODO:
        함수: 루트 변이
        인자: route (Route 객체)
        반환: 불리언 (성공 여부)
        
        루트 변이는 루트를 랜덤하게 바꾸는 함수
        루트 변이율의 확률로 랜덤한 두 루트의 위치를 바꿈
        """
        
        return
    
    def tournamentSelection(self):
        """
        TODO:
        함수: 토너먼트 선택
        인자: population (Population 객체)
        반환: Route 객체
        
        토너먼트 선택은 루트들 중에서 포퓰래이션에 있는 루트들을 토너먼트 크기만큼 랜덤으로 선택해서, 그중 가장 적합한 루트를 찾는 함수
        """
        
        return