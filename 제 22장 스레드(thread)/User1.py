# Calculator 공유객체에 접근하는 스레드 클래스 작성
import threading

from Calculator import *

class User1(threading.Thread):
    def __init__(self):
        super().__init__()

    def setCalculator(self, calculator):
        # 메인에서 생성한 calculator 인스턴스를 매개변수 받아서 접근함
        self.calculator = calculator
        self.setName("User-1")   # 스레드 이름을 설정

    def run(self):
        self.calculator.setMemory(100)