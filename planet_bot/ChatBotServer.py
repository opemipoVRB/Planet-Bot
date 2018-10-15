#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$...........................................................................$$
$$..........................$$$$$$$$$$$$$....................................$$
$$.......................$$$$$$$$$$$$$$$$$$$.................................$$
$$.....................$$$$$$$$$$$$$$$$$$$$$$$...............................$$
$$....................$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$.$$...............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$...$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$.$$...$$$.............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$....................$$$$$$$$$$$$$.....$$$$$$$$$............................$$
$$......................$$$$$$$$$$$$$$$$..$$$$$$$............................$$
$$...................................$$$.....................................$$
$$.................$$................$$$$ $$$$$$$........$...................$$
$$...............$$$$$$..............$$$$$$$$$$$$$...$$$$$$..................$$
$$............$$$$..$$$$$.........................$$$$$$$$$..................$$
$$............$$$$...$$$$$$$....................$$$$$$.$$.$$.................$$
$$...............$$$$$$$$$$$$$$............$$$$$$$$..........................$$
$$.........................$$$$$$$$$...$$$$$$$...............................$$
$$..............................$$$$$$$$$$...................................$$
$$..........................$$$$$....$$$$$$$$$...............................$$
$$............$$.$$$$$$$$$$$$$............$$$$$$$$$$$$$$$$$..................$$
$$............$$.$$..$$$$.....................$$$$$$$$$$$$$$.................$$
$$..............$$$$$$............................$$.$$$$$$$.................$$
$$..................                                   ......................$$
$$.................. @@@  @@@  @@@@@@@        @@@@@@@ .......................$$
$$.................. @@@  @@@  @@@   @@@@     @@@   @@@@.....................$$
$$.................. @@!  @@@  @@!   !@@      @@!   !@@......................$$
$$.................. !@!  @!@  !@!   !@!      !@!   !@!......................$$
$$.................. @!@  !@!  !!@!@!!@@!     !!@!@!!@@!.....................$$
$$.................. !@!  !!!  !!!      !!!   !!!     !!!....................$$
$$.................. :!:  !!:  !!:      :!!   !!:     :::....................$$
$$................... ::!!:!   :!:      :!:   :!:     :::....................$$
$$.................... ::::    :::      :::   :::     :::....................$$
$$...................... :      :        :      :::::::  ....................$$
$$...........................................................................$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$***************************************************************************$$
$$      ChatBotServer.py  Created by  Durodola Opemipo 2018                  $$
$$    Official Email : <durodola.opemipo@venturegardengroup.com>             $$
$$            Personal Email : <opemipodurodola@gmail.com>                   $$
$$                 Telephone Number: +2348182104309                          $$
$$***************************************************************************$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
import sys
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.utils import make_msgid

from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol
from twisted.internet import reactor
from twisted.python import log

#

port = 3000


class ChatBotServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        super().__init__()
        self.driver = []
        self.company = {}
        self.process = "REGISTER"
        self.form_field = None
        self.previous_process = None

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        self.factory.register(self)
        print("Client connected: {0}".format(self.peer))

    def connectionLost(self, reason):
        self.factory.unregister(self)
        print("Client disconnected: {0}".format(self.peer))

    def onMessage(self, payload, isBinary):

        payload = payload.decode('utf-8')
        client = self
        print("Client {0} sending message: {1}".format(self.peer, payload))
        # self.factory.communicate(self, "Hello world!!", True)

        print(" State of Server ", self.process)
        if self.process == "REGISTER":
            self.registerUser(client, payload)
        elif self.process == "CHATBOT":
            self.handle_CHAT(client, payload)
        elif self.process == "DRIVER_LICENSE_APPLICATION":
            self.handle_DRIVER_LICENSE_FORM(client, payload)
        elif self.process == "CHECK_DRIVER_LICENSE_STATUS":
            self.check_DRIVER_LICENSE_STATUS(client, payload)
        elif self.process == "COMPANY_REGISTRATION":
            self.handle_COMPANY_REGISTERATION(client, payload)
        elif self.process == "CAC_APPLICATION":
            self.handle_CAC_FORM(client, payload)
        elif self.process == "CAC_APPLICATION_2":
            self.handle_CAC_FORM_TWO(client, payload)
        else:
            self.bot_response(client, "Sorry I don't understand you.")
            print(self.previous_process)
            print(self.process)
            self.process = self.previous_process

    def registerUser(self, client, data):
        # if user phone number matches existing phone number return user's name
        #  else ask user to register
        if data == "08163635292":
            self.bot_response(client, "Thank you !!")
            response = 'So I\'ve been specially trained and commissioned to help you ' \
                       'access basic ' + \
                       'services<br/> \n ' + 'from on-boarded government agencies in Nigeria.<br/> \n' + \
                       'The following are the list of agencies that' + \
                       ' you can access their services right now<br/> \n' + \
                       '** FIRS **<br/> \n' + \
                       '** FRSC **<br/> \n' + \
                       '** CAC **<br/> \n'
            self.bot_response(client, response)
            self.company["Company-Name"] = "Fire Storm"
            self.company["Venture-Classification"] = "Company"
            self.company["Company-Type"] = "PRIVATE COMPANY LIMITED BY SHARES"
            self.company["D-O-B"] = "01/20/1991"
            self.company["PHONE-NO"] = "08163635292"
            self.process = "CHATBOT"
        else:
            response = 'I\'ve been specially trained and commissioned to help you ' \
                       'access basic ' + \
                       'services<br/> \n ' + 'from on-boarded government agencies in Nigeria.<br/> \n' + \
                       'The following are the list of agencies that' + \
                       ' you can access their services right now<br/> \n' + \
                       '** FIRS **<br/> \n' + \
                       '** FRSC **<br/> \n' + \
                       '** CAC **<br/> \n'
            self.bot_response(client, response)
            self.process = "CHATBOT"


        return

    def handle_CHAT(self, client, data):
        # message = self.getTime() + "<%s> %s" % (self.name, message)
        #### Load metadata into json #####

        def user_input(_message):
            # server sends client handle with message. This enables chatbot to respond to different people
            # concurrently
            try:
                _message = _message.strip()
            except AttributeError:
                _message = _message["message"]
            return _message

        _input_ = data
        entity, value, confidence = wit_response(user_input(_input_))  # pass user response as argument
        if confidence >= 0.5:
            try:
                # 1
                if entity == 'frsc_agent':
                    response = "Would you like to..<br/> \n" \
                               "**Apply for License**<br/> \n" \
                               "**Renew License**<br/> \n" \
                               "**Check Status of Application**<br/> \n"

                    self.bot_response(client, response)
                # 2
                if entity == 'apply_frsc_license':
                    response = "Application for drivers license initiated..."
                    self.process = "DRIVER_LICENSE_APPLICATION"
                    self.form_field = "FIRST_NAME"
                    self.bot_response(client, response)
                    self.bot_response(client, "Enter first name :>>> ")
                    return

                    # 3
                if entity == 'renew_frsc_license':
                    response = "Renewal for drivers license processing..."
                    self.bot_response(client, response)

                # 4
                if entity == 'check_frsc_license_application_status':
                    response = " Drivers license awaiting Director Signature..."
                    self.bot_response(client, response)
                    self.bot_response(client, "Enter License No. :>>> ")
                    self.process = "CHECK_DRIVER_LICENSE_STATUS"
                    return

                # 5
                if entity == 'firs_agent':
                    response = "Would you like to..<br/> \n" \
                               "**Pay my tax**<br/> \n" \
                               "**Get tax clearance Certificate**<br/> \n"
                    self.bot_response(client, response)
                # 6
                if entity == 'pay_tax_action':
                    response = "Doing thing's that pays your tax..."

                    self.bot_response(client, response)
                # 7
                if entity == 'get_tax_clearance':
                    response = "Requesting for your tax clearance...."

                    self.bot_response(client, response)
                # 8
                if entity == 'cac_agent':
                    response = "Would you like to do with CAC(CORPORATE AFFAIRS COMMISION)? <br/>\n" \
                               "Enter <b>1</b> to <i>Register a new company</i><br/>\n" \
                               "Enter <b>2</b> to <i>Continue Registration</i><br/>\n"
                    self.bot_response(client, response)
                    self.process = "COMPANY_REGISTRATION"

                if entity == 'intent':
                    response = 'I\'ve been specially trained and commissioned to help you ' \
                               'access basic ' + \
                               'services<br/> \n ' + 'from on-boarded government agencies in Nigeria.<br/> \n' + \
                               'The following are the list of agencies that' + \
                               ' you can access their services right now<br/> \n' + \
                               '** FIRS **<br/> \n' + \
                               '** FRSC **<br/> \n' + \
                               '** CAC **<br/> \n'
                    self.bot_response(client, response)

            except KeyboardInterrupt:
                pass
        else:
            self.previous_process = self.process
            self.bot_response(client, "Sorry I don't understand you.")

    def bot_response(self, client, message):  # include client parameter
        print("Client is Self ", client == self)
        self.factory.communicate(client=client, payload=message, isBinary=True)
        print("Client ", client, "Self ", self)

    def handle_COMPANY_REGISTERATION(self, client, data):
        choice = data
        if choice.isdigit():
            if choice == "1":
                self.process = "CAC_APPLICATION"
                self.bot_response(client, "Enter your first name please  ")
                self.form_field = "FIRST_NAME"

            elif choice == "2":
                try:
                    self.process = "CAC_APPLICATION_2"
                    preview = "Company Name <b> {} </b> <br/>" \
                              "Venture Classification <b> {}</b><br/>" \
                              "Company Type <b> {}</b> <br/>" \
                              "Date Of Birth <b> {}</b><br/>" \
                              "Phone No <b>{} </b>".format(self.company["Company-Name"]
                                                           , self.company["Venture-Classification"]
                                                           , self.company["Company-Type"]
                                                           , self.company["D-O-B"]
                                                           , self.company["PHONE-NO"])
                    self.bot_response(client,
                                      "Welcome back, you already started a conversation with Alexa <b>below are "
                                      "the "
                                      "details</b>.")
                    self.bot_response(client, preview)
                    self.bot_response(client, "Enter your first name please  ")
                    self.form_field = "FIRST_NAME"
                except KeyError:
                    self.bot_response(client, "You do not have existing record. Please enter 1 to continue.")
                    self.process = "COMPANY_REGISTRATION"
            else:
                self.bot_response(client, "Invalid entry")
                print("Invalid entry")
                self.process = "CHATBOT"
                payload = "CAC".encode("utf-8")
                self.onMessage(payload, False)
        else:
            self.bot_response(client, "Invalid entry")
            self.process = "CHATBOT"
            payload = "CAC".encode("utf-8")
            self.onMessage(payload, False)
        return

    def handle_CAC_FORM_TWO(self, client, data):
        if self.form_field == "FIRST_NAME":
            self.company["FIRST_NAME"] = data
            self.form_field = "LAST_NAME"
            self.bot_response(client, "and  your Last name. ")
            return
        elif self.form_field == "LAST_NAME":
            self.company["LAST_NAME"] = data
            self.form_field = "EMAIL"
            self.bot_response(client, "So what is your email address")
            return
        elif self.form_field == "EMAIL":
            self.company["EMAIL"] = data
            self.form_field = "ADDRESS"
            self.bot_response(client, "Please provide your address in the following format:<br/> "
                                      "Country State City Address")
            return
        elif self.form_field == "ADDRESS":
            self.company["Address"] = data
            self.form_field = "R-O-S"
            self.bot_response(client, "Reason for availability search ?")
            self.bot_response(client, "Enter 1 for - New Incorporation<br/>"
                                      "Enter 2 for - Change of Name<br/>"
                                      "Enter 3 for - Conversion..<br/>"
                                      "Enter 4 for -Subsidiary/Affilate ..<br/>")
            return
        elif self.form_field == "R-O-S":
            if data == "1":
                self.company["R-O-S"] = "New Incorporation"
            elif data == "2":
                self.company["R-O-S"] = "Change of Name"
            elif data == "3":
                self.company["R-O-S"] = "Conversion"
            elif data == "4":
                self.company["R-O-S"] = "Subsidiary/Affilate"
            else:
                self.bot_response(client, "Invalid Entry")
                self.bot_response(client, "Reason for availability search ?")
                self.bot_response(client, "Enter 1 for - New Incorporation<br/>"
                                          "Enter 2 for - Change of Name<br/>"
                                          "Enter 3 for - Conversion..<br/>"
                                          "Enter 4 for -Subsidiary/Affilate ..<br/>")
                return

            self.form_field = "ID-TYPE"
            self.bot_response(client, "Select your means of Identification<br/>"
                                      "Enter 1 for - Int'l Passport <br/>"
                                      "Enter 2 for - Driver's License <br/>"
                                      "Enter 3 for - National ID card <br/>"
                                      "Enter 4 for - Age Declaration <br/>"
                                      "Enter 5 for - Birth Certificate <br/>"
                                      "Enter 6 for - Permanent Voter's Card<br/>")

            return

        elif self.form_field == "ID-TYPE":
            if data == "1":
                self.company["Id-Type"] = "Int'l Passport"
            elif data == "2":
                self.company["Id-Type"] = "Driver's License"
            elif data == "3":
                self.company["Id-Type"] = "National ID card"
            elif data == "4":
                self.company["Id-Type"] = "Age Declaration"
            elif data == "5":
                self.company["Id-Type"] = "Birth Certificate"
            elif data == "6":
                self.company["Id-Type"] = "Permanent Voter's Card"
            else:
                self.bot_response(client, "Select your means of Identification<br/>"
                                          "Enter 1 for - Int'l Passport <br/>"
                                          "Enter 2 for - Driver's License <br/>"
                                          "Enter 3 for - National ID card <br/>"
                                          "Enter 4 for - Age Declaration <br/>"
                                          "Enter 5 for - Birth Certificate <br/>"
                                          "Enter 6 for - Permanent Voter's Card<br/>")
                return

            self.id_card = self.company["Id-Type"]
            self.form_field = "ID-NO"
            self.bot_response(client, "Please Enter your " + self.id_card + "  Number")
            return

        elif self.form_field == "ID-NO":
            self.company["Id-No"] = data
            self.form_field = "PREVIEW"
            self.bot_response(client, "I guess we are done here can you confirm your details?")
            # self.bot_response(client, self.company)
            self.response = "***********************************<br/> " \
                            "<b><i>Company Details</i> </b>***************<br/>" \
                            "1* Company Proposed Name Option 1 <b> <br/>" + self.company["Company-Name"] + "</b><br/>" \
                                                                                                           "2* Company Proposed Name Option 2 " \
                                                                                                           "3* Venture Classification <b>" + \
                            self.company["Venture-Classification"] + "</b><br/>" \
                                                                     "4* Venture Type <b>" + self.company[
                                "Company-Type"] + "</b><br/>" \
                                                  "<b><i>Additional Comments </b></i> <br/>" \
                                                  "<b><i>Presenter Details</b></i> ************ <br/>" \
                                                  "5* First name <b>" + self.company["FIRST_NAME"] + "</b><br/>" \
                                                                                                     "6* Last name <b>" + \
                            self.company["LAST_NAME"] + "</b><br/>" \
                                                        "7* Telephone <b>" + self.company["PHONE-NO"] + "</b><br/>" \
                                                                                                        "8* Email <b>" + \
                            self.company["EMAIL"] + "</b><br/>" \
                                                    "9* Contact Address<b>" + self.company["Address"] + "</b><br/>" \
                                                                                                        "10* Date of Birth   <b>" + \
                            self.company["D-O-B"] + "</b><br/>" \
                                                    "11* Identification Method <b>" + self.company[
                                "Id-Type"] + "</b><br/>" \
                                             "12* ID NO   <b>" + self.company["Id-No"] + "</b><br/>" \
                                                                                         "If you would like to change any field enter the field number " \
                                                                                         "else enter 0 to submit your form "

            # print(" Got this response ", response)
            self.bot_response(client, self.response)

            return

        elif self.form_field == "PREVIEW":

            message_text = """
                           <html>
                          "<b><i>Company Details</i> </b>***************<br/>
                          Company Proposed Name Option 1 <b> <br/> {company_name} </b><br/> 
                          Company Proposed Name Option 2 
                          Venture Classification <b> {venture_classification} </b><br/> 
                          Venture Type <b>  {company_type} </b><br/>
                          <b><i>Additional Comments </b></i> <br/>
                          <b><i>Presenter Details</b></i> ************ <br/> 
                          First name <b> {first_name} </b><br/>
                          Last name <b> {last_name}</b><br/>
                          Telephone <b> {phone_no}</b><br/>
                          Email <b> {email} </b><br/> 
                          Contact Address<b> {address} </b><br/>
                          Date of Birth <b> {d_o_b} </b><br/>
                          Identification Method <b>  {id_type} </b><br/>
                          ID NO   <b>  {id_number} </b><br/>
                          </html>
                          """.format(company_name=self.company["Company-Name"]
                                     , venture_classification=self.company["Venture-Classification"]
                                     , company_type=self.company["Company-Type"]
                                     , first_name=self.company["FIRST_NAME"]
                                     , last_name=self.company["LAST_NAME"]
                                     , phone_no=self.company["PHONE-NO"]
                                     , email=self.company["EMAIL"]
                                     , address=self.company["Address"]
                                     , d_o_b=self.company["D-O-B"]
                                     , id_type=self.company["Id-Type"]
                                     , id_number=self.company["Id-No"]
                                     , subtype='html')

            self.bot_response(client, data)
            self.bot_response(client, "You Confirmed this preview. <br/>"
                                      "Well an e-mail has been sent to you. ")
            message = MIMEText(message_text, 'html')
            message['From'] = "CORPORATE AFFAIRS COMMISSION <noreply@1gov.ng.com>"
            message['To'] = 'Mr/Mrs {first_name} {last_name} < {email} >'.format(
                first_name=self.company["FIRST_NAME"]
                , last_name=self.company["LAST_NAME"]
                , email=self.company["EMAIL"])
            message['Subject'] = 'CORPORATE AFFAIRS COMMISSION'
            msg_full = message.as_string()

            send_message(msg_full, receivers=[self.company["EMAIL"]])

            self.form_field = None
            self.process = "CHATBOT"
            return

    def handle_CAC_FORM(self, client, data):
        if self.form_field == "FIRST_NAME":
            self.company["FIRST_NAME"] = data
            self.form_field = "LAST_NAME"
            self.bot_response(client, "and  your Last name. ")
            return
        elif self.form_field == "LAST_NAME":
            self.company["LAST_NAME"] = data
            self.form_field = "PHONE-NO"
            self.bot_response(client, "I'm going to need your phone number. ")
            return
        if self.form_field == "PHONE-NO":
            self.company["PHONE-NO"] = data
            self.form_field = "EMAIL"
            self.bot_response(client, "So what is your email address")
            return
        elif self.form_field == "EMAIL":
            self.company["EMAIL"] = data
            self.form_field = "DATE_OF_BIRTH"
            self.bot_response(client, "Please, provide me with your date of birth in this format: dd/mm/yyyy")
            return
        elif self.form_field == "DATE_OF_BIRTH":
            self.company["D-O-B"] = data
            self.form_field = "ADDRESS"
            self.bot_response(client, "Please provide your address in the following format:<br/> "
                                      "Country State City Address")
            return
        elif self.form_field == "ADDRESS":
            self.company["Address"] = data
            self.form_field = "NATIONALITY"
            self.bot_response(client, "What is your nationality? For Nigerian, Kindly select, while others, "
                                      "input your details")
            return
        elif self.form_field == "NATIONALITY":
            self.company["Nationality"] = data
            self.form_field = "COMPANY-NAME"
            self.bot_response(client, "What is the name of the proposed company?")
            return
        elif self.form_field == "COMPANY-NAME":
            self.company["Company-Name"] = data
            self.bot_response(client, "Congratulations! " + data + " has not been registered by anyone.")
            self.form_field = "VENTURE-CLASSIFICATION"
            self.bot_response(client, "How can your venture be classified?")
            self.bot_response(client, "Enter 1 for - Business<br/> "
                                      "Enter 2 for - Company<br/>"
                                      "Enter 3 for - Incorporated trustee")

            return
        elif self.form_field == "VENTURE-CLASSIFICATION":
            if data == "1":
                self.company["Venture-Classification"] = "Business"
            elif data == "2":
                self.company["Venture-Classification"] = "Company"
            elif data == "3":
                self.company["Venture-Classification"] = "Incorporated trustee"
            else:
                self.bot_response(client, "Invalid entry")
                self.bot_response(client, "How can your venture be classified?")
                self.bot_response(client, "Enter 1 for - Business<br/> "
                                          "Enter 2 for - Company<br/>"
                                          "Enter 3 for - Incorporated trustee")
                return

            self.form_field = "COMPANY-TYPE"
            self.bot_response(client, "What type of company is it?")
            self.bot_response(client, "Enter 1 for - PRIVATE COMPANY LIMITED BY SHARES<br/>"
                                      "Enter 2 for -PUBLIC COMPANY LIMITED BY SHARES<br/>"
                                      "Enter 3 for - PRIVATE COMPANY LIMITED BY ..<br/>"
                                      "Enter 4 for -PUBLIC COMPANY LIMITED BY ..<br/>"
                                      "Enter 5 for - PRIVATE UNLIMITED COMPANY <br/>"
                                      "Enter 6 for -PUBLIC UNLIMITED COMPANY <br/>"
                              )

            return
        elif self.form_field == "COMPANY-TYPE":
            if data == "1":
                self.company["Company-Type"] = "PRIVATE COMPANY LIMITED BY SHARES"
            elif data == "2":
                self.company["Company-Type"] = "PUBLIC COMPANY LIMITED BY SHARES"
            elif data == "3":
                self.company["Company-Type"] = "PRIVATE COMPANY LIMITED BY "
            elif data == "4":
                self.company["Company-Type"] = "PUBLIC COMPANY LIMITED BY"
            elif data == "5":
                self.company["Company-Type"] = "PRIVATE UNLIMITED COMPANY"
            elif data == "6":
                self.company["Company-Type"] = "PUBLIC UNLIMITED COMPANY"
            else:
                self.bot_response(client, "Invalid Entry")
                self.bot_response(client, "What type of company is it?")
                self.bot_response(client, "Enter 1 for - PRIVATE COMPANY LIMITED BY SHARES<br/>"
                                          "Enter 2 for -PUBLIC COMPANY LIMITED BY SHARES<br/>"
                                          "Enter 3 for - PRIVATE COMPANY LIMITED BY ..<br/>"
                                          "Enter 4 for -PUBLIC COMPANY LIMITED BY ..<br/>"
                                          "Enter 5 for - PRIVATE UNLIMITED COMPANY <br/>"
                                          "Enter 6 for -PUBLIC UNLIMITED COMPANY <br/>"
                                  )

                return

            self.form_field = "R-O-S"
            self.bot_response(client, "Reason for availability search ?")
            self.bot_response(client, "Enter 1 for - New Incorporation<br/>"
                                      "Enter 2 for - Change of Name<br/>"
                                      "Enter 3 for - Conversion..<br/>"
                                      "Enter 4 for -Subsidiary/Affilate ..<br/>")
            return
        elif self.form_field == "R-O-S":
            if data == "1":
                self.company["R-O-S"] = "New Incorporation"
            elif data == "2":
                self.company["R-O-S"] = "Change of Name"
            elif data == "3":
                self.company["R-O-S"] = "Conversion"
            elif data == "4":
                self.company["R-O-S"] = "Subsidiary/Affilate"
            else:
                self.bot_response(client, "Invalid Entry")
                self.bot_response(client, "Reason for availability search ?")
                self.bot_response(client, "Enter 1 for - New Incorporation<br/>"
                                          "Enter 2 for - Change of Name<br/>"
                                          "Enter 3 for - Conversion..<br/>"
                                          "Enter 4 for -Subsidiary/Affilate ..<br/>")
                return

            self.form_field = "ID-TYPE"
            self.bot_response(client, "Select your means of Identification<br/>"
                                      "Enter 1 for - Int'l Passport <br/>"
                                      "Enter 2 for - Driver's License <br/>"
                                      "Enter 3 for - National ID card <br/>"
                                      "Enter 4 for - Age Declaration <br/>"
                                      "Enter 5 for - Birth Certificate <br/>"
                                      "Enter 6 for - Permanent Voter's Card<br/>")

            return

        elif self.form_field == "ID-TYPE":
            if data == "1":
                self.company["Id-Type"] = "Int'l Passport"
            elif data == "2":
                self.company["Id-Type"] = "Driver's License"
            elif data == "3":
                self.company["Id-Type"] = "National ID card"
            elif data == "4":
                self.company["Id-Type"] = "Age Declaration"
            elif data == "5":
                self.company["Id-Type"] = "Birth Certificate"
            elif data == "6":
                self.company["Id-Type"] = "Permanent Voter's Card"
            else:
                self.bot_response(client, "Select your means of Identification<br/>"
                                          "Enter 1 for - Int'l Passport <br/>"
                                          "Enter 2 for - Driver's License <br/>"
                                          "Enter 3 for - National ID card <br/>"
                                          "Enter 4 for - Age Declaration <br/>"
                                          "Enter 5 for - Birth Certificate <br/>"
                                          "Enter 6 for - Permanent Voter's Card<br/>")
                return

            self.id_card = self.company["Id-Type"]
            self.form_field = "ID-NO"
            self.bot_response(client, "Please Enter your " + self.id_card + "  Number")
            return

        elif self.form_field == "ID-NO":
            self.company["Id-No"] = data
            self.form_field = "PREVIEW"
            self.bot_response(client, "I guess we are done here can you confirm your details?")
            # self.bot_response(client, self.company)
            self.response = "***********************************<br/> " \
                            "<b><i>Company Details</i> </b>***************<br/>" \
                            "1* Company Proposed Name Option 1 <b> <br/>" + self.company["Company-Name"] + "</b><br/>" \
                                                                                                           "2* Company Proposed Name Option 2 " \
                                                                                                           "3* Venture Classification <b>" + \
                            self.company["Venture-Classification"] + "</b><br/>" \
                                                                     "4* Venture Type <b>" + self.company[
                                "Company-Type"] + "</b><br/>" \
                                                  "<b><i>Additional Comments </b></i> <br/>" \
                                                  "<b><i>Presenter Details</b></i> ************ <br/>" \
                                                  "5* First name <b>" + self.company["FIRST_NAME"] + "</b><br/>" \
                                                                                                     "6* Last name <b>" + \
                            self.company["LAST_NAME"] + "</b><br/>" \
                                                        "7* Telephone <b>" + self.company["PHONE-NO"] + "</b><br/>" \
                                                                                                        "8* Email <b>" + \
                            self.company["EMAIL"] + "</b><br/>" \
                                                    "9* Contact Address<b>" + self.company["Address"] + "</b><br/>" \
                                                                                                        "10* Date of Birth   <b>" + \
                            self.company["D-O-B"] + "</b><br/>" \
                                                    "11* Identification Method <b>" + self.company[
                                "Id-Type"] + "</b><br/>" \
                                             "12* ID NO   <b>" + self.company["Id-No"] + "</b><br/>" \
                                                                                         "If you would like to change any field enter the field number " \
                                                                                         "else enter 0 to submit your form "

            # print(" Got this response ", response)
            self.bot_response(client, self.response)

            return

        elif self.form_field == "PREVIEW":

            message_text = """
                        <html>
                       "<b><i>Company Details</i> </b>***************<br/>
                       Company Proposed Name Option 1 <b> <br/> {company_name} </b><br/> 
                       Company Proposed Name Option 2 
                       Venture Classification <b> {venture_classification} </b><br/> 
                       Venture Type <b>  {company_type} </b><br/>
                       <b><i>Additional Comments </b></i> <br/>
                       <b><i>Presenter Details</b></i> ************ <br/> 
                       First name <b> {first_name} </b><br/>
                       Last name <b> {last_name}</b><br/>
                       Telephone <b> {phone_no}</b><br/>
                       Email <b> {email} </b><br/> 
                       Contact Address<b> {address} </b><br/>
                       Date of Birth <b> {d_o_b} </b><br/>
                       Identification Method <b>  {id_type} </b><br/>
                       ID NO   <b>  {id_number} </b><br/>
                       </html>
                       """.format(company_name=self.company["Company-Name"]
                                  , venture_classification=self.company["Venture-Classification"]
                                  , company_type=self.company["Company-Type"]
                                  , first_name=self.company["FIRST_NAME"]
                                  , last_name=self.company["LAST_NAME"]
                                  , phone_no=self.company["PHONE-NO"]
                                  , email=self.company["EMAIL"]
                                  , address=self.company["Address"]
                                  , d_o_b=self.company["D-O-B"]
                                  , id_type=self.company["Id-Type"]
                                  , id_number=self.company["Id-No"]
                                  , subtype='html')

            self.bot_response(client, data)
            self.bot_response(client, "You Confirmed this preview. <br/>"
                                      "An e-mail has been sent to you.<br/> Kindly follow the further instructions to "
                                      "make "
                                      "payment ")
            message = MIMEText(message_text, 'html')
            message['From'] = "CORPORATE AFFAIRS COMMISSION <noreply@1gov.ng.com>"
            message['To'] = 'Mr/Mrs {first_name} {last_name} < {email} >'.format(
                first_name=self.company["FIRST_NAME"]
                , last_name=self.company["LAST_NAME"]
                , email=self.company["EMAIL"])
            message['Subject'] = 'CORPORATE AFFAIRS COMMISSION'
            msg_full = message.as_string()

            send_message(msg_full, receivers=[self.company["EMAIL"]])

            self.form_field = None
            self.process = "CHATBOT"
            return

    def handle_DRIVER_LICENSE_FORM(self, client, data):
        if self.form_field == "FIRST_NAME":
            self.driver.append(data)
            self.form_field = "LAST_NAME"
            self.bot_response(client, "Enter last name :>>> ")
            return
        elif self.form_field == "LAST_NAME":
            self.driver.append(data)
            self.form_field = "ADDRESS"
            self.bot_response(client, "Enter address :>>> ")
            return
        elif self.form_field == "ADDRESS":
            self.driver.append(data)
            self.form_field = None
            self.process = "CHATBOT"
            first_name = self.driver[0]
            last_name = self.driver[1]
            address = self.driver[2]
            response = apply_for_driver_license(first_name, last_name, address)
            response = response[0] + " <br/> \n" + response[1].strip()
            response = str(response)
            # print(" Got this response ", response)
            self.bot_response(client, response)
            return

    def check_DRIVER_LICENSE_STATUS(self, client, data):
        license_no = data
        response = check_drivers_license_status(license_no)
        self.bot_response(client, response)
        self.process = "CHATBOT"
        return


class ChatBotRouletteFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):
        super(ChatBotRouletteFactory, self).__init__(*args)
        self.clients = []

    def register(self, client):
        self.clients.append({'client-peer': client.peer, 'client': client})

    def unregister(self, client):
        for c in self.clients:
            if c['client-peer'] == client.peer: self.clients.remove(c)

    def broadcast_communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c['client'] == client:
                print("I am the client ", client)
                id = i
                break
        for c in self.clients:
            print("This are the present clients   -->", c)
            try:
                msg = '{0}'.format(payload.decode('utf-8'))
            except AttributeError:
                msg = '{0}'.format(payload)
            c['client'].sendMessage(str.encode(msg))

    def communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c['client'] == client:
                id = i
                break
        for c in self.clients:
            print("This are the present clients   -->", c)
            if c['client'] == client:
                print("Sending message to ", client)
                try:
                    msg = '{0}'.format(payload.decode('utf-8'))
                except AttributeError:
                    msg = '{0}'.format(payload)
                c['client'].sendMessage(str.encode(msg))


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    ip_add = get_pub_IP()
    print("This is IP", ip_add)

    factory = ChatBotRouletteFactory(u"ws://" + ip_add + ":3000")
    factory.protocol = ChatBotServerProtocol

    reactor.listenTCP(port, factory)
    print("ChatBot Server started on port %s" % (port,))

reactor.run()
