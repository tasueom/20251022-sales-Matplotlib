import mysql.connector

# MySQL 기본 연결 설정 (데이터베이스를 지정하지 않고 접속)
base_config = {
    "host": "localhost",   # MySQL 서버 주소 (로컬)
    "user": "root",        # MySQL 계정
    "password": "1234"     # MySQL 비밀번호
}

# 사용할 데이터베이스 이름
DB_NAME = "salesdb"

# 커넥션 반환하는 함수
def get_conn():
    return mysql.connector.connect(database=DB_NAME, **base_config)

def init_db():
    """데이터베이스 생성"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(f"create database if not exists {DB_NAME} default character set utf8mb4")
    conn.commit()
    conn.close()

def create_table():
    """테이블 생성"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            pid VARCHAR(50),
            pname VARCHAR(100),
            price INT,
            quantity INT,
            sale INT
        )
    """)
    conn.commit()
    conn.close()

def init_all():
    """DB와 테이블 모두 초기화 (편의 함수)"""
    init_db()
    create_table()