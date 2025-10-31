<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>유리식 디지털 교과서</title>
    <style>
        body {
            background-color: rgb(203,147,160);
            font-family: 'Noto Sans KR', sans-serif;
            margin: 0;
            padding: 30px;
        }

        h1 {
            text-align: center;
            color: #ffffff;
            background-color: rgba(153,70,95,0.9);
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        section {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            margin: 20px auto;
            max-width: 800px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        h2 {
            color: rgb(153,70,95);
        }

        p {
            font-size: 18px;
            line-height: 1.6;
        }

        .example {
            background-color: #f9e0e6;
            padding: 15px;
            border-left: 6px solid rgb(153,70,95);
            margin: 15px 0;
            border-radius: 6px;
        }

        .comparison {
            display: flex;
            justify-content: space-between;
            gap: 20px;
            flex-wrap: wrap;
        }

        .comparison div {
            flex: 1;
            min-width: 250px;
            background-color: #fff4f6;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .comparison h3 {
            color: rgb(153,70,95);
        }

    </style>
</head>
<body>
    <h1>유리식 디지털 교과서</h1>

    <section>
        <h2>1. 유리식의 정의</h2>
        <p>유리식은 <strong>두 다항식의 몫으로 나타낼 수 있는 식</strong>을 말합니다.  
        즉, 분모와 분자가 모두 다항식이며, <strong>분모가 0이 되어서는 안 됩니다.</strong></p>

        <div class="example">
            <p><strong>예시 1:</strong> \( \dfrac{x+3}{x-2} \)</p>
            <p><strong>예시 2:</strong> \( \dfrac{2x^2 - 5}{x^2 + 4} \)</p>
        </div>
    </section>

    <section>
        <h2>2. 유리식과 다항식 구분하기</h2>
        <p>다항식은 <strong>분모에 문자가 없는 식</strong>이고,  
        유리식은 <strong>분모에 문자가 포함된 식</strong>입니다.</p>

        <div class="comparison">
            <div>
                <h3>다항식</h3>
                <p>예: \( 3x^2 + 2x - 1 \)</p>
                <p>→ 분모에 문자가 없음</p>
            </div>
            <div>
                <h3>유리식</h3>
                <p>예: \( \dfrac{2x + 1}{x - 2} \)</p>
                <p>→ 분모에 문자가 있음</p>
            </div>
        </div>
    </section>
</body>
</html>
