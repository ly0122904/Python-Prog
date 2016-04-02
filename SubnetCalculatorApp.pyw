import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

#ADD IMPORT STATEMENT FOR YOUR GENERATED UI.PY FILE HERE
import SubnetCalculatorUI

#CHANGE THE SECOND PARAMETER HERE TO MATCH YOUR GENERATED UI.PY FILE
class MyForm(QMainWindow, SubnetCalculatorUI.Ui_MainWindow):
    # set variable to carry the input network address and Number of host
    addressNW = ""
    hostNum = ""
    unsaved_changes = False

        # DO NOT MODIFY THIS CODE
    def __init__(self, parent=None):
        super(MyForm, self).__init__(parent)
        self.setupUi(self)
        # END DO NOT MODIFY

        # ADD SLOTS HERE
        #==1. Set action triggers
        self.actionOpenFile.triggered.connect(self.load_Data_from_file)
        self.actionSave_as.triggered.connect(self.saveFile)
        self.actionExit.triggered.connect(self.exit_application)
        self.actionCalculate.triggered.connect(self.SubnetCalculate)
        self.actionClear.triggered.connect(self.resetWindow)

        #==2. Set other slots
        self.pushButtonCalculate.clicked.connect(self.SubnetCalculate)
        self.pushButtonReset.clicked.connect(self.resetWindow)


    # ADD SLOT FUNCTIONS HERE
    def resetWindow(self):
        if self.unsaved_changes == True:
            msg = "Save changes to file?"
            reply = QMessageBox.question(self, 'Save?',
                 msg, QMessageBox.Yes, QMessageBox.No)

            if reply == QMessageBox.No:
                self.unsaved_changes = False        # reset the unsaved file check

            if reply == QMessageBox.Yes:
                self.saveFile()

        self.lineEditNWAddress.clear()
        self.lineEditNumHost.clear()
        self.lineEditSbSize.clear()
        self.lineEditDecimalOctets.clear()
        self.lineEditDecimalAddress.clear()
        self.lineEditBinaryOctets.clear()
        self.lineEditHexOctets.clear()
        self.lineEditNWClass.clear()
        self.lineEditIPAddress.clear()
        self.lineEditSubnetMask.clear()
        self.lineEditBinaryMask.clear()
        self.lineEditNumSubnet.clear()
        self.listWidgetIPRange.clear()

    def load_Data_from_file(self):
        # open file for read only
        with open("SubnetResults.txt","r") as myFile:
            textString = myFile.read()
            textList = textString.split("\n")

            self.lineEditNWAddress.setText(textList[0])
            self.lineEditNumHost.setText(textList[1])
            self.lineEditSbSize.setText(textList[2])
            self.lineEditDecimalOctets.setText(textList[3])
            self.lineEditDecimalAddress.setText(textList[4])
            self.lineEditBinaryOctets.setText(textList[5])
            self.lineEditHexOctets.setText(textList[6])
            self.lineEditNWClass.setText(textList[7])
            self.lineEditIPAddress.setText(textList[8])
            self.lineEditSubnetMask.setText(textList[9])
            self.lineEditBinaryMask.setText(textList[10])
            self.lineEditNumSubnet.setText(textList[11])
            for i in range (12,len(textList)-1):
                self.listWidgetIPRange.addItem(textList[i])

    def saveFile(self):
        # open the file for writing (w)
        with open("SubnetResults.txt","w") as myFile:
            #myFile.write("Subnet Calculator Result \n")
            myFile.write(self.lineEditNWAddress.text()+"\n")
            myFile.write(self.lineEditNumHost.text()+"\n")
            myFile.write(self.lineEditSbSize.text()+"\n")
            myFile.write(self.lineEditDecimalOctets.text()+"\n")
            myFile.write(self.lineEditDecimalAddress.text()+"\n")
            myFile.write(self.lineEditBinaryOctets.text()+"\n")
            myFile.write(self.lineEditHexOctets.text()+"\n")
            myFile.write(self.lineEditNWClass.text()+"\n")
            myFile.write(self.lineEditIPAddress.text()+"\n")
            myFile.write(self.lineEditSubnetMask.text()+"\n")
            myFile.write(self.lineEditBinaryMask.text()+"\n")
            myFile.write(self.lineEditNumSubnet.text()+"\n")
            f=self.listWidgetIPRange.count()            # integer for total items in listWidget
            for i in range(self.listWidgetIPRange.count()):
                aa=self.listWidgetIPRange.item(i).text()
                myFile.write(aa+"\n")

        self.unsaved_changes = False        # After saved reset it


    def exit_application(self):
        QApplication.closeAllWindows()

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit?"
        reply = QMessageBox.question(self, 'Exit?',
                 quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            # debug self.unsaved_changes == False
            if self.unsaved_changes == True:
                msg = "Save changes to file?"
                reply = QMessageBox.question(self, 'Save?',
                 msg, QMessageBox.Yes, QMessageBox.No)

                if reply == QMessageBox.No:
                    self.unsaved_changes = False        # reset the unsaved file check

                if reply == QMessageBox.Yes:
                    self.saveFile()
                    #event.accept()

            event.accept()
        else:
            event.ignore()

    def SubnetCalculate(self):
        self.addressNW = self.lineEditNWAddress.text()  # set the Network address
        self.hostNum = self.lineEditNumHost.text()  # Set the host number

        # Function for check the valid input
        checkNumber = self.CheckValid(self.addressNW,self.hostNum)
        if checkNumber == False: # if there is an invalid input clear everything
            self.resetWindow()
        else:
            # Calculate the Subnet Size
            varSubnetSize = self.CalculateSubnetSize(self.hostNum)
            self.lineEditSbSize.setText(str(varSubnetSize))

            # Get the decimal Octets
            varDecimalOctets = self.CalculateDecimalOctets(self.addressNW)
            self.lineEditDecimalOctets.setText(varDecimalOctets)

            # Get the decimal Address
            varDecimalAddress=self.CalculateDecimalAddress(self.addressNW)
            self.lineEditDecimalAddress.setText(str(varDecimalAddress))

            # Get the Binary Address
            varBinaryAddress=self.CalculateBinaryAddress(self.addressNW)
            self.lineEditBinaryOctets.setText(varBinaryAddress)

            # Get the Hex Address
            varHexAddress=self.CalculateHexAddress(self.addressNW)
            self.lineEditHexOctets.setText(varHexAddress)

            # Get the network class of the ip address
            varClass = self.CalculateNetworkClass(self.addressNW)
            self.lineEditNWClass.setText(varClass)

            # Get the number of network ip address
            varNumNWIP = self.CalculateNumberOfIPAddresses(self.addressNW)
            self.lineEditIPAddress.setText(str(varNumNWIP))

            # Get Subnet Mask
            varSubnetMask = self.CalculateSubnetMask(self.hostNum)
            self.lineEditSubnetMask.setText(varSubnetMask)

            # Get Binary Subnet Mask
            varBinSubnetMask = self.CalculateBinaryMask(self.hostNum)
            self.lineEditBinaryMask.setText(varBinSubnetMask)

            # Get Number of subnets
            varNumSubnet = self.CalculateNumberOfSubnets(self.addressNW,self.hostNum)
            self.lineEditNumSubnet.setText(str(varNumSubnet))

            # Get the List of Ip ranges
            varSubnetRangeList = self.CalculateSubnetList(self.addressNW,self.hostNum)
            self.listWidgetIPRange.clear()
            for varSubnet in varSubnetRangeList:
                self.listWidgetIPRange.addItem(varSubnet)

            # Set un_save to true for file save
            self.unsaved_changes = True

    #ADD HELPER FUNCTIONS HERE

    # Function for checking the valid input
    def CheckValid(self, ipAddressNW, numberHost): #<- return a bool True: Valid
        varCheck = True
        ipAddList = ipAddressNW.split(".")
        #debugger: ipAdd_NoDot = ipAddressNW.replace(".","")

        # Check the digits valid for input varCheck_Digit
        varCheck_Digit = True

        for i in ipAddList:
            try:
                a=int(i)
                if a > 255:
                    varCheck_Digit = False
            except:
                varCheck_Digit = False
                self.Error_Message_IPv4()
                break
        if varCheck_Digit == True:
            if len(ipAddList)!= 4:      # debugger: or ipAdd_NoDot.isdigit()== False:
                varCheck = False
                self.Error_Message_IPv4()
            elif numberHost.isdigit()== False:
                varCheck = False
                self.Error_Message_HostNumber()

        # Check the input ip address and host number match the network class
        # valid network ip address depending on it class
        # possible host= total available host - network and broadcast
        # available host number = 2**(Class C is 8, class B is 16, class A is 24)
        if (varCheck_Digit and varCheck) == True:
            varClassName = self.CalculateNetworkClass(ipAddressNW)
            if varClassName == "D" or varClassName == "E":
                varCheck = False
                self.Error_Message_IPv4()
            else:
                if varClassName == "A":         # Class A: sth.0.0.0
                    if ipAddList[3] != "0" or ipAddList[2] != "0" or ipAddList[1] != "0":
                        varCheck = False
                        self.Error_Message_NWAddress()
                    else:
                        if int(numberHost) > (2**24-2):
                            varCheck = False
                            self.Error_Message_HostIP()

                elif varClassName == "B":       # Class B:  sth.sth.0.0
                    if ipAddList[3] != "0" or ipAddList[2] != "0":
                        varCheck = False
                        self.Error_Message_NWAddress()
                    else:
                        if int(numberHost) > (2**16-2):
                            varCheck = False
                            self.Error_Message_HostIP()

                elif varClassName == "C":       # Class C: sth.sth.sth.0
                    if ipAddList[3] != "0":
                        varCheck = False
                        self.Error_Message_NWAddress()
                    else:
                        if int(numberHost) > 254:       # Class C: host 0~(256-2)
                            varCheck = False
                            self.Error_Message_HostIP()
        # debugger: print ("here", varCheck_In,varCheck)
        # debugger: print (varCheck and varCheck_Digit)
        return (varCheck and varCheck_Digit)

    # === Error Message Functions
    def Error_Message_IPv4(self):           # Error message for invalid IPV4 address
        errMsg_ipAdd = "Network Address must be a valid IPv4 address."
        QMessageBox.warning(self,"Invalid Data", errMsg_ipAdd)
    def Error_Message_HostNumber(self):     # Error message for invalid host number
        errMsg_Host = "Number of hosts must be a valid number."
        QMessageBox.warning(self,"Invalid Data", errMsg_Host)
    def Error_Message_NWAddress(self):      # Error message for invalid network address
        errMsg = "Network Address must be a valid network address."
        QMessageBox.warning(self,"Invalid Data", errMsg)
    def Error_Message_HostIP(self):         # Error message for invalid host number (match class)
        errMsg = "Number of hosts required is too big for the network class of Ip address."
        QMessageBox.warning(self,"Invalid Data", errMsg)

    #====== Required functions =======================

    def CalculateSubnetSize(self, numberHost): # returns an integer, Given a string
        b = bin(int(numberHost))[2:]
        varNum = 2**len(b)
        return varNum

    def CalculateDecimalOctets(self,ipAddress): # returns a string
        ipAddressString=ipAddress
        return ipAddressString

    def CalculateDecimalAddress(self,ipAddress): # returns an integer
        ipAddNumList = self.convertStrList(ipAddress)
        ipAddNumList.reverse() # reversed number list for the calculation

        total=0
        for i in range(0,4):
            total += ipAddNumList[i]*(256**i)
        return total

    def CalculateBinaryAddress(self,ipAddress): # returns a string
        ipAddNumList = self.convertStrList(ipAddress)
        varA = []
        for i in ipAddNumList:
            aa = self.convertBinary(i)
            varA.append(aa)

        return ".".join(varA)

    def CalculateHexAddress(self,ipAddress): # returns a string Hint: Research the built-in hex() #function
        ipAddNumList = self.convertStrList(ipAddress)
        varA = []
        for i in ipAddNumList:
            aa = self.convertHex(i)
            varA.append(aa)
        return ".".join(varA)

    def CalculateNetworkClass(self,ipAddress): # returns a string
        aValue = self.CalculateDecimalAddress(ipAddress)
        classATH = self.CalculateDecimalAddress("128.0.0.0")
        classBTH = self.CalculateDecimalAddress("192.0.0.0")
        classCTH = self.CalculateDecimalAddress("224.0.0.0")
        classDTH = self.CalculateDecimalAddress("240.0.0.0")
        classETH = self.CalculateDecimalAddress("256.0.0.0")
        if aValue < classATH:
            varCl = "A"
        elif aValue < classBTH:
            varCl = "B"
        elif aValue < classCTH:
            varCl = "C"
        elif aValue < classDTH:
            varCl = "D"
        elif aValue < classETH:
            varCl = "E"
        return varCl

    def CalculateNumberOfIPAddresses(self,networkIPAddress): # returns an integer
        varClassName = self.CalculateNetworkClass(networkIPAddress)
        if varClassName == "A":
            return 2**24
        elif varClassName == "B":
            return 2**16
        elif varClassName == "C":
            return 2**8

    def CalculateSubnetMask(self,numberOfHostsPerSubnet): # returns a string
        aString = self.CalculateBinaryMask(numberOfHostsPerSubnet) #<- aValue is a integer
        aList = aString.split(".")
        aNumList = []
        b = []
        for a in aList:
            a = int(a,2) # convert to decimal number
            b.append(str(a))
        stringSM = ".".join(b)
        numSM = aString.count("1")
        return stringSM + "  or /"+str(numSM)

    def CalculateBinaryMask(self,numberOfHostsPerSubnet): # returns a string
        aValue = self.CalculateSubnetSize(numberOfHostsPerSubnet)
        aBinStr = bin(aValue)[2:]
        binNum1 = int("11111111111111111111111111111111",2) #32 binary
        binNum2 = int(aBinStr,2)
        binNum3 = bin(binNum1- binNum2 + 1)
        ms = binNum3[2:]
        aSMstring = ms[:8]+"."+ms[8:16]+"."+ms[16:24]+"."+ms[24:]

        return aSMstring

    def CalculateNumberOfSubnets(self, ipAddress, numberOfHostsPerSubnet): # returns an integer
        varClassName = self.CalculateNetworkClass(ipAddress)
        varBinSM = self.CalculateBinaryMask(numberOfHostsPerSubnet)
        if varClassName == "A":
            aStr = varBinSM[9:]
        if varClassName == "B":
            aStr = varBinSM[18:]
        if varClassName == "C":
            aStr = varBinSM[27:]
        countOne = aStr.count("1")
        numSN = 2**countOne

        return numSN
    # Calculate List of ip address
    def CalculateSubnetList(self,ipAddress, numberOfHostsPerSubnet): # returns a list
        subnetList = []
        varClName = self.CalculateNetworkClass(ipAddress)   # string
        varSnSize = self.CalculateSubnetSize(numberOfHostsPerSubnet) # integer
        varNumSN = self.CalculateNumberOfSubnets(ipAddress,numberOfHostsPerSubnet) #
        ipAddressPrefix = []            # store prefix, length depend on network Class
        ipList = ipAddress.split(".")

        # Prefix depending on the network class
        if varClName == "C":
            varPrefix = 3
        if varClName == "B":
            varPrefix = 2
        if varClName == "A":
            varPrefix = 1
        # Save prefix in a list for future use
        for i in range(varPrefix):
            ipAddressPrefix.append(ipList[i])

        aaStr = ".".join(ipAddressPrefix)   #prefix store in a string for return

        a = 0
        x = 0
        y = 0
        # For Class C
        if varClName == "C":
            for j in range (varNumSN):
                bOneLine = self.oneLineIP(aaStr,varSnSize,a)
                a += varSnSize
                subnetList.append(bOneLine)
        # For Class B
        if varClName == "B":
            bbStr = aaStr+"."+str(ipList[2])
            for j in range (100):        #varNumSN):
                if a < 256:     # ip address for dot_decimal in range (0-255)
                    bOneLine = self.oneLineIP(bbStr,varSnSize,a)
                    a += varSnSize
                    subnetList.append(bOneLine)
                else:       # when last one over 256 reassign the last second dot-decimal number
                    x += int(a/256)
                    ipList[2]= x
                    a = int(a%256)
                    bbStr = aaStr+"."+str(ipList[2]) # updata prefix string for next j
        # For Class A
        if varClName == "A":
            bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2])
            for j in range (100):  #varNumSN):
                if a < 256:
                    bOneLine = self.oneLineIP(bbStr,varSnSize,a)
                    a += varSnSize
                    subnetList.append(bOneLine)
                else:       # when last one over 256 reassign the last second dot-decimal number
                    if x < 256:
                        x += int(a/256)
                        ipList[2]= x
                        a = int(a%256)
                        bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2]) # updata prefix string for next j
                    else:   # when last second over 256 reassign the last third dot-decimal number
                        y += int(x/256)
                        ipList[1] = y
                        x = int (x%256)
                        bbStr = aaStr+"."+str(ipList[1])+"."+str(ipList[2]) # updata prefix string for next j
        return subnetList

    #====== Other help calculation functions=========
    def convertStrList(self,ipAddString): # take in a string of ip address, return a list contain number of ip address
        aList = ipAddString.split(".")
        bList = []
        for aa in aList:
            bb = int(aa)
            bList.append(bb)
        return bList

    def convertBinary(self, a): # Get a number return a binary string octet
        b = bin(a)[2:]
        c=[]
        if len(b)< 8:
            for j in range(0,8-len(b)):
                c.append("0")
        result=c+list(b)
        return "".join(result)

    def convertHex(self, a): # Get a number return a Hex string
        b = hex(a)[2:].upper()
        if len(b) == 1:
            b = "0"+b[0]
        result = list(b)
        return "".join(result)

    # Function to add one ip address range to the Subnet List
    def oneLineIP(self,aString,subnetSize,aValue): #<- return string
        bbStr = aString+"."+str(aValue)
        aValue += subnetSize        # subnet size
        bbStr2 = aString+"."+str(aValue-1)
        bbResult = bbStr+" - "+bbStr2

        return bbResult

# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_form = MyForm()
    the_form.show()
    sys.exit(app.exec_())
# END DO NOT MODIFY
