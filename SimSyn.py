# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SimSyn_v02.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import psycopg2
from psycopg2.extensions import AsIs
import time
import pysd
import pandas as pd
from os import path
QtCore.QCoreApplication.addLibraryPath(path.join(path.dirname(QtCore.__file__), "plugins"))
QtGui.QImageReader.supportedImageFormats()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        #Create main window, insert central widget into main window (child of main window)
        #Add grid layout as child of central widget
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(600, 370)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Local_v01-001.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.v = QtGui.QGridLayout(self.centralwidget)
        self.v.setObjectName(_fromUtf8("v"))

        #Put spacer between croup boxes
        spacerItem1 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.v.addItem(spacerItem1, 0, 0, 1, 1)

        #Create 1st Group Box: Set Connections
        self.GroupBox_Connect = QtGui.QGroupBox(self.centralwidget)              #Assign 1st group box to central widget
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GroupBox_Connect.setFont(font)
        self.GroupBox_Connect.setObjectName(_fromUtf8("GroupBox_Connect"))

        self.gridLayout = QtGui.QGridLayout(self.GroupBox_Connect)               #Assign gridLayout to 1st group box
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.Db_Name = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Db_Name.setFont(font)
        self.Db_Name.setObjectName(_fromUtf8("Db_Name"))
        self.gridLayout.addWidget(self.Db_Name, 0, 0, 1, 1)

        self.Host_Name = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Host_Name.setFont(font)
        self.Host_Name.setObjectName(_fromUtf8("Host_Name"))
        self.gridLayout.addWidget(self.Host_Name, 0, 1, 1, 1)

        self.User_Name = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.User_Name.setFont(font)
        self.User_Name.setObjectName(_fromUtf8("User_Name"))
        self.gridLayout.addWidget(self.User_Name, 1, 0, 1, 1)

        self.Password = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Password.setFont(font)
        self.Password.setObjectName(_fromUtf8("Password"))
        self.gridLayout.addWidget(self.Password, 1, 1, 1, 1)

        self.Port = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Port.setFont(font)
        self.Port.setObjectName(_fromUtf8("Port"))
        self.gridLayout.addWidget(self.Port, 2, 0, 1, 1)

        self.Table_Name = QtGui.QLineEdit(self.GroupBox_Connect)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Table_Name.setFont(font)
        self.Table_Name.setObjectName(_fromUtf8("Table_Name"))
        self.gridLayout.addWidget(self.Table_Name, 2, 1, 1, 1)

        self.Btn_Connect = QtGui.QPushButton(self.GroupBox_Connect)
        self.Btn_Connect.setEnabled(True)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Connect.setFont(font)
        self.Btn_Connect.setFixedWidth(150)
        self.Btn_Connect.setFixedHeight(20)
        self.Btn_Connect.setObjectName(_fromUtf8("Btn_Connect"))
        self.gridLayout.addWidget(self.Btn_Connect, 3, 0, 1, 1)

        self.v.addWidget(self.GroupBox_Connect, 1, 0, 1, 1)                      #Add 1st group box to master grid layout

        self.Host_Name.raise_()                                                  #Raise widgets to the top of the parent widget's stack. After this call widget will be visually in front of any overlapping sibling widgets
        self.Password.raise_()
        self.User_Name.raise_()
        self.Table_Name.raise_()
        self.Port.raise_()
        self.Db_Name.raise_()
        self.Btn_Connect.raise_()
        self.GroupBox_Connect.raise_()



        #But spacer between croup boxes
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.v.addItem(spacerItem2, 2, 0, 1, 1)



        #Create 2nd Group Box: Build Vensim Model
        self.GroupBox_build = QtGui.QGroupBox(self.centralwidget)                #Assign 1st group box to central widget
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GroupBox_build.setFont(font)
        self.GroupBox_build.setObjectName(_fromUtf8("GroupBox_Connect"))

        self.gridLayout2 = QtGui.QGridLayout(self.GroupBox_build)                #Assign gridLayout to 1st group box
        self.gridLayout2.setObjectName(_fromUtf8("gridLayout2"))

        self.Model_Dir = QtGui.QLineEdit(self.GroupBox_build)
        self.gridLayout2.addWidget(self.Model_Dir, 0, 0, 1, 2)

        self.sub_gridLayout = QtGui.QGridLayout(self.GroupBox_build)             #Subgrid layout to backage 'browse-button' and 'Build-VENSIM-Model-Button' gridLayout
        self.sub_gridLayout.setObjectName(_fromUtf8("sub_gridLayout"))
        self.gridLayout2.addLayout(self.sub_gridLayout, 0,2,1,1)

        self.Btn_Browse_Ven = QtGui.QPushButton(self.GroupBox_build)
        self.Btn_Browse_Ven.setObjectName(_fromUtf8("Btn_Browse_Ven"))
        self.Btn_Browse_Ven.setFixedWidth(25)
        self.Btn_Browse_Ven.setFixedHeight(20)
        self.sub_gridLayout.addWidget(self.Btn_Browse_Ven, 0, 0, 1, 1)

        self.Btn_Build = QtGui.QPushButton(self.GroupBox_build)
        self.Btn_Build.setEnabled(True)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Build.setFont(font)
        self.Btn_Build.setFixedWidth(90)
        self.Btn_Build.setFixedHeight(20)
        self.Btn_Build.setObjectName(_fromUtf8("Btn_Build"))
        self.sub_gridLayout.addWidget(self.Btn_Build, 0, 1, 1, 1)

        self.v.addWidget(self.GroupBox_build, 3, 0, 1, 1)                        #Add 2nd group box to master grid layout



        #But spacer between croup boxes
        spacerItem3 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.v.addItem(spacerItem3, 4, 0, 1, 1)



        #Create 3rd Group Box: Connection Settings
        self.GroupBox_Settings = QtGui.QGroupBox(self.centralwidget)             #Assign 3rd group box to central widget
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.GroupBox_Settings.setFont(font)
        self.GroupBox_Settings.setObjectName(_fromUtf8("GroupBox_Settings"))

        self.gridLayout_3 = QtGui.QGridLayout(self.GroupBox_Settings)            #Assign gridLayout2 to 2nd group box
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))

        self.Link_Tab_Frame = QtGui.QFrame(self.GroupBox_Settings)               #Create "Link_Tab_Frame" (Child) as subcontainer of "GroupBox_Settings" (Parent)
        self.Link_Tab_Frame.setObjectName(_fromUtf8("Link_Tab_Frame"))
        self.gridLayout_3.addWidget(self.Link_Tab_Frame, 2, 0, 3, 1)             #Add subcontainer to grid Layout of the "GroupBox_Settings" parent object
        self.gridLayout_frame = QtGui.QGridLayout(self.Link_Tab_Frame)           #Create new grid Layout within "Link_Tab_Frame" subcontainer
        self.gridLayout_frame.setObjectName(_fromUtf8("gridLayout_frame"))
        self.gridLayout_frame.setContentsMargins(0, 0, 0, 0)

        self.Link_Tab = QtGui.QTableWidget(self.Link_Tab_Frame)
        self.Link_Tab.setObjectName(_fromUtf8("Link_Tab"))
        self.Link_Tab.setColumnCount(4)
        self.Link_Tab.horizontalHeader().setFixedHeight(20)
        self.Link_Tab.setHorizontalHeaderLabels(["Model Variable", "Database Variable", "Use as", "Time (optional)"])
        stylesheet = "QHeaderView::section{Background-color:rgb(90,90,90); border-radius:15px;border-right:1px solid #FFFFFF;}"
        self.Link_Tab.horizontalHeader().setStyleSheet(stylesheet)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(8.5)
        for c in range(self.Link_Tab.columnCount()):
            self.Link_Tab.setColumnWidth(c, 130)
            self.Link_Tab.horizontalHeaderItem(c).setFont(font)
            self.Link_Tab.horizontalHeaderItem(c).setForeground(QtGui.QBrush(QtGui.QColor(255,255,255)))
        self.gridLayout_frame.addWidget(self.Link_Tab, 0, 0, 1, 1)

        self.Button_Frame = QtGui.QFrame(self.GroupBox_Settings)
        self.Button_Frame.setObjectName(_fromUtf8("Button_Frame"))
        self.gridLayout_3.addWidget(self.Button_Frame, 2, 1, 1, 2)
        self.gridLayout_button = QtGui.QGridLayout(self.Button_Frame)
        self.gridLayout_button.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_button.setContentsMargins(0, 0, 0, 0)

        self.Btn_Plus = QtGui.QPushButton(self.GroupBox_Settings)
        self.Btn_Plus.setEnabled(True)
        self.Btn_Plus.setObjectName(_fromUtf8("Btn_Plus"))
        self.Btn_Plus.setFixedHeight(20)
        self.Btn_Plus.setFixedWidth(20)
        self.gridLayout_button.addWidget(self.Btn_Plus, 0, 0, 1, 1)

        self.Btn_Minus = QtGui.QPushButton(self.GroupBox_Settings)
        self.Btn_Minus.setEnabled(True)
        self.Btn_Minus.setObjectName(_fromUtf8("Btn_Minus"))
        self.Btn_Minus.setFixedHeight(20)
        self.Btn_Minus.setFixedWidth(20)
        self.gridLayout_button.addWidget(self.Btn_Minus, 1, 0, 1, 1)

        self.Btn_Reset = QtGui.QPushButton(self.GroupBox_Settings)
        self.Btn_Reset.setEnabled(True)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Reset.setFont(font)
        self.Btn_Reset.setFixedHeight(20)
        self.Btn_Reset.setFixedWidth(70)
        self.Btn_Reset.setObjectName(_fromUtf8("Btn_Reset"))
        self.gridLayout_button.addWidget(self.Btn_Reset, 2, 0, 1, 1)

        self.Btn_Run = QtGui.QPushButton(self.GroupBox_Settings)
        self.Btn_Run.setEnabled(True)
        font.setBold(False)
        font.setWeight(50)
        self.Btn_Run.setFont(font)
        self.Btn_Run.setFixedHeight(20)
        self.Btn_Run.setFixedWidth(70)
        self.Btn_Run.setObjectName(_fromUtf8("Btn_Run"))
        self.gridLayout_button.addWidget(self.Btn_Run, 3, 0, 1, 1)

        self.Progress_Run = QtGui.QProgressBar(self.GroupBox_Settings)
        self.Progress_Run.setProperty("value", 0)
        self.Progress_Run.setFixedHeight(15)
        self.Progress_Run.setFixedWidth(70)
        self.Progress_Run.setVisible(False)                                       #Progress bar is not visible before compress button is pushed
        self.Progress_Run.setObjectName(_fromUtf8("Progress_Run"))
        self.gridLayout_button.addWidget(self.Progress_Run, 4, 0, 1, 1)

        self.v.addWidget(self.GroupBox_Settings, 5, 0, 1, 1)                      #Add 2nd group box to master grid layout

        self.GroupBox_Settings.raise_()



        #But spacer between croup boxes
        spacerItem4 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.v.addItem(spacerItem4, 6, 0, 1, 1)



        #?????????????????
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "SimSyn", None))

        self.GroupBox_Connect.setTitle(_translate("MainWindow", "Database Connection", None))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(60)
        self.GroupBox_Connect.setFont(font)

        self.GroupBox_build.setTitle(_translate("MainWindow", "Model Connection", None))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(60)
        self.GroupBox_build.setFont(font)


        self.GroupBox_Settings.setTitle(_translate("MainWindow", "Data Link(s)", None))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(60)
        self.GroupBox_Settings.setFont(font)


        self.Password.placeholderText()
        self.Password.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.Port.placeholderText()
        self.Port.setPlaceholderText(_translate("MainWindow", "Port", None))
        self.User_Name.placeholderText()
        self.User_Name.setPlaceholderText(_translate("MainWindow", "User Name", None))
        self.Host_Name.placeholderText()
        self.Host_Name.setPlaceholderText(_translate("MainWindow", "Host", None))
        self.Table_Name.placeholderText()
        self.Table_Name.setPlaceholderText(_translate("MainWindow", "Table Name [comma delimit multiple tables]", None))
        self.Db_Name.placeholderText()
        self.Db_Name.setPlaceholderText(_translate("MainWindow", "Database Name", None))

        self.Btn_Connect.setText(_translate("MainWindow", "Connect Database", None))
        self.Btn_Build.setText(_translate("MainWindow", "Load Model", None))
        self.Btn_Run.setText(_translate("MainWindow", "Run", None))
        self.Btn_Reset.setText(_translate("MainWindow", "Reset...", None))

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icons/BrowseIcon_v01.png"))
        self.Btn_Browse_Ven.setIcon(icon)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Icons/PlusIcon3.png"))         #Cannot add vector svg!!!
        self.Btn_Plus.setIcon(icon2)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Icons/MinusIcon3.png"))         #Cannot add vector svg!!!
        self.Btn_Minus.setIcon(icon3)

        #Execute functions, if buttons are clicked
        self.Btn_Connect.clicked.connect(self.connectDb)
        self.Btn_Browse_Ven.clicked.connect(self.browse)
        self.Btn_Build.clicked.connect(self.loadVen)
        self.Btn_Plus.clicked.connect(self.addrow)
        self.Btn_Minus.clicked.connect(self.removerow)
        self.Btn_Reset.clicked.connect(self.reset)
        self.Btn_Run.clicked.connect(self.run)




    def connectDb(self):
        #Get DB specification
        name_db = self.Db_Name.text()
        user_nm = self.User_Name.text()
        host = self.Host_Name.text()
        passwrd = self.Password.text()
        pt = self.Port.text()

        #Format table names as 'Table 1', 'Table 2', 'Table 3' ...
        self.name_tb = ""
        for t in self.Table_Name.text().split(','):
            if self.name_tb != "":
                self.name_tb += ","
            self.name_tb += "'" + t + "'"

        #Delete empty space, if required
        try:
            self.name_tb.replace(" ", "")
        except:
            pass

        #Access Database, get column names of tables and save them as a self attribute of the class
        try:
            self.con = psycopg2.connect(dbname = name_db, host = host, port = int(pt), user = user_nm, password = passwrd)
            curs = self.con.cursor()
            curs.execute("SELECT column_name, table_name FROM information_schema.columns WHERE table_name IN (%s);" % AsIs(str(self.name_tb)))
            self.tb_columns = curs.fetchall()

            try:
                self.Progress_Label_con.clear()                                   #Reset label
            except:
                pass

            if len(self.tb_columns) == 0:
                self.error_message = QtGui.QMessageBox(self.centralwidget)
                self.error_message.setIcon(QtGui.QMessageBox.Critical)
                self.error_message.setWindowTitle("Connection Info")
                self.error_message.setText("Unable to connect to database!")
                self.error_message.setStandardButtons(QtGui.QMessageBox.Ok)
                self.error_message.exec_()

            else:
                font = QtGui.QFont()
                font.setBold(False)
                font.setWeight(15)
                self.Progress_Label_con = QtGui.QLabel()
                self.Progress_Label_con.setFont(font)
                self.gridLayout.addWidget(self.Progress_Label_con, 3, 1, 1, 1)
                self.Progress_Label_con.setText("Connected to " + self.name_tb)

        except:
            self.error_message = QtGui.QMessageBox(self.centralwidget)
            self.error_message.setIcon(QtGui.QMessageBox.Critical)
            self.error_message.setWindowTitle("Connection Info")
            self.error_message.setText("Unable to connect to database!")
            self.error_message.setStandardButtons(QtGui.QMessageBox.Ok)
            self.error_message.exec_()


    def browse(self):
        self.Model_Dir.setText(QtGui.QFileDialog.getOpenFileName())

    def loadVen(self):
        try:
            ven_path = str(self.Model_Dir.text())
            self.model = pysd.read_vensim(ven_path)

            self.message = QtGui.QMessageBox(self.centralwidget)
            self.message.setIcon(QtGui.QMessageBox.Information)
            self.message.setWindowTitle("Load VENSIM")
            self.message.setText("Successfully connected to '" + str(self.model.__str__.split("/")[-1]) + "'")
            self.message.setStandardButtons(QtGui.QMessageBox.Ok)
            self.message.exec_()

        except:
            self.error_message1 = QtGui.QMessageBox(self.centralwidget)          #self.centralwidget is used as parent to so that messagebox is centered above parent
            self.error_message1.setWindowTitle("Load VENSIM")
            self.error_message1.setText("Couldn't connect to VENSIM model.")
            self.error_message1.setIcon(QtGui.QMessageBox.Critical)
            self.error_message1.setStandardButtons(QtGui.QMessageBox.Ok)
            self.error_message1.exec_()

    def addrow(self):

        labels = []
        elem = []
        try:
            #Get name (labels) of PostgreSQL table columns
            for c in self.tb_columns:
                labels.append(c[0])

            #Get name (labels) VENSIM model elements
            for i in dir(self.model.components):
                if i[0] != "_" and i not in ['doc', 'time', 'time_step', 't', 'state_vector', 'state', 'final_time', 'functions', 'reset_state', 'saveper', 'd_dt']:  #Not very clean solution for filtering model elements!
                    elem.append(i)
        except:
            pass

        if (len(labels) == 0) or (len(elem) == 0):
            self.error_message2 = QtGui.QMessageBox(self.centralwidget)
            self.error_message2.setIcon(QtGui.QMessageBox.Critical)
            self.error_message2.setWindowTitle("Input Info")
            self.error_message2.setText("No database dataset or no VENSIM model loaded!")
            self.error_message2.setStandardButtons(QtGui.QMessageBox.Ok)
            self.error_message2.exec_()
        else:
            #Add Combobox as item to table
            rowPosition = self.Link_Tab.rowCount()
            self.Link_Tab.insertRow(rowPosition)
            self.Link_Tab.setRowHeight(rowPosition, 20)
            self.ven_var = QtGui.QComboBox()
            self.ven_var.addItems(labels)
            self.post_var = QtGui.QComboBox()
            self.post_var.addItems(elem)
            self.use = QtGui.QComboBox()
            self.use.addItems(["Time Series", "Subscript"])
            self.time_edit = QtGui.QLineEdit()
            font = QtGui.QFont()
            font.setBold(False)
            font.setWeight(50)
            self.time_edit.setFont(font)
            self.time_edit.setObjectName(_fromUtf8("time_edit"))
            #self.time_edit.setText("<Default is constant>")
            self.time_edit.setPlaceholderText("<Default is constant>")
            self.Link_Tab.setCellWidget(rowPosition,0,self.post_var)
            self.Link_Tab.setCellWidget(rowPosition,1,self.ven_var)
            self.Link_Tab.setCellWidget(rowPosition,2,self.use)
            self.Link_Tab.setCellWidget(rowPosition,3,self.time_edit)

    def removerow(self):
        rowPosition = self.Link_Tab.rowCount()
        self.Link_Tab.removeRow((rowPosition - 1))

    def reset(self):
        self.message1 = QtGui.QMessageBox(self.centralwidget)
        self.message1.setIcon(QtGui.QMessageBox.Information)
        self.message1.setWindowTitle("Reset Info")
        self.message1.setText("Outputs ('sim_out' table) of a previous run will be deleted!")
        self.message1.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
        retval = self.message1.exec_()
        if retval == 1024:
            curs = self.con.cursor()
            try:
                curs.execute(""" DROP TABLE sim_out; """)
                self.con.commit()
                del curs
                self.Progress_Run.setVisible(False)
            except:
                self.con.commit()
                del curs

    #So far users cannot decide what to consider in the output!!
    #Only VENSIM Stocks are written to separate PostGIS Table Columns
    def run(self):

        #Catch runtime error, if no links are set in table
        #Consider: Links can only be set if DB is connected and Simulation Input is selected
        if len(self.Link_Tab.findChildren(QtGui.QComboBox)) == 0:
            self.error_message3 = QtGui.QMessageBox(self.centralwidget)
            self.error_message3.setIcon(QtGui.QMessageBox.Critical)
            self.error_message3.setWindowTitle("Compression Info")
            self.error_message3.setText("No application links selected")
            self.error_message3.setStandardButtons(QtGui.QMessageBox.Ok)
            self.error_message3.exec_()

        #Catch exception: sim_out already exist --> Old compression schema (merge_id, sim_out) blocks compression
        bool_tab_exist = 0
        try:
            curs = self.con.cursor()
            curs.execute(""" SELECT * FROM sim_out WHERE gid = 1; """)
            bool_tab_exist = 1
            del curs
        except:
            self.con.commit()
            del curs

        if bool_tab_exist == 1:
            self.error_message5 = QtGui.QMessageBox(self.centralwidget)
            self.error_message5.setIcon(QtGui.QMessageBox.Critical)
            self.error_message5.setWindowTitle("Compression Info")
            self.error_message5.setText("Output already exists. Make a reset before execution.")
            self.error_message5.setStandardButtons(QtGui.QMessageBox.Ok)
            self.error_message5.exec_()

        #Count subscripting links
        subscripting_count = 0
        for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
            if (idx + 1) % 3 == 0:
                if itm.currentText() == "Subscript":
                    subscripting_count += 1

        ##make sure that subscripting table has 'geometry column'
        #Get name of subscripting table
        subscripting_table = []
        for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
            if (idx + 1) % 3 == 0:
                if itm.currentText() == "Subscript":
                    subscripting_table.append(self.tb_columns[self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentIndex()][1])
        subscripting_table = list(set(subscripting_table))
        print subscripting_table

        bool_tab_geom = 0
        try:
            curs = self.con.cursor()
            curs.execute("SELECT geom FROM %s WHERE gid = 1;" % AsIs(str(subscripting_table[0])))
            bool_tab_geom = 1
            del curs
        except:
            self.con.commit()
            del curs

        #Create sim_out table with geometry column (input subscripting table with geometry)
        if (subscripting_count > 0) and (bool_tab_geom == 1) and (bool_tab_exist == 0):

            try:
                curs = self.con.cursor()
                curs.execute("CREATE TABLE sim_out AS SELECT geom, gid FROM %s; ALTER TABLE sim_out ADD PRIMARY KEY (gid);" % AsIs(subscripting_table[0]))   #copy geom as spatial and gid as non-spatial foreign key
                self.con.commit()                                                                                                                            #gid is simultaniously used as foreign and primary key in 'sim_out' as table relation is 1 to 1
                del curs
            except psycopg2.OperationalError:
                self.error_message7 = QtGui.QMessageBox(self.centralwidget)
                self.error_message7.setIcon(QtGui.QMessageBox.critical)
                self.error_message7.setWindowTitle("Operational Error 1")
                self.error_message7.setText("Size of array exceeded (see Documentation)")
                self.error_message7.setStandardButtons(QtGui.QMessageBox.Ok)
                self.error_message7.exec_()

            curs = self.con.cursor()

            self.con.commit()
            del curs


        #Create sim_out table without geometry column (input subscripting table is non-spatial)
        if (subscripting_count > 0) and (bool_tab_geom == 0) and (bool_tab_exist == 0):

            try:
                curs = self.con.cursor()
                curs.execute("CREATE TABLE sim_out AS SELECT gid FROM %s; ALTER TABLE sim_out ADD PRIMARY KEY (gid);" % AsIs(subscripting_table[0]))    #copy gid as non-spatial foreign key
                self.con.commit()                                                                                                                       #gid is simultaniously used as foreign and primary key in 'sim_out' as table relation is 1 to 1
                del curs
            except psycopg2.OperationalError:
                self.error_message7 = QtGui.QMessageBox(self.centralwidget)
                self.error_message7.setIcon(QtGui.QMessageBox.critical)
                self.error_message7.setWindowTitle("Operational Error 1")
                self.error_message7.setText("Size of array exceeded (see Documentation)")
                self.error_message7.setStandardButtons(QtGui.QMessageBox.Ok)
                self.error_message7.exec_()


        #Assign time series to model
        for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
            if (idx + 1) % 3 == 0:
                if itm.currentText() == "Time Series":
                    #Get name of time series table
                    time_series_tb = []
                    time_series_tb.append(self.tb_columns[self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentIndex()][1])
                    time_series_tb = list(set(time_series_tb))

                    #print time_series_tb

                    #Fetch time series data from database
                    curs = self.con.cursor()
                    field = self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentText()
                    curs.execute("SELECT %s FROM %s;" % (field, time_series_tb[0]))
                    time_series = curs.fetchall()

                    #Assign data to model
                    pandas_t = []
                    pandas_d = []
                    for t,d in enumerate(time_series):
                        pandas_t.append(t)
                        pandas_d.append(d[0])
                    time_series_pd = pd.Series(index=pandas_t, data=pandas_d)
                    ven_var_ts = self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 2].currentText()
                    self.model.set_components(params={str(ven_var_ts):time_series_pd})

        #Only run subscripting procedure, if at least one subscripting link is selected
        if (subscripting_count != 0) and (bool_tab_exist == 0):
            #Get Table Links as List [[VENSIM Var. Name 1, PostGIS Var. Name 1, Time1], [VENSIM Var. Name 2, PostGIS Var. Name 2, Time2], [...], ...]
            table_links = []
            for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
                if (idx + 1) % 3 == 0:
                    if itm.currentText() == "Subscript":
                        if str(self.Link_Tab.findChildren(QtGui.QLineEdit)[((idx + 1) / 3) - 1].text()) != "":
                            table_links.append([str(self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 2].currentText()),
                            str(self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentText()), str(self.Link_Tab.findChildren(QtGui.QLineEdit)[((idx + 1) / 3) - 1].text())])
                        else:
                            table_links.append([str(self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 2].currentText()),
                            str(self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentText()), str(self.Link_Tab.findChildren(QtGui.QLineEdit)[((idx + 1) / 3) - 1].placeholderText())])

            #Check for duplicates in entries (Vensim Variable is assigned twice,
            #e.g. Table Row 1: 'albedo' | 'albedo0ad' | 0; Table Row 2: 'albedo' | 'albedo1000ad' | 0 --> albedo at time 0 can only have one value!)
            table_links_reduced = [x[::2] for x in table_links]
            dupl_count = 0
            for idx, itm in enumerate(table_links_reduced):
                for l in table_links_reduced:
                    if cmp(itm, l) == 0:
                        dupl_count+=1
            if dupl_count > len(table_links_reduced):
                self.error_message9 = QtGui.QMessageBox(self.centralwidget)
                self.error_message9.setIcon(QtGui.QMessageBox.Critical)
                self.error_message9.setWindowTitle("Input Error")
                self.error_message9.setText("Time constant or time dependent value assignment is redundant! Change time settings. Then reset, compress and rerun simulation.")
                self.error_message9.setStandardButtons(QtGui.QMessageBox.Ok)
                self.error_message9.exec_()

            ###Input error 'time origin > 0' is not implemented yet!!!

            else:
                #Make progress bar visible once run button is pushed
                self.Progress_Run.setVisible(True)

                #Add column, one per stock in the SD model, type array; also count rows in the table
                curs = self.con.cursor()
                for i in self.model.components._stocknames:
                    curs.execute("ALTER TABLE sim_out ADD COLUMN %s real[]" % i)        #real is 4 bytes per array element, double precision would be 8 bytes
                    self.con.commit()

                #Count rows of sim_out
                row_count = 0.0
                curs.execute(""" SELECT count(*) FROM sim_out; """)
                row_count = curs.fetchall()[0][0]

                #Get name of subscripting table
                subscripting_table = []
                for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
                    if (idx + 1) % 3 == 0:
                        if itm.currentText() == "Subscript":
                            subscripting_table.append(self.tb_columns[self.Link_Tab.findChildren(QtGui.QComboBox)[idx - 1].currentIndex()][1])
                subscripting_table = list(set(subscripting_table))

                #Fetch run, save
                g_count = 0.0
                for g in xrange(1,(row_count + 1)):

                    start = time.time()

                    pvars = [x[1] for x in table_links]
                    post_vars = str(pvars).replace('[', '').replace(']', '').replace("'", "")

                    SQL = ''' SELECT %s FROM %s WHERE gid = %s; ''' % (AsIs(post_vars), AsIs(subscripting_table[0]), g)

                    curs.execute(SQL)
                    self.con.commit()
                    post_data = curs.fetchall()
                    #curs.execute("""DROP TABLE tempo;""")

                    #Append Fetched PostGIS data to the tables link list [[VENSIM Var. Name 1, PostGIS Var. Name 1, Time1, PostGIS Value 1], [VENSIM Var. Name 2, PostGIS Var. Name 2, Time2, PostGIS Value 2], [...], ...]
                    for idx, itm in enumerate(table_links):
                        itm.append(post_data[0][idx])

                    #Set time constant parameters in Vensim model
                    for x in table_links:
                        if x[2] == "<Default is constant>":
                            self.model.set_components(params={x[0]:x[3]})

                    #end = time.time()
                    #print "Fetch " + str((end - start))

                    #start = time.time()

                    #Set time dependent parameters in Vensim model. Values are linearly interpolated between time dependent inputs
                    for v in list(set([x[0] for x in table_links if x[2].isalnum()])):
                        pandas_time = []
                        pandas_data = []
                        for x in table_links:
                            if (x[2].isalnum()) and (x[0] == v):
                                pandas_time.append(x[2])
                                pandas_data.append(x[3])

                        pandas_time_float = [float(x) for x in pandas_time]
                        pandas_data_float = [float(x) for x in pandas_data]
                        pandas_data_sorted = [x for (y,x) in sorted(zip(pandas_time_float,pandas_data_float))]      #sort pandas data by time
                        pandas_time_sorted = sorted(pandas_time_float)
                        look = pd.Series(index=pandas_time_sorted, data=pandas_data_sorted)
                        self.model.set_components(params={v:look})


                    #Run simulation for one collection element
                    st = self.model.run()

                    #end = time.time()
                    #print "Run " + str((end - start))

                    #Clear data value for next spatial object simulation run
                    for e in table_links:
                        del e[-1]

                    #start = time.time()

                    #save to database
                    for col in self.model.components._stocknames:
                        pd_lst = st[col].tolist()
                        curs.execute("UPDATE sim_out SET (%s) = (%s) WHERE gid = %s", (AsIs(col), pd_lst, g))
                        self.con.commit()

                    #Update progress
                    g_count += 1
                    complete = g_count / row_count * 100
                    self.Progress_Run.setValue(complete)
                    QtGui.QApplication.processEvents()                        #refresh application


                    end = time.time()
                    print "1 FRS " + str((end - start))

        #Check for number of time series links
        series_count = 0
        for idx, itm in enumerate(self.Link_Tab.findChildren(QtGui.QComboBox)):
            if (idx + 1) % 3 == 0:
                if itm.currentText() == "Time Series":
                    series_count += 1

        #If link schema includes time series links only, then run and save to sim_out
        if (subscripting_count == 0) and (series_count > 0) and (bool_tab_exist == 0):

            #Make progress bar visible once run button is pushed
            self.Progress_Run.setVisible(True)

            #create sim_out table
            curs = self.con.cursor()
            curs.execute(""" CREATE TABLE sim_out (gid BIGSERIAL PRIMARY KEY); """)
            self.con.commit()
            for i in self.model.components._stocknames:
                curs.execute("ALTER TABLE sim_out ADD COLUMN %s numeric" % i)        #real is 4 bytes per array element, double precision would be 8 bytes
                self.con.commit()
            del curs

            #Run
            st = self.model.run()

            #Save
            curs = self.con.cursor()
            stocks_str = str(self.model.components._stocknames).replace("[", "").replace("]", "").replace("'", "")
            for idx, row in st.iterrows():
                groups = ()
                for v in row:
                    groups += (v,)
                curs.execute("INSERT INTO sim_out (%s) VALUES %s" % (stocks_str, groups))
                self.con.commit()
            del curs

            self.Progress_Run.setValue(100)

        try:
            del curs
        except:
            pass

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create("plastique"))

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()                      #Create instance of class Ui_MainWindow() defined above
    ui.setupUi(MainWindow)                    #The class Ui_MainWindow inherits from class "QtGui.QMainWindow()" using method setupUi (see definition of method setupUi above)

    MainWindow.show()
    sys.exit(app.exec_())

