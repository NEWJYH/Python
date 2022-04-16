# 스레드 실습-2
# join()메소드 : 모든 서브(작업)스레드가 작업을 마칠 때까지 기다리라는 것을 의미한다.
# 보통 데이터를 여러 스레드를 통해서 병렬로 처리한 후 그 값들을 다시 모아서 순차적으로
# 처리해야할 필요성이 있을 때 분할한 데이터가 모든 스레드에서 처리될 때까지 기다렸다가
# 메인 스레드가 다시 추후 작업을 하는 경우에 통상적으로 많이 사용된다.
import threading
import time


# 스레드 클래스 정의
# 스레드가 되기 위해서는 threading.Thread 클래스를 상속을 반드시 받았야 한다.
class Worker(threading.Thread):
    # 생성자
    def __init__(self, name):
        super().__init__()  # 조상클래스 생성자 호출
        self.name = name    # 스레드 이름

    # CPU 스케쥴러에 따라서 특정 스레드가 먼저 시작하였다 하더라도 CPU스케쥴러에 따라서
    # 종료하는 스레드의 순서가 얼마든지 바뀔수가 있다.
    def run(self):
        print("작업스레드 시작 : ", threading.currentThread().getName())
        time.sleep(5)  # 5초간 스레드 일시정지
        print("작업스레드 종료 : ", threading.currentThread().getName())

if __name__ == "__main__":
    print("메인스레드 시작")
    # 3개의 스레드가 생성되고 시작된다.
    t1 = Worker("1")        # 작업스레드를 생성
    t1.start()              # run()메소드를 자동 호출
    t2 = Worker("2")        # 작업스레드를 생성
    t2.start()              # run()메소드를 자동 호출
    t3 = Worker("3")        # 작업스레드를 생성
    t3.start()              # run()메소드를 자동 호출

    # 작업스레드가 join()를 호출하는 지점에서 메인스레드가 기다린다.
    t1.join()               # t1스레드가 종료될 때까지 기다려라라는 의미
    t2.join()               # t2스레드가 종료될 때까지 기다려라라는 의미
    t3.join()               # t3스레드가 종료될 때까지 기다려라라는 의미
    print("메인스레드 종료")