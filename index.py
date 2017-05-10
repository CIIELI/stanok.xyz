#!c:\Python\Python36-32\python.exe

import sys
import cgi
import html

form = cgi.FieldStorage()
data = form.getfirst("data", "-")

if data == '-':

	print ('Content-Type: text/html\n')
	print ('<script src="js/jquery.min.js" type="text/javascript"></script>')
	print ('''
<!DOCTYPE html>
<html lang="ru">
	<head>
        <title>Онлайн контроль станков</title>
		<style>
		h {
			background: #D9FFAD; /* Цвет фона под заголовком */
			color: green; /* Цвет текста */
			padding: 2px; /* Поля вокруг текста */
			display: inline-block;
		}
		h3 {
			background: #D9FFAD; /* Цвет фона под заголовком */
			color: green; /* Цвет текста */
			padding: 2px; /* Поля вокруг текста */
			display: inline-block;
		}
		</style>
	</head>
<body background='images/fon.gif' bgcolor='#EAFFBC'>
<table border="1" bordercolor="cc215a" width="800" align="center"> 
<tr> 
<td bgcolor="e6e6fa"> 
<!--Шапка сайта.-->

<table border="1" bordercolor="cc215a" width="790" height="200"
 cellpadding="10"> 
<tr> 
<th background='images/fon4.jpg' width='790' height='200'> 
<h1><font color='#000000' face='Arial'>
STANOK.XYZ</font>
<h3 align="center"> 
<font color="#000000" size=+5>Мониторинг работы станков
</font>
</h3> 
</h1> 
</th> 
</tr> 
</table> 
<!--Текст статьи--> 
<table border="1" bordercolor="cc215a" width="790" cellpadding="10"> 
<tr> 
<td rowspan="4" width="600" bgcolor="e6e6fa"> 
<h3>Galaxy-Skynet</h3> 
<p style="text-indent:20px"><!--<span style = "font-size: 30px;">
<font face="Monotype Corsiva"> <font color="cc215a">
<strong></strong></font></font></span>--> Galaxy-Skynet используется для
мониторинга работы оборудования и повышения эффективности производительности
процессов, связанных с работой станков с ЧПУ. Особенность решения
заключается в способности объединить в единое информационное пространство
как новейшие импортные, так и отечественные станки предыдущих поколений.</p>
 
<p style="text-indent:20px"> Инновационная концепция нашего решения
заключается в ассистировании
всем участникам производственного процесса. Руководитель предприятия имеет
возможность принимать управленческие решения на основе объективной
информации о загрузке и причинах простоя оборуования. Цеховые службы
становятся более оперативными, реагируя на запросы о поломках и
необходимости ремота оборудования, отсутствии режущего инструмента
или заготовок. Оператор станка получает сменно-суточное задание
и нормативы времени на его выполнение прямо на экране блока мониторинга,
а комплекс мотивирует его на выполнение операции точно в строк.
Таким образом, наше решение не только контролирует состояние
оборудования и деятельность персонала, но и активно помогает сделать
ваше производство более прозрачным, эффективным и современным.</p>
<p style="text-indent:20px"> С нами вы делаете первый шаг к бережливому производству и технологиям
Industry 4.0.
</p>
</td> 
<!--Сайдбар--> 
<td bgcolor="e6e6fa" align="left"> 
<h3>Меню</h3> 
<p><img src='images/123.jpg'>
Главная</p> 
<p><img src='images/123.jpg'>
Список станков</p> 
<p><img src='images/123.jpg'>
Документация</p> 
<p><img src='images/123.jpg'>
Другая страница</p> 
</td> 
</tr> 
<tr> 
<td bgcolor="e6e6fa" align="center"> 
<h3>Тревожная кнопка</h3> 
<p id="data-block">Try to get data, please wait...</p>
</td> 
</td> 
</tr> 
</tr> 
</table> 
</table> 
</body> 
</html>''')
	
	print('''
	
	<script language="javascript" type="text/javascript">
	
	String.prototype.contains = function(it) { return this.indexOf(it) != -1; };
	
	var timerId = setInterval(function() {
	
		var green = '<img src="/images/onLamp.png" alt="Green button" height="150" width="150">';
		var red = '<img src="/images/offLamp.png" alt="Red button" height="150" width="150">';
	
		$.ajax({
		  url: '/?data=get',
		  success: function(data) {
			var tag = green;
			if ( !data.contains('1') ) {
				tag = red;
			}
			$('#data-block').html(tag);
		  }
		});
	}, 1000);
	
	</script>
	
	''')

	print ("</body></html>")
	
else:
	print ("Content-Type: text/text\n")
	with open('text_files\data.txt') as f:
		data = f.read()
		print (data)
	