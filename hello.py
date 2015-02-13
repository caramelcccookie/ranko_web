from flask import Flask
from ranko import sentence

app = Flask(__name__)

@app.route('/ranko_bot.html') 
def index():
	path='/ranko_bot.html'
	sen=sentence()
	return """
<!DOCTYPE html>
<html>
	<head>
		<title>란코어 생성기 웹 서비스</title>
		<meta charset="utf-8"/>
	</head>
	<body>
		<h1>란코어 생성기</h1>
			<p>본 서비스는 신데마스 캐릭터인 칸자키 란코의 흉내를 내어 '란코어'로 말합니다.</p>
		<h2>메뉴</h2>
			<p>%s</p>
			<button onclick="myFunction()">Reload page</button>

			<script>
			function myFunction() {
    		location.reload();
			}
			</script>
		<button onclick="myFunction()">Tweet it</button>
		<script>
			function myFunction() {
    		location.assign("https://twitter.com/intent/tweet?text=%s");
			}
		</script>
	</body>	
</html>
"""%(sen,sen)
@app.route('/')
def hello_world():
	return """
<!DOCTYPE html>
<html>
	<head>
		<title>란코어 생성기 웹 서비스</title>
		<meta charset="utf-8"/>

	</head>
	<body>
		<h1>란코어 생성기</h1>
			<p>본 서비스는 신데마스 캐릭터인 칸자키 란코의 흉내를 내어 '란코어'로 말합니다.</p>
		<h2>메뉴</h2>
			<p>현 주소의 뒤에 ranko_bot.html 를 붙여주세요<p>
	</body>	
</html>
"""

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0')

