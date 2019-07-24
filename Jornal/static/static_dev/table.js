
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
    };
};

function tableCreate(object){
    jornal = object
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
       date.push(jornal[j+'']['date'])
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
        for (var k of dateList){
            var htmlTr = [];
            var vall = {'date': k, 'score': null}
            htmlTr.push(vall);
            studentGrades[stap].push(htmlTr);
            htmlTr = [];
        };
    stap = stap + 1
    };
    for(i of studentGrades){
        vall = i.slice(3)
        for (j of vall){
            for(var s = 1; s < jornal['iterator']; s++){
               if (i[0]===jornal[String(s)]['student']['first_name']
                && i[1]===jornal[String(s)]['student']['last_name']
                && i[2]===jornal[String(s)]['student']['patronymic']
                && j[0]['date']===jornal[String(s)]['date']){
                j[0]['score'] = jornal[String(s)]['score']
               };
            };
        };
    };
    for (i of studentGrades){
        var tr = document.createElement('tr');
        table.appendChild(tr);
        var td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = i[1]+' '+i[0][0]+'.'+i[2][0]+'.'
        vall = i.slice(3)
            for (j of vall){
                var td = document.createElement('td');
                tr.appendChild(td);
                td.innerHTML = j[0]['score']
            };
        };
};

getJSON()
