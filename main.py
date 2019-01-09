import os


class Interpreter:

    singalch = ['+', '-', '*', '/', '(', ')', '=', ',', '.', '#', ';']
    symbol = [
        'begin', 'call', 'const', 'do', 'end', 'if', 'odd', 'procedure',
        'read', 'then', 'var', 'while', 'write'
    ]

    def __init__(self, fname):
        self.str = []  # 初始化str
        self.ignore = 0  # 初始化忽略sym标志
        self.num = 0  # 初始化数字
        self.tab = 0  # 初始化缩进标志
        self.tabdepth =0  # 缩进深度
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        os.chdir(curr_dir)
        self.pl0file = open(fname, 'r')
        self.pyfile = open('pl0.py', 'w')
        self.getch()

    def getch(self):
        # 获取一个字符并后移游标
        self.ch = self.pl0file.read(1)
        print(self.ch)

    def watch():
        # 获取游标后面的字符
        print()

    def getsym(self):
        while (self.ch == ' ' or self.ch == 10 or self.ch == 13
               or self.ch == 9):
            self.getch()
        if (self.ch >= 'a' and self.ch <= 'z'):
            while (self.ch >= 'a' and self.ch <= 'z'):
                self.str.append(self.ch)
                self.getch()
        # 获取一个关键字
            self.issym = self.listtostr(self.str)
            if (self.issym in self.symbol):
                self.sym = self.issym
            else:
                self.sym = 'ident'
        elif (self.ch >= '0' and self.ch <= '9'):
            self.sym = 'number'
            while (self.ch >= '0' and self.ch <= '9'):
                self.num = 10 * self.num + int(self.ch) - int('0')
                self.getch()
        elif (self.ch == ':'):
            self.getch()
            if (self.ch == '='):
                self.sym = 'becomes'
                self.getch()
            else:
                self.sym = 'nul'
        elif (self.ch == ';'):
            self.getch()
            if (self.ch == '\n'):
                self.sym = 'nextline'
                self.getch()
        elif (self.ch == '.'):
            self.sym = 'pl0end'
        elif (self.ch == ','):
            self.sym = 'comma'
            self.getch()
        
        print(self.sym)

    def output(self):
        if (self.sym == 'var'):
            self.ignore = 1
        elif (self.sym == 'ident'):
            if (self.ignore == 0):
                self.pyfile.write(self.issym)
        elif (self.sym == 'number'):
            self.pyfile.write(str(self.num))
        elif (self.sym == 'becomes'):
            self.pyfile.write('=')

        if (self.sym == 'nextline' or self.sym == 'pl0end'):
            if (self.ignore == 0):
                self.pyfile.write('\n')
            self.ignore = 0
        else:
            if (self.ignore == 0):
                self.pyfile.write(' ')

    def translate(self):
        self.getsym()
        self.output()
        while (self.sym != 'pl0end'):
            self.str.clear()
            self.num = 0
            self.getsym()
            self.output()

    def listtostr(self, list):
        return ''.join(str(e) for e in list)


a = Interpreter("pl0.txt")
a.translate()
