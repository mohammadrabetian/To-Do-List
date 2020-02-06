#برای کار کردن با این برنامه 
#PyQt5 And PyQt5-tools باید نصب شود
import sys
from PyQt5 import QtWidgets , QtCore , QtGui

class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Rick ToDo list'
        self.left = 200
        self.top = 200
        self.width = 400
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        IconWin = QtGui.QIcon('Icons\win.png')
        self.setWindowIcon(IconWin)
        self.setFixedSize(400,400)

    #تابع اضافه کردن کار جدید
        def AddTask():
            if TextLine.text() != "":
                stxt = TextLine.text()
                NotCompleteList.addItem(stxt)
                TextLine.setText("")
    #تابعی برای انتقال کار های انجام شده به لیست مربوط
        def Complete():
            try:
                text = NotCompleteList.currentItem().text()
                CompleteList.addItem(text)
                RemoveTasks()
            except:
                ErrorMsg("Select Task") 
    #تابع سیو کردن فایل
        def SaveFile():
            try:
                fileFullName = str(QtWidgets.QFileDialog.getSaveFileName())
                start = fileFullName.find("'") + 1
                end = fileFullName.find(".rick") + 5
                if end == 4:
                    ErrorMsg("Just .rick Format")
                else:
                    FileName = fileFullName[start:end]
                    MyFile = open(FileName,'w')
                    for i in range(NotCompleteList.count()):
                        item = NotCompleteList.item(i).text()
                        MyFile = open(FileName,'a')
                        MyFile.write(item + ' ')
                    for i in range(CompleteList.count()):
                        item = CompleteList.item(i).text()
                        MyFile = open(FileName,'a')
                        MyFile.write(item + '~ ')
            except:
                ErrorMsg("Just .rick Format")                
    #تابع باز کردن فایل
        def OpenFile():
            try:
                fileFullName = str(QtWidgets.QFileDialog.getOpenFileName())
                start = fileFullName.find("'") + 1
                end = fileFullName.find(".rick") + 5
                if end == 4:
                    ErrorMsg("Just .rick Format")
                else:
                    RemoveAllTask()
                    FileName = fileFullName[start:end]
                    MyFile = open(FileName , 'r')       
                    MyFileItems = MyFile.read()
                    SplitedItems = MyFileItems.split()
                    for item in range(len(SplitedItems)):
                        if SplitedItems[item].find('~') == -1:
                            NotCompleteList.addItem(SplitedItems[item])  
                        else:
                            newText = SplitedItems[item].replace('~','')
                            CompleteList.addItem(newText) 
            except:
                ErrorMsg("Just .rick Format")                

    #تابعی برای حذف آیتم از هر دو لیست       
        def RemoveTasks():
            try:
                for item in NotCompleteList.selectedItems():
                    NotCompleteList.takeItem(NotCompleteList.row(item))
            except:
                ErrorMsg("Select item") 
            else:
                for item in CompleteList.selectedItems():
                    CompleteList.takeItem(CompleteList.row(item))
    #تابعی برای حذف همه آیتم هااز هر دو لیست       
        def RemoveAllTask():
            NotCompleteList.clear()
            CompleteList.clear()
    #تابعی برای مرتب سازی آیتم ها
        def SortTasks():
            NotCompleteList.sortItems()
            CompleteList.sortItems()
    #تابع دی سلکت 
        def DeSelectNotComlated():
            CompleteList.clearSelection()
        def DeSelectComlated():
            NotCompleteList.clearSelection()
    #تابع پیام خطا       
        def ErrorMsg(text):
            msg = QtWidgets.QMessageBox(self)
            msg.setText(text)
            msg.show()
    #فونت ها   
        font1 = QtGui.QFont()
        font1.setFamily('Comic Sans MS')
        font1.setWeight(75) 

        font2 = QtGui.QFont()
        font2.setBold(True)
        font2.setStrikeOut(True)
        font2.setFamily('Comic Sans MS')
        font2.setWeight(75)
    #بک گراند
        BGlbl = QtWidgets.QLabel(self)
        BGlbl.setGeometry(0,0,400,400)
        pixmapBG = QtGui.QPixmap('Icons\Rickbg.jpg')
        BGlbl.setPixmap(pixmapBG)
    #دکمه ها
        OpenBtn = QtWidgets.QPushButton(self)
        OpenBtn.setGeometry(5,330,70,50)
        OpenBtn.clicked.connect(OpenFile)
        IconOpen = QtGui.QIcon('Icons\open.png')
        OpenBtn.setIconSize(QtCore.QSize(30,30))
        OpenBtn.setIcon(IconOpen)
        

        SaveBtn = QtWidgets.QPushButton(self)
        SaveBtn.setGeometry(85,330,70,50)
        SaveBtn.clicked.connect(SaveFile)
        IconSave = QtGui.QIcon('Icons\save.png')
        SaveBtn.setIconSize(QtCore.QSize(30,30))
        SaveBtn.setIcon(IconSave)

        AddBtn = QtWidgets.QPushButton(self)
        AddBtn.setGeometry(160,20,40,30)
        AddBtn.clicked.connect(AddTask)
        IconAdd = QtGui.QIcon('Icons\Add.png')
        AddBtn.setIconSize(QtCore.QSize(20,20))
        AddBtn.setIcon(IconAdd)

        CompleteBtn = QtWidgets.QPushButton(self)
        CompleteBtn.setGeometry(180,80,40,230)
        CompleteBtn.clicked.connect(Complete)
        CompleteBtn.setFont(QtGui.QFont("tahoma" , 20))
        IconComplete = QtGui.QIcon('Icons\done.png')
        CompleteBtn.setIconSize(QtCore.QSize(30,30))
        CompleteBtn.setIcon(IconComplete)

        RemoveBtn = QtWidgets.QPushButton(self)
        RemoveBtn.setGeometry(165,330,70,50)
        RemoveBtn.clicked.connect(RemoveTasks)
        IconRemove = QtGui.QIcon('Icons\Remove.png')
        RemoveBtn.setIconSize(QtCore.QSize(55,55))
        RemoveBtn.setIcon(IconRemove)

        RemoveAllBtn = QtWidgets.QPushButton(self)
        RemoveAllBtn.setGeometry(245,330,70,50)
        RemoveAllBtn.clicked.connect(RemoveAllTask)
        IconRemoveAll = QtGui.QIcon('Icons\RemoveAll.png')
        RemoveAllBtn.setIconSize(QtCore.QSize(55,55))
        RemoveAllBtn.setIcon(IconRemoveAll)

        SortBtn = QtWidgets.QPushButton(self)
        SortBtn.setGeometry(325,330,70,50)
        SortBtn.clicked.connect(SortTasks)
        IconSort = QtGui.QIcon('Icons\sort.png')
        SortBtn.setIconSize(QtCore.QSize(30,30))
        SortBtn.setIcon(IconSort)
    #لیست ها
        NotCompleteList = QtWidgets.QListWidget(self)
        NotCompleteList.setGeometry(220,80,170,230)
        NotCompleteList.setStyleSheet("border:4px solid yellow;")
        NotCompleteList.setFont(font1)
        NotCompleteList.itemClicked.connect(DeSelectNotComlated)

        CompleteList = QtWidgets.QListWidget(self)
        CompleteList.setGeometry(10,80,170,230)
        CompleteList.setStyleSheet("border:4px solid green;")
        CompleteList.setFont(font2)
        CompleteList.itemClicked.connect(DeSelectComlated)
    #لیبل ها
        NotCompleteLbl = QtWidgets.QLabel("NOT Done",self)
        NotCompleteLbl.setGeometry(320,60,60,20)
        NotCompleteLbl.setFont(font1)

        CompleteLbl = QtWidgets.QLabel("Done",self)
        CompleteLbl.setGeometry(130,60,60,20)
        CompleteLbl.setFont(font1)

        ImageLbl = QtWidgets.QLabel("Done",self)
        ImageLbl.setGeometry(5,5,150,60)
        pixmap = QtGui.QPixmap('Icons\Rick.png')
        ImageLbl.setPixmap(pixmap)
    #تکست لاین برای نوشتن کار جدید
        TextLine = QtWidgets.QLineEdit(self)
        TextLine.setGeometry(200,20,190,30)
        TextLine.returnPressed.connect(AddTask)

        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())