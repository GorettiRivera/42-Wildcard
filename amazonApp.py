# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    amazonApp.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gorettirivera <gorettirivera@student.42    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/14 22:16:08 by mrivera-          #+#    #+#              #
#    Updated: 2019/10/14 22:17:15 by gorettirive      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tracker.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
# Build a Python App that tracks Amazon Prices! We are using python to make requests and do web scraping on amazon website.

from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import re


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(593, 396)
        icon = QtGui.QIcon.fromTheme("Shoop")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Amazon = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Amazon.setFont(font)
        self.Amazon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Amazon.setStyleSheet("")
        self.Amazon.setObjectName("Amazon")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Amazon)
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(11, 11, 11, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.Amazon)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.URL = QtWidgets.QLineEdit(self.Amazon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.URL.setFont(font)
        self.URL.setStyleSheet("")
        self.URL.setObjectName("URL")
        self.gridLayout.addWidget(self.URL, 0, 1, 1, 3)
        self.comboBox = QtWidgets.QComboBox(self.Amazon)
        self.comboBox.setObjectName("comboBox")
        # self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)
        self.Price = QtWidgets.QLineEdit(self.Amazon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Price.setFont(font)
        self.Price.setText("")
        self.Price.setObjectName("Price")
        self.gridLayout.addWidget(self.Price, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Amazon)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)
        self.Email = QtWidgets.QLineEdit(self.Amazon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.Email.setFont(font)
        self.Email.setText("")
        self.Email.setObjectName("Email")
        self.gridLayout.addWidget(self.Email, 2, 2, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.Amazon)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.Amazon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 3, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        self.Alert = QtWidgets.QPushButton(self.Amazon)
        self.Alert.setStyleSheet("QPushButton:Hover{\n"
                                 "color:Black;\n"
                                 "font:Bold;\n"
                                 # "backgroud:rgb(51, 78, 255)\n"
                                 "}")
        self.Alert.clicked.connect(self.check_price) #HERE
      

        self.Alert.setObjectName("Alert")
        self.verticalLayout.addWidget(self.Alert)
        self.verticalLayout_2.addWidget(self.Amazon)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 593, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Amazon Price Tracker"))
        self.Amazon.setTitle(_translate("MainWindow", "Amazon Price Tracker"))
        self.label.setText(_translate("MainWindow", "URL:"))
        self.URL.setPlaceholderText(_translate(
            "MainWindow", "Please enter a valid URL"))
        # self.comboBox.setItemText(0, _translate("MainWindow", ">="))
        self.comboBox.setItemText(0, _translate("MainWindow", "<="))
        self.Price.setPlaceholderText(_translate(
            "MainWindow", "Please enter the desired price"))
        self.label_3.setText(_translate("MainWindow", "Email:"))
        self.Email.setPlaceholderText(_translate(
            "MainWindow", "Please enter a valid email"))
        self.label_2.setText(_translate("MainWindow", "Price:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; color:#000000;\"><br /></p></body></html>"))
        self.Alert.setText(_translate("MainWindow", "Setup Alert!"))

    def check_price(self):

        lineedit = self.URL.text()
        listPrice = self.Price.text()
        Email = self.Email.text()
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

        if self.validation_url(lineedit) & self.validation_price(listPrice) & self.validation_email(Email,regex):

            headers = {
                "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
           
            page = requests.get(lineedit, headers=headers)

            soup = BeautifulSoup(page.content, 'html.parser')
            soup1 = BeautifulSoup(soup.prettify(), "html.parser")

            # title
            try:
                title = soup1.find(id="productTitle").get_text().strip()
            except:
                pass

            # price
            try:
                if soup1.find(id="priceblock_saleprice"):
                    price = soup1.find(id="priceblock_saleprice").get_text()
                if soup1.find(id="priceblock_ourprice"):
                    price = soup1.find(id="priceblock_ourprice").get_text()
                if soup1.find(id="priceblock_dealprice"):
                    price = soup1.find(id="priceblock_dealprice").get_text()
                if not price:
                    print(
                        "Sorry, We don't know when or if this item will be back in stock.")
                else:
                    converted_price = price[1:].strip()
                    converted_price = converted_price.replace(",", "")
                    converted_price = converted_price.replace("$", "")
                    converted_price = float(converted_price)
            except:
                print("Error, please check the price")
                self.textBrowser.append(str("Error, please check the price"))

            print(title.strip())
            word1 = '<span style=\" color: #000000; font-weight: bold;\">Product Name: </span>'
            self.textBrowser.append(str(word1 + title.strip()))
            print(converted_price)
            word2 = '<span style=\" color: #000000; font-weight: bold;\"><br />Price: </span>'
            self.textBrowser.append(str(word2) + str(converted_price))
            convertedExpectedprice = float(listPrice)
            text = str(self.comboBox.currentText())
            word3 = '<span style=\" color: #1D12A6; font-weight: bold; \"><br />Alert executed!. It will run again in 24 hours. </span>'
            self.textBrowser.append(str(word3))
            # if text == '>=':
            #     if(converted_price >= convertedlistprice):
            #         self.send_mail(lineedit, Email, regex)
            if text == '<=':
                if(converted_price <= convertedExpectedprice):
                    self.send_mail(lineedit, Email, regex)
                    print("Email sent")
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.check_price)
        self.timer.start(86400000)  # the time is in milliseconds, so it is set 1 day(86400000) -- 1min(60000)
            

    def send_mail(self, URL, Email, regex):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('amazontrackerprice@gmail.com', 'qanfcpmvgnexaibd')

        subject = 'Price fell down!!'
        body = f"Check the amazon link: ' {URL}"
    
        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            'amazontrackerprice@gmail.com',
            Email,
            msg
        )

        word3 = '<span style=\" color: #1D12A6; font-weight: bold;\"><br />The product price has reduced, check your email for more details!</span>'
        self.textBrowser.append(str(word3))

        server.quit()

    def validation_url(self,lineedit):
       
        if lineedit.find('https://www.amazon.com/') != -1:
            return True
        else:
            print("Invalid URL, please enter a valid URL")
            self.textBrowser.append(
                str("Invalid URL, please enter a valid URL"))
            return False

    def validation_price(self, listPrice):
        
        if listPrice.isdigit():
            return True
        else:
            print("Invalid price, please enter a valid price")
            self.textBrowser.append(
                str("Invalid price, please enter a valid price"))
            return False

    def validation_email(self,Email,regex):
       
        if re.search(regex, Email):
            return True
        else:
            print("Invalid Email, please enter a valid Email")
            self.textBrowser.append(
                str("Invalid Email, please enter a valid Email"))
            return False
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
