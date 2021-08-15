class Account:
    __minBalLimit = 100
    __numAccounts = 0

    def __init__(self, accountId, accountTitle, openingBal, emailID="Email ID not available", ):
        if openingBal < 5000:
            print("Opening balance is lower than Rs. 5000")
            self.__openingBal = 0
            self.__balance = 0
        else:
            print("Your Account is Sucessfully created")
            self.__openingBal = openingBal
            self.__balance = openingBal
        self.__accountId = str(self.__numAccounts + 1)
        self.__accountTitle = accountTitle
        self.__emailID = emailID
        Account.__numAccounts += 1

    #       SETTERS
    def setAccountID(self, accountID):
        self.__accountId = accountID

    def setAccountTitle(self, accountTitle):
        self.__accountTitle = accountTitle

    def setOpeningBal(self, openingBal):
        if openingBal < 5000:
            print("Opening balance is lower than Rs. 5000")
        else:
            self.__openingBal = openingBal

    def setEmailID(self, EmailID):
        self.__accountTitle = EmailID

    #       GETTERS
    def getAccountID(self):
        return self.__accountId

    def getAccountTitle(self):
        return self.__accountTitle

    def getOpeningBal(self):
        return self.__openingBal

    def getEmailID(self):
        return self.__emailID

    def getAccountBal(self):
        return self.__balance

    def getNumAccount(self):
        return self.__numAccounts

    def getMinBalLimit(self):
        return self.__minBalLimit

    def toString(self):

        return f"Account ID: {self.getAccountID()},\n" \
               f"Account Title: {self.getAccountTitle()},\n" \
               f"Account Balance: {self.getAccountBal()},\n" \
               f"E-mail ID :{self.getEmailID()},\n" \
               f"Openning Balance :{self.getOpeningBal()},\n" \
               f"________________________________________________"
n: str
A_bal: float

def Create_Account():
    global n, A_bal
    while True:
        try:
            n = input("enter your title name")
            if eval(n):
                raise ValueError

        except ValueError:
            print("please enter your title name...")

        except NameError:

            break

    while True:
        try:
            A_bal = eval(input("enter your Account Balance"))
            break
        except NameError:
            print("please enter account balnace")
for i in range(3):
    print("--------Create your Account-------")

    Create_Account()

    a1 = Account(0, n, A_bal, "forexample123@gmail.com")
    print(a1.toString())




