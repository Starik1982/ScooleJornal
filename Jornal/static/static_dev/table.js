/*function tableCreate() {
    var body = document.getElementsByTagName('body')[0];
    var table = document.createElement('table');
    var tr = document.createElement('tr');
    for (var i = 0; i < 3; i++) {
    var th = document.createElement('th');
    th.innerHTML = "<h1>Привет!"+i+"</h1>";
    tr.appendChild(th);
		}
	table.appendChild(tr)

    for (var j = 0; j < 8; j++) {
	var tr = document.createElement('tr');
		for (var i = 0; i < 3; i++) {
    	var td = document.createElement('td');
    	td.innerHTML = "<h1>Строка №"+(j+1)+"Столбец №"+(i+1)+" </h1>";
    	tr.appendChild(td);
    	}
    	table.appendChild(tr)
	}
    body.appendChild(table)
    }*/

function getElement(){
    var class_title = document.getElementById('class_title')
    var subject = document.getElementById('subject')
    class_title = class_title.textContent;
    subject = subject.textContent;
    url = "http://127.0.0.1:8000/area/load_subject_jornal/"+class_title+"&"+subject+"/"
    console.log(url)
    return url
};

function getJSON(){
    var requestURL = getElement()
    var request = new XMLHttpRequest();
    request.open('GET', requestURL);
    request.responseType = 'json';
    request.send();
    request.onload = function() {
    var jornal = request.response;
    tableCreate(jornal)

    }
};

function tableCreate(object){
    jornal = object
    console.log(jornal)
    //таблица
    var div = document.getElementById('table');
    var table = document.createElement('table');
    div.appendChild(table);
    //заголовок таблицы
    var tr = document.createElement('tr');
    table.appendChild(tr);
    var th = document.createElement('th');
    tr.appendChild(th);
    th.innerHTML = jornal['period']['title'];
    //ряд с датами
    var date = [];
    for(var j = 1; j < jornal['iterator']; j++) {
       date.splice(j-1, 0, jornal[j+'']['date'])
    };
    dateList = new Set(date)
    var tr = document.createElement('tr');
    table.appendChild(tr);
     var th = document.createElement('th');
        tr.appendChild(th);
        th.innerHTML = '/';
    for(i of dateList){
        var th = document.createElement('th');
        tr.appendChild(th);
        th.innerHTML = i;
        };
     //робоча зона таблиці
    var htmlTr = []
    var studentGrades = []
    stap = 0
    for(var i of jornal['student_list']) {
        studentGrades.push(i);
        for(var j = 1; j < jornal['iterator']; j++) {
            if (i[0]===jornal[j+'']['student']['first_name']
            && i[1]===jornal[j+'']['student']['last_name']
            && i[2]===jornal[j+'']['student']['patronymic']){
            htmlTr.push(jornal[j+'']);
            };
        studentGrades[stap].push(htmlTr);
        };

    stap = stap + 1
    };
    console.log(studentGrades)


};





getJSON()
