from flask import Flask, render_template as ren, request, redirect, url_for
import pandas as pd
import db
app = Flask(__name__)

@app.route('/')
def index():
    products = db.get_all_products()
    return ren('index.html', products=products)

@app.route('/import_csv', methods=['POST'])
def import_csv():
    """CSV 파일을 읽어서 데이터베이스에 저장"""
    file = request.files['file']
    df = pd.read_csv(file, encoding='utf-8-sig')
    
    # 필수 칼럼명 인증
    required_columns = ['상품코드', '상품명', '단가', '수량']
    if list(df.columns) != required_columns:
        return "CSV 파일의 칼럼명이 올바르지 않습니다."
    
    # 결측치 제거
    df = df.dropna(axis=0)
    # '매출액' 컬럼을 미리 생성
    df['매출액'] = df.apply(lambda row: row['단가'] * row['수량'], axis=1)

    for i in range(len(df)):
        row = df.iloc[i]
        # 각 줄의 값을 변수에 저장
        pcode = row['상품코드']
        pname = row['상품명']
        price = row['단가']
        quantity = row['수량']
        sale = row['매출액']
        db.insert_product(pcode, pname, price, quantity, sale)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)