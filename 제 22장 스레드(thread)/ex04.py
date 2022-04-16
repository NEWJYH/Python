# 스레드의 문제점 : 모든 스레드는 모든 자원(파일, 장치, 객체 등)을 전부
# 공유한다.예를 들어서 스레드는 전역변수를 전부 공유를 하는데 서로 다른
# 스레드가 전역변수에 접근을 하면 원치 않은 결과를 초래할 수 있다.

# Lock 클래스를 사용하지 않은 예제
import threading
totalCount = 0   # 전역 변수 선언과 초기화

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()
    def run(self):
        global totalCount         # global 키워드로 메소드 내에 전역변수 선언
        for _ in range(2500000):
            totalCount += 1
        print(threading.currentThread().getName(), " 스레드 2,500,000번 누적 종료")

# 메인코드 작성
if __name__ == "__main__":
    for _ in range(4):
        counterThread = CounterThread()
        counterThread.start()
    print("모든 스레드들이 종료될 때까지 기다립니다.")
    mainThread = threading.currentThread()
    # threading 모듈 enumerate()메소드는 현재 active 는 모든 스레드를 리스트로
    # 반환해준다.
    # print("현재 Active 한 스레드 이름 : ", threading.enumerate())
    for thread in threading.enumerate():
        # mainThread 를 제외한 모든 스레드들이 작업을 완료하고 끝날 때까지 기다리는 코드
        if thread is not mainThread:
            thread.join()
    totalCount = format(totalCount,",")
    # totalCount 의 값이 10,000,000이 나올 것으로 우리는 예상하지만 아래와 같이
    # 출력코드를 작성해서 실행해보면 엉뚱한 값이 나오는 것을 볼 수가 있다.
    # 그 이유는? 바로 4개의 스레드가 동시다발적으로 totalCount 에 접근하기 때문에
    # 문제가 발생한 것이다.
    # 이러한 문제점을 해결하기 위한 방안이 Lock 클래스의 aquire(), release() 두 개의
    # 메소드를 이용하여 동기화 처리를 해서 해결하면 되는 것이다.
    print("totalCount = ", totalCount)

