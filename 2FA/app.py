#imports
import random as random
import yagmail
from twilio.rest import Client
import Keys

def GenerateCode():
    RandomCode = random.randint(100000, 999999)
    return RandomCode

def AuthoriseCode(AuthCode):
    RandomCode = AuthCode
    CodeLoop = True
    while CodeLoop == True:
        UserInputCode = input(f"Please Enter The Code Recieved: \n")
        if UserInputCode == RandomCode:
            print("Correct Code")
            CodeLoop = False
        else:
            print("Wrong Code")

def SendEmail():
    UserEmailLoop = True
    while UserEmailLoop == True:
        UserEmailInput = input(f"Please Enter Your Email: \n")
        UserEmailConfirm = input(f"Please Enter Your Email Again To Confirm:\n")
        if UserEmailInput == UserEmailConfirm:
            print("Sending Email Now")
            UserEmailLoop = False
        else:
            print(f"Try Again\n")
            UserEmailLoop = True
    # Send password reset email
    AuthCode = str(GenerateCode())
    gmail_user = 'cmatty4500@gmail.com'
    app_password='axpcqlsmsdbymrya'
    to = UserEmailInput
    subject = 'Your 2FA Code'
    content = AuthCode
    with yagmail.SMTP(gmail_user, app_password) as yag:
        yag.send(to, subject, content)

    
    AuthoriseCode(AuthCode)

def SendSMS():
    UserPhoneNumberLoop = True
    while UserPhoneNumberLoop == True:
        UserPhoneNumberInput = input(f"Please Enter Your Phone Number Please Include Country Code: \n")
        UserPhoneNumberConfirm = input(f"Please Enter Your Phone Number With Country Code Again To Confirm:\n")
        if UserPhoneNumberInput == UserPhoneNumberConfirm:
            print("Sending Text Message Now")
            UserPhoneNumberLoop = False
        else:
            print(f"Try Again\n")
            UserPhoneNumberLoop = True
    # Send password reset email
    AuthCode = str(GenerateCode())
    client = Client(Keys.account_sid, Keys.auth_token)
    message = client.messages.create(
        body=AuthCode,
        from_= Keys.twilio_number,
        to = UserPhoneNumberConfirm
    )

    AuthoriseCode(AuthCode)
    
def MainMenu():
    MenuSelectorLoop = True
    while MenuSelectorLoop == True:
        MenuSelectorChoice = input(f"Please Type The Number Of The Option You Would Like To pick: \n1.Email Code\n2.SMS Code\n3.Cancel\n\n")
        if MenuSelectorChoice == "1":
            MenuSelectorLoop = False
            SendEmail()
        elif MenuSelectorChoice == "2":
            MenuSelectorLoop = False
            SendSMS()
        elif MenuSelectorChoice == "3":
            MenuSelectorLoop = False
            break
        else:
            MenuSelectorLoop = True


MainMenu()

