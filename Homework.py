<html>
<head>
<title>Homework.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cf8e6d;}
.s1 { color: #bcbec4;}
.s2 { color: #7a7e85;}
.s3 { color: #bcbec4;}
.s4 { color: #6aab73;}
.s5 { color: #2aacb8;}
</style>
</head>
<body bgcolor="#1e1f22">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
Homework.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>

<span class="s2"># список учеников</span>
<span class="s1">students </span><span class="s3">= [</span><span class="s4">'Аполлон'</span><span class="s3">, </span><span class="s4">'Ярослав'</span><span class="s3">, </span><span class="s4">'Александра'</span><span class="s3">, </span><span class="s4">'Дарья'</span><span class="s3">, </span><span class="s4">'Ангелина'</span><span class="s3">]</span>
<span class="s2"># отсортируем список учеников</span>
<span class="s1">students</span><span class="s3">.</span><span class="s1">sort</span><span class="s3">()</span>
<span class="s2"># список предметов</span>
<span class="s1">classes </span><span class="s3">= [</span><span class="s4">'Математика'</span><span class="s3">, </span><span class="s4">'Русский язык'</span><span class="s3">, </span><span class="s4">'Информатика'</span><span class="s3">]</span>
<span class="s2"># пустой словарь с оценками по каждому ученику и предмету</span>
<span class="s1">students_marks </span><span class="s3">= {}</span>

<span class="s2"># сгенерируем данные по оценкам:</span>
<span class="s2"># цикл по ученикам</span>
<span class="s0">for </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:  </span><span class="s2"># 1 итерация: student = 'Александра'</span>
    <span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">] = {}  </span><span class="s2"># 1 итерация: students_marks['Александра'] = {}</span>
    <span class="s2"># цикл по предметам</span>
    <span class="s0">for </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:  </span><span class="s2"># 1 итерация: class_ = 'Математика'</span>
        <span class="s1">marks </span><span class="s3">= [</span><span class="s1">random</span><span class="s3">.</span><span class="s1">randint</span><span class="s3">(</span><span class="s5">1</span><span class="s3">, </span><span class="s5">5</span><span class="s3">) </span><span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range</span><span class="s3">(</span><span class="s5">3</span><span class="s3">)]  </span><span class="s2"># генерируем список из 3х случайных оценок</span>
        <span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">] = </span><span class="s1">marks  </span><span class="s2"># students_marks['Александра']['Математика'] = [5, 5, 5]</span>
<span class="s2"># выводим получившийся словарь с оценками:</span>
<span class="s0">for </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
    <span class="s1">print</span><span class="s3">(</span><span class="s4">f'''</span><span class="s0">{</span><span class="s1">student</span><span class="s0">}</span>
            <span class="s0">{</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">]</span><span class="s0">}</span><span class="s4">'''</span><span class="s3">)</span>

<span class="s1">print</span><span class="s3">(</span><span class="s4">''' 
        Список команд: 
        1. Добавить оценки ученика по предмету 
        2. Вывести средний балл по всем предметам по каждому ученику 
        3. Вывести все оценки по всем ученикам 
        4. Вывести информацию по всем оценкам для определенного ученика 
        5. Вывести средний балл по каждому предмету по определенному ученику 
        6. Вывести средний балл по каждому ученику по определенному предмету 
        7. Удалить данные по ученикам 
        8. Удалить данные по предметам 
        9. Удалить данные по оценкам 
        10. Редактировать данные по предметам 
        11. Добавление нового ученика 
        12. Выход из программы 
        '''</span><span class="s3">)</span>

<span class="s0">while True</span><span class="s3">:</span>
    <span class="s1">command </span><span class="s3">= </span><span class="s1">int</span><span class="s3">(</span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите команду: '</span><span class="s3">))</span>
    <span class="s0">if </span><span class="s1">command </span><span class="s3">== </span><span class="s5">1</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'1. Добавить оценку ученика по предмету'</span><span class="s3">)</span>
        <span class="s2"># считываем имя ученика</span>
        <span class="s1">student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя ученика: '</span><span class="s3">)</span>
        <span class="s2"># считываем название предмета</span>
        <span class="s1">class_ </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите предмет: '</span><span class="s3">)</span>
        <span class="s2"># считываем оценку</span>
        <span class="s1">mark </span><span class="s3">= </span><span class="s1">int</span><span class="s3">(</span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите оценку: '</span><span class="s3">))</span>
        <span class="s2"># если данные введены верно</span>
        <span class="s0">if </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students_marks</span><span class="s3">.</span><span class="s1">keys</span><span class="s3">() </span><span class="s0">and </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">].</span><span class="s1">keys</span><span class="s3">():</span>
            <span class="s2"># добавляем новую оценку для ученика по предмету</span>
            <span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">].</span><span class="s1">append</span><span class="s3">(</span><span class="s1">mark</span><span class="s3">)</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">f'Для </span><span class="s0">{</span><span class="s1">student</span><span class="s0">} </span><span class="s4">по предмету </span><span class="s0">{</span><span class="s1">class_</span><span class="s0">} </span><span class="s4">добавлена оценка </span><span class="s0">{</span><span class="s1">mark</span><span class="s0">}</span><span class="s4">'</span><span class="s3">)</span>
        <span class="s2"># неверно введены название предмета или имя ученика</span>
        <span class="s0">else</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">'ОШИБКА: неверное имя ученика или название предмета'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">2</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'2. Вывести средний балл по всем предметам по каждому ученику'</span><span class="s3">)</span>
        <span class="s2"># цикл по ученикам</span>
        <span class="s0">for </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s1">student</span><span class="s3">)</span>
            <span class="s2"># цикл по предметам</span>
            <span class="s0">for </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
                <span class="s2"># находим сумму оценок по предмету</span>
                <span class="s1">marks_sum </span><span class="s3">= </span><span class="s1">sum</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s2"># находим количество оценок по предмету</span>
                <span class="s1">marks_count </span><span class="s3">= </span><span class="s1">len</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s2"># выводим средний балл по предмету</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">f'</span><span class="s0">{</span><span class="s1">class_</span><span class="s0">} </span><span class="s4">- </span><span class="s0">{</span><span class="s1">marks_sum </span><span class="s3">// </span><span class="s1">marks_count</span><span class="s0">}</span><span class="s4">'</span><span class="s3">)</span>
            <span class="s1">print</span><span class="s3">()</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">3</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'3. Вывести все оценки по всем ученикам'</span><span class="s3">)</span>
        <span class="s2"># выводим словарь с оценками:</span>
        <span class="s2"># цикл по ученикам</span>
        <span class="s0">for </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s1">student</span><span class="s3">)</span>
            <span class="s2"># цикл по предметам</span>
            <span class="s0">for </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">f'</span><span class="s0">\t{</span><span class="s1">class_</span><span class="s0">} </span><span class="s4">- </span><span class="s0">{</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">]</span><span class="s0">}</span><span class="s4">'</span><span class="s3">)</span>
            <span class="s1">print</span><span class="s3">()</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">4</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'4. Вывести информацию по всем оценкам для определенного ученика'</span><span class="s3">)</span>
        <span class="s1">student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя ученика: '</span><span class="s3">)</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">f'''Ученик: </span><span class="s0">{</span><span class="s1">student</span><span class="s0">} </span>
<span class="s4">Оценка: </span><span class="s0">{</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">]</span><span class="s0">}</span><span class="s4">'''</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">5</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'5. Вывести средний балл по каждому предмету по определенному ученику'</span><span class="s3">)</span>
        <span class="s1">student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя ученика: '</span><span class="s3">)</span>
        <span class="s0">for </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
            <span class="s0">if </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students_marks</span><span class="s3">:</span>
                <span class="s1">marks_sum </span><span class="s3">= </span><span class="s1">sum</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s1">marks_count </span><span class="s3">= </span><span class="s1">len</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">f'</span><span class="s0">{</span><span class="s1">class_</span><span class="s0">} </span><span class="s4">- </span><span class="s0">{</span><span class="s1">marks_sum </span><span class="s3">// </span><span class="s1">marks_count</span><span class="s0">}</span><span class="s4">'</span><span class="s3">)</span>
            <span class="s0">else</span><span class="s3">:</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого ученика в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">6</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'5. Вывести средний балл по каждому ученику по определенному предмету'</span><span class="s3">)</span>
        <span class="s1">class_ </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите название предмета: '</span><span class="s3">)</span>
        <span class="s0">for </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s1">student</span><span class="s3">)</span>
            <span class="s0">if </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
                <span class="s1">marks_sum </span><span class="s3">= </span><span class="s1">sum</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s1">marks_count </span><span class="s3">= </span><span class="s1">len</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">f'</span><span class="s0">{</span><span class="s1">class_</span><span class="s0">} </span><span class="s4">- </span><span class="s0">{</span><span class="s1">marks_sum </span><span class="s3">// </span><span class="s1">marks_count</span><span class="s0">}</span><span class="s4">'</span><span class="s3">)</span>
            <span class="s0">else</span><span class="s3">:</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого предмета в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">7</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'7. Удалить данные по ученикам'</span><span class="s3">)</span>
        <span class="s1">end_student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите ученика, который хотите удалить: '</span><span class="s3">)</span>
        <span class="s0">if </span><span class="s1">end_student </span><span class="s0">in </span><span class="s1">students_marks</span><span class="s3">:</span>
            <span class="s0">del </span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">end_student</span><span class="s3">]</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">)</span>
        <span class="s0">else</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого ученика в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">8</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'8. Удалить данные по предметам'</span><span class="s3">)</span>
        <span class="s1">end_class </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите предмет, который хотите удалить: '</span><span class="s3">)</span>
        <span class="s0">if </span><span class="s1">end_class </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
            <span class="s1">classes</span><span class="s3">.</span><span class="s1">remove</span><span class="s3">(</span><span class="s1">end_class</span><span class="s3">)</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s1">classes</span><span class="s3">)</span>
        <span class="s0">else</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого предмета в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">9</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'9. Удалить данные по оценкам'</span><span class="s3">)</span>
        <span class="s1">student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя: '</span><span class="s3">)</span>
        <span class="s0">if </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
            <span class="s1">class_ </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите предмет: '</span><span class="s3">)</span>
            <span class="s0">if </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
                <span class="s1">end_mark </span><span class="s3">= </span><span class="s1">int</span><span class="s3">(</span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите оценку, которую хотите удалить: '</span><span class="s3">))</span>
                <span class="s0">if </span><span class="s1">end_mark </span><span class="s0">in </span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">]):</span>
                    <span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">]).</span><span class="s1">remove</span><span class="s3">(</span><span class="s1">end_mark</span><span class="s3">)</span>
                    <span class="s1">print</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">[</span><span class="s1">student</span><span class="s3">][</span><span class="s1">class_</span><span class="s3">])</span>
                <span class="s0">else</span><span class="s3">:</span>
                    <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этой оценки в списке нет'</span><span class="s3">)</span>
            <span class="s0">else</span><span class="s3">:</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого предмета в списке нет'</span><span class="s3">)</span>
        <span class="s0">else</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого ученика в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">10</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'10. Редактировать данные по предметам'</span><span class="s3">)</span>
        <span class="s1">new_class </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Новое название предмета: '</span><span class="s3">)</span>
        <span class="s1">students_marks</span><span class="s3">[</span><span class="s1">new_class</span><span class="s3">] = []</span>
        <span class="s1">classes</span><span class="s3">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">new_class</span><span class="s3">)</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'Новый предмет добавлен'</span><span class="s3">)</span>

        <span class="s1">student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя: '</span><span class="s3">)</span>
        <span class="s0">if </span><span class="s1">student </span><span class="s0">in </span><span class="s1">students</span><span class="s3">:</span>
            <span class="s1">class_ </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите предмет: '</span><span class="s3">)</span>
            <span class="s0">if </span><span class="s1">class_ </span><span class="s0">in </span><span class="s1">classes</span><span class="s3">:</span>
                <span class="s1">classes</span><span class="s3">.</span><span class="s1">remove</span><span class="s3">(</span><span class="s1">class_</span><span class="s3">)</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s1">classes</span><span class="s3">)</span>
            <span class="s0">else</span><span class="s3">:</span>
                <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого предмета в списке нет'</span><span class="s3">)</span>
        <span class="s0">else</span><span class="s3">:</span>
            <span class="s1">print</span><span class="s3">(</span><span class="s4">'Этого ученика в списке нет'</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">11</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'11. Добавление нового ученика'</span><span class="s3">)</span>
        <span class="s1">new_student </span><span class="s3">= </span><span class="s1">input</span><span class="s3">(</span><span class="s4">'Введите имя нового ученика: '</span><span class="s3">)</span>
        <span class="s1">students_marks</span><span class="s3">[</span><span class="s1">new_student</span><span class="s3">] = {</span>
            <span class="s4">'Математика'</span><span class="s3">: [],</span>
            <span class="s4">'Русский язык'</span><span class="s3">: [],</span>
            <span class="s4">'Информатика'</span><span class="s3">: [],</span>
            <span class="s3">}</span>
        <span class="s1">students</span><span class="s3">.</span><span class="s1">append</span><span class="s3">(</span><span class="s1">new_student</span><span class="s3">)</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'Новый ученик добавлен'</span><span class="s3">)</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s1">students_marks</span><span class="s3">)</span>

    <span class="s0">elif </span><span class="s1">command </span><span class="s3">== </span><span class="s5">12</span><span class="s3">:</span>
        <span class="s1">print</span><span class="s3">(</span><span class="s4">'12. Выход из программы'</span><span class="s3">)</span>
        <span class="s0">break</span></pre>
</body>
</html>