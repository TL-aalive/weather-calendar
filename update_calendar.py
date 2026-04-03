import os
import requests
from datetime import datetime
import pytz

def debug():
    api_key = os.environ.get('KMA_API_KEY')
    seoul_tz = pytz.timezone('Asia/Seoul')
    now = datetime.now(seoul_tz)
    
    # 1. 단기예보 주소 (4.3 단기예보조회)
    base_date = now.strftime('%Y%m%d')
    base_time = "0500" # 테스트용 고정 시간
    url = f"https://apihub.kma.go.kr/api/typ02/openApi/VilageFcstInfoService_2.0/getVilageFcst?pageNo=1&numOfRows=10&dataType=JSON&base_date={base_date}&base_time={base_time}&nx=60&ny=127&authKey={api_key}"
    
    print("--- [1] API 호출 시작 ---")
    try:
        res = requests.get(url)
        print(f"상태 코드: {res.status_code}")
        print("--- [2] 기상청 응답 내용 (이 부분을 복사해서 알려주세요) ---")
        print(res.text)
        print("--- [3] 응답 내용 끝 ---")
    except Exception as e:
        print(f"에러 발생: {e}")

    # 파일이 없으면 에러가 나므로 빈 파일 생성
    with open('weather.ics', 'w') as f:
        f.write("BEGIN:VCALENDAR\nVERSION:2.0\nEND:VCALENDAR")

if __name__ == "__main__":
    debug()
