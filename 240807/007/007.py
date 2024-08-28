class SecretMeeting:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

    def display_info(self):
        print(f"secret code : {self.secret_code}")
        print(f"meeting point : {self.meeting_point}")
        print(f"time : {self.time}")

# 입력을 받아서 처리
secret_code, meeting_point, time = map(str, input().split())

# 객체 생성 및 정보 출력
meeting = SecretMeeting(secret_code, meeting_point, time)
meeting.display_info()