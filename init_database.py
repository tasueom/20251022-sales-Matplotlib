# init_database.py
from db import init_all  # db.py에서 함수만 가져옴

if __name__ == '__main__':
    init_all()  # 그냥 함수 호출만!
    print("데이터베이스 초기화 완료!")