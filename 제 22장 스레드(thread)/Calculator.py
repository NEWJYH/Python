# 동기화 실습(파일분리-Calulator.py, User-1.py, User-2.py, CalculatorMain.py)

# 공유 객체를 만든다.
import threading
import time

lock = threading.Lock()

class Calculator():
    # 생성자, 초기화 처리
    def __init__(self, memory):
        super().__init__()
        self.memory = memory
    # getter() 작성
    def getMemory(self):
        return self.memory

    # setter() 작성
    # 데이터의 신뢰성을 보장하기 위해서 특정 스레드가 접근해서 작업을 하고 있는 동안은
    # lock.acquire()메소드가 다른 스레드의 접근을 막아줌으로써 데이터의 신뢰성을 보
    # 장할 수가 있다.(동기화 처리)속도적인 측면은 조금은 느릴 수 있다.
    def setMemory(self, memory):
        lock.acquire()     # 잠금 발생
        self.memory = memory
        # 1초간 일시정지
        time.sleep(1)
        # 현재 실행 중인 스레드 이름과 memory 값을 출력
        print(threading.currentThread().getName() + ":", self.memory)
        lock.release()  # 잠금 해제