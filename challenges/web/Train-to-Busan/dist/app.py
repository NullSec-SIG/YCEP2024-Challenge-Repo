# 유출된 디렉토리 구조:
# .
# |- static
#   |- ???
# |- templates
#   |- index.html
# |- app.py
# |- flag.txt

# 유출된 APP.PY 소스 코드
BLACKLISTED_STRINGS = ['\'', '\"', '[', ']', 'os', 'subprocess']

@app.route('/')
def index():
    return render_template('index.html', trips=trips)

@app.route('/confirmation')
def confirmation():
    trip = request.args.get('trip')

    # 해킹 가능성을 줄이기 위한 사용자 정의 sanitzation 메서드
    blacklisted = any([w in trip.lower() for w in BLACKLISTED_STRINGS])

    return render_template_string(
        CONFIRMATION_TEMPLATE.replace("TRIP", trip),
        trips=trips,
        blacklisted=blacklisted
    )
