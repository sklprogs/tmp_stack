#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import PyQt5
import PyQt5.QtWidgets


class StackedWidget(PyQt5.QtWidgets.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def set_gui(self, mode=0):
        if mode == 0:
            text = 'Label 1'
            color = 'grey'
        elif mode == 1:
            text = 'Label 2'
            color = 'orange'
        else:
            print('Wrong mode!')
            text = 'Wrong mode!'
        self.label = PyQt5.QtWidgets.QLabel(text)
        self.layout_ = PyQt5.QtWidgets.QVBoxLayout()
        self.setLayout(self.layout_)
        self.layout_.addWidget(self.label)
        self.label.setStyleSheet(f'background-color:{color};')
    
    def run(self, mode=0):
        self.set_gui(mode)
        return self



class App(PyQt5.QtWidgets.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.front = 0
        self.set_gui()
    
    def bind(self, hotkeys, action):
        for hotkey in hotkeys:
            PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey), self).activated.connect(action)
    
    def report_size(self):
        mes = f'Stack #{1}: {self.stacked1.width()}x{self.stacked1.height()}'
        print(mes)
        mes = f'Stack #{2}: {self.stacked2.width()}x{self.stacked2.height()}'
        print(mes)
    
    def resize2(self):
        # For some reason, the hidden widget becomes disproportionally large
        self.stacked2.resize(self.stacked1.width(), self.stacked1.height())
    
    def resize1(self):
        # For some reason, the hidden widget becomes disproportionally large
        self.stacked1.resize(self.stacked2.width(), self.stacked2.height())
    
    def switch_stack(self):
        self.report_size()
        if self.front:
            print('1 -> 0')
            self.front = 0
            self.stacked2.hide()
            self.stacked1.show()
            self.resize1()
        else:
            print('0 -> 1')
            self.front = 1
            self.stacked1.hide()
            self.stacked2.show()
            self.resize2()
        self.report_size()
    
    def set_gui(self):
        self.create()
        self.attach()
        self.set_bindings()
    
    def set_bindings(self):
        self.bind(('Return',), self.switch_stack)
        self.bind(('Escape',), self.close)
    
    def attach(self):
        #TODO: Study addDocWidget
        self.layout_.addWidget(self.pane1, 0, 0, 1, 1)
        self.layout_.addWidget(self.pane2, 1, 1, 1, 1)
        self.setCentralWidget(self.central)
        self.pane1.setLayout(self.stack)
        
        self.stack.addWidget(self.stacked1)
        self.stack.addWidget(self.stacked2)
    
    def create(self):
        self.central = PyQt5.QtWidgets.QWidget()
        self.pane1 = PyQt5.QtWidgets.QWidget(self.central)
        self.pane2 = PyQt5.QtWidgets.QWidget(self.central)
        self.layout_ = PyQt5.QtWidgets.QGridLayout()
        self.stack = PyQt5.QtWidgets.QStackedLayout()
        self.stacked1 = StackedWidget().run(0)
        self.stacked2 = StackedWidget().run(1)



class Panel:
    
    def __init__(self, parent, y):
        self.set_values()
        self.parent = parent
        self.y = y
        self.set_gui()
    
    def set_values(self):
        self.start = 20
        self.width = 80
        self.distance = 8
        self.y = 30
    
    def set_gui(self):
        self.set_widgets()
        self.attach_buttons()
        self.adjust_buttons()
    
    def set_buttons(self):
        self.button1 = PyQt5.QtWidgets.QPushButton('Button1', self.parent)
        self.button2 = PyQt5.QtWidgets.QPushButton('Button2', self.parent)
        self.button3 = PyQt5.QtWidgets.QPushButton('Button3', self.parent)
        self.button4 = PyQt5.QtWidgets.QPushButton('Button4', self.parent)
        self.button5 = PyQt5.QtWidgets.QPushButton('Button5', self.parent)
    
    def set_widgets(self):
        self.button_group = PyQt5.QtWidgets.QButtonGroup(self.parent)
        self.set_buttons()
    
    def attach_buttons(self):
        self.button_group.addButton(self.button1)
        self.button_group.addButton(self.button2)
        self.button_group.addButton(self.button3)
        self.button_group.addButton(self.button4)
        self.button_group.addButton(self.button5)
    
    def _get_x(self, button_no=0):
        return self.start + (self.width + self.distance) * button_no
    
    def adjust_buttons(self):
        self.button1.move(self._get_x(0), self.y)
        self.button2.move(self._get_x(1), self.y)
        self.button3.move(self._get_x(2), self.y)
        self.button4.move(self._get_x(3), self.y)
        self.button5.move(self._get_x(4), self.y)


if __name__ == '__main__':
    import sys
    exe = PyQt5.QtWidgets.QApplication(sys.argv)
    app = App()
    Panel(app.pane2, app.pane1.height() + 20)
    app.show()
    sys.exit(exe.exec_())
