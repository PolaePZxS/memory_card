from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, correct, wrong1, wrong2, wrong3):
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    
que_ans = []
que_ans.append(Question('Какой национальности не существует', 'Таргонцы','Немцы','Ингушеты', 'Энцы'))
que_ans.append(Question('Гос. язык португалии','португальский', 'Английский', 'Испанский','Французский'))
que_ans.append(Question( 'Как называется еврейский Новый год', 'Ханука', 'Йом Кипур', 'Кванза','Рош ха-Шана'))
que_ans.append(Question('Кто из этих персонажей не дружит с Гарри Поттером', 'Драко Малфой','Рон Уизли','Невилл Лонгботтом','Гермиона Грейнджер'))
que_ans.append(Question('Что такое Linux?', 'Операционная система с открытым исходным кодом.', 'Еда', 'Мой акк в лиге', '???'))
que_ans.append(Question('На каком языке написан Linux', ' C и assembler', 'На русском', '刀光剑影','lkjsdclkshdflwhdgbl'))
que_ans.append(Question('Лицензия','GPLv2','BT - 7274','podfhvoid','owyegf100-7'))
que_ans.append(Question('Первый релиз','1991','1983','1987','1234567890'))
que_ans.append(Question('Пользовательский интерфейс','Unix shell', 'bt7274','t-34','Doom slayer'))
que_ans.append(Question('Капибара?','Yes','SSSSSUUUUUUUUUUUUUUUiiii','no','Ну разумеется'))

app = QApplication([])
main_win = QWidget()
main_win.cur_que = 0
main_win.setWindowTitle('Memory card')
main_win.resize(800, 400)
main_win.que_score = 0
main_win.que_amount = 0


que_lbl = QLabel('Какой национальности не существует?')
ans_btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов:')
que_data = QLabel()
r_btn1 = QRadioButton('Энцы')
r_btn2 = QRadioButton('Смурфы')
r_btn3 = QRadioButton('Чулымцы')
r_btn4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()
RadioGroup.addButton(r_btn1)
RadioGroup.addButton(r_btn2)
RadioGroup.addButton(r_btn3)
RadioGroup.addButton(r_btn4)

ans_layout1 = QHBoxLayout()
ans_layout2 = QVBoxLayout()
ans_layout3 = QVBoxLayout()
ans_layout2.addWidget(r_btn1)
ans_layout2.addWidget(r_btn2)
ans_layout3.addWidget(r_btn3)
ans_layout3.addWidget(r_btn4)
ans_layout1.addLayout(ans_layout2)
ans_layout1.addLayout(ans_layout3)
RadioGroupBox.setLayout(ans_layout1)

AnsGroupBox = QGroupBox('Результат теста')
cor_incor = QLabel('Правильно/Неправильно')
res = QLabel('Правильный ответ')
r_layout = QVBoxLayout()
r_layout.addWidget(cor_incor, alignment = (Qt.AlignLeft | Qt.AlignTop))
r_layout.addWidget(res, alignment = Qt.AlignVCenter)
AnsGroupBox.setLayout(r_layout)


line_layout_1 = QHBoxLayout()
line_layout_2 = QHBoxLayout()
line_layout_3 = QHBoxLayout()
line_layout_1.addWidget(que_lbl, alignment = (Qt.AlignVCenter| Qt.AlignHCenter))
line_layout_1.addWidget(que_data, alignment = (Qt.AlignRight| Qt.AlignTop))
line_layout_2.addWidget(RadioGroupBox)
line_layout_2.addWidget(AnsGroupBox)
line_layout_3.addStretch(1)
line_layout_3.addWidget(ans_btn, stretch = 3)
line_layout_3.addStretch(1)
AnsGroupBox.hide()

the_main_layout = QVBoxLayout()
the_main_layout.addLayout(line_layout_1)
the_main_layout.addLayout(line_layout_2, stretch = 4)
the_main_layout.addLayout(line_layout_3)
main_win.setLayout(the_main_layout)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    ans_btn.setText('Следующий вопрос')

def show_que():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    ans_btn.setText('Ответить')
    RadioGroup.setExclusive(False) 
    r_btn1.setChecked(False)
    r_btn2.setChecked(False)
    r_btn3.setChecked(False)
    r_btn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [r_btn1,r_btn2,r_btn3,r_btn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.correct)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    que_lbl.setText(q.question)
    res.setText(q.correct)
    show_que()

def show_corr(res):
    cor_incor.setText(res)
    show_result()

def ch_ans():
    if answers[0].isChecked():
        show_corr('Правильно')
        main_win.que_score += 1
    else:
        show_corr('НЕВЕРНО')
        
def next_que():
    main_win.cur_que = main_win.cur_que +1
    if main_win.cur_que == len(que_ans):
        main_win.cur_que = 0
    que_rand = randint(0, len(que_ans) - 1)
    main_win.que_amount += 1
    ask(que_ans[que_rand])    
    
def click_ok():
    if ans_btn.text() == 'Ответить':
        ch_ans()
    else:
        next_que()

ans_btn.clicked.connect(click_ok)

main_win.show()
app.exec_()

que_rating = main_win.que_score / main_win.que_amount * 100
que_data.setText(que_rating)

print(round(que_rating, 1),'%')