# 앞선 예제의 문제점을 해결하는 예제
# 동기화 방법 중에서 Lock 클래스를 살펴보도록 한다.
# Lock 클래스는 특정 스레드가 변수를 사용하기 시작하면 다른 스레드는 대기 상태로 존재한다.
# Lock 클래스는 다른 스레드가 지금 사용하고 있는 스레드가 변수에 접근했다면 다른 스레드를
# 막아준다. 이런 것을 객체(전역변수) 잠금이라고 한다.
# Lock 클래스 메소드
# 1. Lock.aquire() : 잠금 역할을 하며, 다른 스레드들은 접근 못하게 막아준다.
# 아래 위, 두 개의 메소드 사이에 코드를 작성하면 된다.아울러 이런 영역을 임계영역이라고 한다.
# 2. Lock.release() : 해제 역할을 하면, 다른 스레드들이 접근을 하도록 허용한다.
# 속도는 조금 느릴 수 있으나 현 시대에서 데이터의 신뢰성이 가장 우선시 되어야 되기 때문에
# Lock 클래스를 이용할 수 밖에 없다.
import threading
totalCount = None
# 공유된 변수를 위한 클래스 작성
class ThreadVariable():
    def __init__(self):
        self.lock = threading.Lock()    # 멤버변수로 Lock 클래스의 인스턴스를 생성
        self.lockValue = 0
    # 누적시키는 메소드 정의(동기화 처리 메소드)
    def plus(self, value):
        self.lock.acquire()    # 다른 스레드들의 접근을 막음
        self.lockValue += value    # 1을 누적함
        self.lock.release()    # 다른 스레드들의 접근을 허용함.

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global totalCount
        for _ in range(250000):
            totalCount.plus(1)
        print("250,000번 누적 완료")

if __name__ == "__main__":
    totalCount = ThreadVariable()
    for _ in range(4):
        lockThread = CounterThread()
        lockThread.start()
    print("모든 스레드들이 종료될 때까지 기다립니다.")
    mainThread = threading.currentThread()
    for thread in threading.enumerate():
        if thread is not mainThread:
            thread.join()
    total = format(totalCount.lockValue,",")
    print("누적된 총 값(totalCount.lockValue) : ", total)