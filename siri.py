# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'siri.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import speech_recognition as sr
import random
from datetime import datetime
import smtplib, imaplib, email
import requests

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 401)
        Form.setStyleSheet("background-color: rgb(47, 47, 47);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(71, 11, 481, 71))
        font = QtGui.QFont()
        font.setFamily("URW Palladio L")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(136, 136, 136);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 320, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(136, 136, 136);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.voice_commands)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(41, 279, 461, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 280, 81, 31))
        self.pushButton_2.clicked.connect(self.text_commands)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(136, 136, 136);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(65, 129, 491, 111))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 255, 0);\n"
                                   "")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setWordWrap(True)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SIRI"))
        self.pushButton.setText(_translate("Form", "Speak Now"))
        self.pushButton_2.setText(_translate("Form", "OK"))

    def speechReco(self):
        # Record Audio
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            speech = r.recognize_google(audio)
            print("You said: " + speech)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return speech

    def random_joke(self):
        jokes = ["What did the traffic light say to the car?\nDon’t look! I’m about to change.",
                 "Why was the little strawberry crying?\nHis mom was in a jam.",
                 "What do you call a nosy pepper?\nJalapeño business.",
                 "Why are frogs are so happy?\nThey eat whatever bugs them.",
                 "How do you befriend a squirrel?\nJust act like a nut.",
                 "Have you heard about the corduroy pillow?\nNo? Really? It’s making headlines!",
                 "Why did the jaguar eat the tightrope walker?\nIt was craving a well-balanced meal.",
                 "What did the big bucket say to the smaller one?\nLookin’ a little pail there.",
                 "Why do chicken coups always have two doors?\nWith four, they’d be chicken sedans.",
                 "What did one hat say to the other?\nYou stay here. I’ll go on ahead.",
                 "Why did the lifeguard kick the elephants out of the pool?\nThey kept dropping their trunks.",
                 "What do you call a pony with a cough?\nA little hoarse.",
                 "What do you do if someone thinks an onion is the only food that can make them cry?\nThrow a coconut at their face.",
                 "What do you call a man with no arms or legs wading in a pool?\nBob.",
                 "What do cows most like to read?\nCattle-logs.",
                 "How does a duck buy lipstick?\nShe just puts it on her bill.",
                 "What do you call a guy with a rubber toe?\nRoberto.",
                 "What did the cop say to his stomach?\nStop! I’ve got you under a vest!",
                 "What do you call a snowman on a hot day?\nPuddle.",
                 "What do you do with a sick boat?\nTake it to the doc already.",
                 "What did the rubber band factory worker say when he was fired?\nOh, snap!",
                 "What do you do when you see a spaceman?\nPark your car, man.",
                 "What did one shark say to the other as he ate a clownfish?\nWell this tastes a little funny.",
                 "What do you do with epileptic lettuce?\ىMake a seizure salad.",
                 "What did the older chimney say to the younger one?\nBut you’re way too young to smoke!",
                 "Who do call when the ocean needs a little cleaning?\nA mermaid, of course.",
                 "What do you call a bee that’s having a bad hair day?\nFrisbee.",
                 "Which plant rules the garden?\nThe dande-lion.",
                 "Why did the skeleton hit the party solo?\nHe had no body to go with him.",
                 "What does the cobbler say when a cat wanders into his shop?\nShoe!",
                 "Why was the poor guy selling yeast?\nTo raise some dough.",
                 "What’s a firefly’s favorite game?\nHide-and-glow-seek.",
                 "Who does a pharaoh talk to when he’s sad?\nHis mummy, of course.",
                 "What do you call a pooch living in Alaska?\nA chilly dog.",
                 "Why was the sand wet?\nBecause the sea weed.",
                 "How much does a pirate pay for corn?\nA buccaneer.",
                 "Did you hear about that wedding?\nIt was in-tents.",
                 "How did Darth Vader know what Luke got him for Christmas?\nHe could feel his presents.",
                 "What do baby kangaroos wear when it’s cold out?\nJumpsuits.",
                 "What kind of music to chiropractors listen to?\nMostly hip-pop.",
                 "What’s the most famous creature in the ocean?\nThe starfish.",
                 "I just wrote a book on reverse psychology.\nDo not read it!",
                 "What do ants get when they do all their chores?\nAn allow-ants.",
                 "Why don’t skeletons watch scary movies?\nThey just don’t have the guts.",
                 "What did one egg say to the other?\nEggs-cuse me, please.",
                 "What’s so bad about Russian dolls?\nThey’re all so full of themselves.",
                 "Why doesn’t anyone want to shave a crazy sheep?\nCause it’s a baaaaaaaaaad idea.",
                 "What do clouds wear under their shorts?\nThunderpants.",
                 "What does a farmer say after feeding a stick of dynamite to his steer?\nAbominable! [A-bomb-in-a-bull}",
                 "Why wouldn’t the shrimp share his treasure?\nBecause he was a little shellfish. "
                 ]
        return random.choice(jokes)

    def random_fact(self):
        facts = [
            "Space smells like a combination of diesel fuel and barbecue, according to astronauts. The smell is caused by dying stars.",
            "Rapunzel, Rapunzel!\nA single strand of hair can hold up to 3 ounces of weight.\nThat means the typical person’s full head of hair can support up to 12 tons.",
            "Cornell University scientists have created a functioning guitar the size of a human blood cell.",
            "Many oranges are green when they’re ripe. Scientists remove their chlorophyll to make them more appealing to North American consumers.",
            "The average person walks the equivalent of 5 laps around the world during their lifetime.",
            "The chills you get when listening to music are caused by your brain releasing dopamine, a neurotransmitter that causes pleasure.",
            "Women constitute 70 percent of Iranian university science and engineering students",
            "A British research study found that watching a horror film prior to viewing abstract art enhances the enjoyment of the art for most people.",
            "In 2005, an Australian research institute published a study on the loss of teaspoons in the workplace.",
            "The average bolt of lightning contains enough energy to toast 100,000 pieces of bread.",
            "The scientific name for brain freeze is sphenopalatine ganglioneuralgia.",
            "Researchers from Heidelberg University Hospital have determined it takes 6 minutes for alcohol to impact human brain cells.",
            "In 1992, 29,000 rubber ducks were lost at sea, and they are still being discovered in unexpected places.",
            "Globally, only 2 percent of the population has green eyes.",
            "Great Britain briefly had a Cones Hotline in the early 1990s. It was a special number citizens could call if they saw traffic cones on the road for no reason. It was disbanded after three years because almost no one ever called it.",
            "A New Jersey man flunked out of law school and subsequently sued the school for having accepted him in the first place.",
            "The Waldorf Astoria hotel once had its own private railroad track at Grand Central so that its guests could clandestinely enter and exit New York City. Largely abandoned now, it operates only when the president is in town, if the need arises for an emergency exit.",
            "New York City’s oldest house is a cottage in Queens near LaGuardia Airport. It was built in 1654 by the Rikers family (the same family that gave Rikers Island its name) and even has a family cemetery in the backyard.",
            "The top speed of the first American car race in 1895 for 7 mph.",
            "The first African-American to win the Nobel Peace Prize was Ralph Bunche, who won in 1950 for his meditation work in Israel. He was also involved in the formation of the United Nations.",
            "Barbed wire was invented in 1845 and was largely responsible for putting cowboys out of business since it provided cheap and easy fencing.",
            "The first U.S. town to be completely lit by electric streetlights was Wabash, Indiana, in 1880. It had a population of 320 at the time.",
            "Ocean liner stewardess Violet Jessop was on board during the three largest ship sinkings in history: the Titanic, the Britannic, and the Olympic.",
            "The first written instance of “OMG” that we know of was in a letter to Winston Churchill in 1917.",
            "Charles Dickens had bookbinders print up a number of fake books for his library. Titles included Drowsy’s Recollections of Nothing (3 volumes), Hansard’s Guide to Refreshing Sleep (as many volumes as possible), and Bowwowdom: A Poem. ",
            "There’s music made especially for cats. Apparently cats develop their musical taste soon after they’re born, so cat music includes not only traditional (human-made) instruments, but also feeding noises, bird chirps and purring noises.",
            "The designer of the Eiffel Tower built an apartment in the tower itself. Though he didn’t live there, he did use it to entertain distinguished guests and scientists.",
            "Pablo Picasso carried a revolver loaded with blanks, which he would fire at whoever asked him what his work “meant.”",
            "In 2011, a woman paid $10,000 for a “non-visible” work of art from actor James Franco’s Museum of Non-Visible Art.",
            "Ernest Wright’s 1939 novel Gadsby does not contain the letter “e.”",
            "There are over 1,000 adaptations of Shakespeare’s works.",
            "Toni Morrison was the first African-American woman to receive a Nobel Prize. It was in recognition of her contributions to literature and poetry.",
            "British artist Willard Wigan creates micro sculptures, you need a microscope to see them. His work often sits in the eye of a sewing needle or on the head of a pin. He got his start at 5 years old making a house for ants because he thought they needed a place to live.",
            "Artist Ivan Albright was so meticulous, he often worked with a single-haired brush and would spend whole days working on 1 square inch of canvas.",
            "The only word that rhymes with “purple” is “hirple,” which means “to limp awkwardly.” Nothing rhymes with “woman.”",
            "In 2012, the Smithsonian officially recognized video games as an art form and had an exhibit to “comprehensively examine the evolution of video games as an artistic medium.”",
            "Bananas are more effective in replenishing electrolytes than Gatorade. They also have serotonin and dopamine—chemicals that help you feel happy.",
            "An 8-week meditation course will cause the amygdala, associated with fear and other emotions, to shrink while the prefrontal cortex, associated with awareness, concentration and decision-making, will thicken.",
            "Phobophobia is the fear of having a phobia. Symptoms include dizziness, excessive sweating, increased heart rate, and faintness.",
            "Every time you lick a USPS stamp, you ingest about 10 percent of a calorie. British stamps, however, contain about 5.9 calories. Israeli stamps are kosher.",
            "Honey is a better cough suppressant than over-the-counter cough suppressants.",
            "Simply taking 1 step uses over 200 muscles in the body.",
            "Laughing boosts the immune system, burns calories and reduces stress hormones, making it a very healthy activity.",
            "Green tea contains catechins, which have been shown to stabilize blood sugar levels and curb appetite.",
            "Sarcasm makes you more creative.",
            "American 18- to 34-year-olds spend 25.7 hours on Facebook, 7 hours on Instagram, 5.9 hours on Snapchat, 5.7 hours on Tumblr and 3.5 hours on Twitter each month.",
            "People are more likely to agree with a statement written in Baskerville than any other font.",
            "Scientists found that the most relaxing song ever is “Weightless” by the Marconi Union—it reduced anxiety by 65 percent in the average test subject.",
            "The average person will spend a total of 3,680 hours, or 153 days searching for misplaced items. Keys, cellphones, sunglasses and paperwork top the list of commonly lost items",
            "Google processed 11.382 billion searches in September 2015.",
            "56 percent of internet users have googled themselves.",
            "Parents have started naming their children after Instagram filters. The most popular filter name was Lux, but there were even a few Kelvins.",
            "Talking to yourself makes your brain work more efficiently.",
            "At age 23, Evan Spiegel, the founder of Snapchat, is the world’s youngest billionaire.",
            "3 out of 4 Americans use an emoji in text messaging every single day.",
            "The world’s oldest socks were in fact designed to be worn with sandals. Made in Egypt sometime in the fourth or fifth century, the wool socks have two toes."
        ]
        return random.choice(facts)

    def get_date(self):
        curr_time = datetime.today().strftime('%Y-%m-%d-%H-%M')
        time = curr_time.split('-')
        months = {'01': 'January',
                  '02': 'February',
                  '03': 'March',
                  '04': 'April',
                  '05': 'May',
                  '06': 'June',
                  '07': 'July',
                  '08': 'August',
                  '09': 'September',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December'}

        today = "Today is " + months[time[1]] + "," + time[2] + "," + time[0]
        current_time = "It is " + time[3] + " and " + time[4] + " minutes"
        return [today, current_time]

    GMAIL_USERNAME = "enter your mail here "
    GMAIL_PASSWORD = "enter your password here"

    def check_mail(self):
        GMAIL_USERNAME = self.GMAIL_USERNAME
        GMAIL_PASSWORD = self.GMAIL_PASSWORD
        conn = imaplib.IMAP4_SSL('imap.gmail.com')
        conn.login(GMAIL_USERNAME, GMAIL_PASSWORD)
        conn.select('Inbox')
        typ, data = conn.search(None, 'UNSEEN')
        unread_msgs = "You got " + str(len(data[0].split())) + " unread messages."

        for msgId in data[0].split():
            typ, messageParts = conn.fetch(msgId, '(RFC822)')
            emailBody = messageParts[0][1]
            mail = email.message_from_bytes(emailBody)
            print(mail['From'])
            # if "noobcakes333@gmail.com" in mail['From']:
            #    to = mail['From']
            #    parts = [part.as_string() for part in mail.walk()]
            #    msg = parts[-2].strip('Content-Type: text/plain; charset="UTF-8"\n\n')
            #    print(msg)
        conn.close()
        return unread_msgs

    def get_weather(self, city):
        query = "q=" + city
        res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
        result = res.json()
        temp = "{}'s temperature: {}°C ".format(city, result['main']['temp'])
        wind = "Wind speed: {} m/s".format(result['wind']['speed'])
        descrpition = "Description: {}".format(result['weather'][0]['description'])
        weather = "Weather: {}".format(result['weather'][0]['main'])
        return temp+"\n"+wind+"\n"+descrpition+"\n"+weather

    def voice_commands(self):
        speech = self.speechReco()
        if speech:
            if "joke" in speech:
                joke = self.random_joke()
                self.label_2.setText(joke)

            elif "fact" in speech:
                fact = self.random_fact()
                self.label_2.setText(fact)

            elif "date" in speech:
                date = self.get_date()[0]
                self.label_2.setText(date)

            elif "time" in speech:
                time = self.get_date()[1]
                self.label_2.setText(time)

            elif "mail" in speech:
                msgs = self.check_mail()
                self.label_2.setText(msgs)

            elif "weather" in speech:
                weather = self.get_weather("USA")
                self.label_2.setText(weather)

            else:
                print("[Invalid] " + speech)

    def text_commands(self):
        text = self.textEdit.toPlainText()
        if "joke" in text:
            joke = self.random_joke()
            self.label_2.setText(joke)

        elif "fact" in text:
            fact = self.random_fact()
            self.label_2.setText(fact)

        elif "date" in text:
            self.label_2.setText(self.get_date()[0])

        elif "time" in text:
            self.label_2.setText(self.get_date()[1])

        elif "mail" in text:
            msgs = self.check_mail()
            self.label_2.setText(msgs)

        elif "weather" in text:
            weather = self.get_weather("USA")
            self.label_2.setText(weather)

        else:
            print("[Invalid] " + text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
