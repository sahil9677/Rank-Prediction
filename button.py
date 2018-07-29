import sys
import csv
import time
import os
from collections import Counter

from PyQt5 import QtCore, QtGui, QtWidgets
from test1gui import Ui_Form
from test3gui import Ui_Form1
from test2gui import Ui_Form2
from test4gui import Ui_Form3
from test5gui import Ui_Form4
from test6gui import Ui_Form5
from test7gui import Ui_Form6
from test8gui import Ui_Form7
from PyQt5.QtGui import QDoubleValidator

class Seventh(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Seventh, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form7()
        self.ui.setupUi(self)
        self.ui.Button11.clicked.connect(self.OnPageSuggest)
        self.ui.Button12.clicked.connect(self.OpenWindow9)
        self.ui.Button13.clicked.connect(QtWidgets.QApplication.instance().quit)
    def OnPageSuggest(self):
        if query['Keyword Optimization'] == 'Medium':
            self.ui.textEdit.setPlainText('You have an average Keyword Optimization. You need to take care about Keyword Placement and Spacing in your articles also start using Primary Keywords in slug, title, meta, and sub-headings')
        elif query['Keyword Optimization'] == 'Low':
            self.ui.textEdit.setPlainText('You have an average Keyword Optimization. You need to take care about Keyword Placement and Spacing in your articles also start using Primary Keywords in slug, title, meta, and sub-headings')
        elif query['Keyword Optimization'] == 'High':
            self.ui.textEdit.setPlainText('You have an good Keyword Optimization.')
        if query['Internal Linking'] == 'Medium':
            self.ui.textEdit_2.setPlainText('You have average Internal Linking. You should start giving Related articles in your content by using Also Read Tags. You should also use anchor tect to interlink your own articles')
        elif query['Internal Linking'] == 'Low':
            self.ui.textEdit_2.setPlainText('You have poor Internal Linking. You should start giving Related articles in your content by using Also Read Tags. You should also use anchor tect to interlink your own articles')
        elif query['Internal Linking'] == 'High':
            self.ui.textEdit_2.setPlainText('You have good Internal Linking.')
        self.ui.textEdit_3.setPlainText('Word Count depends on the type of content you write. But if you have unique and more content compared to your competitors, you get an edge over them. So Wherever possible try to extend the word count over 600+ provided you have that much unique content')
        self.ui.textEdit_3.setPlainText('Grammar Language and Plagiarism refers to the Quality of Content. Without a doubt if you keep copying content word to word from different sources google will put your website into the spam list. Also it is better to give a link back to the source from where you got the content. Lastly it goes without saying that Grammar and Language affect readability and will Lower the User Rating of your website.')
        self.ui.textEdit_3.setPlainText('A well categorized content helps google to create a sitemap of your website which inturn leads to fast indexing of your articles')
    def OpenWindow9(self):
        self.open = First(self)
        column.clear()
        freq.clear()
        Probability.clear()
        occurance_counts.clear()
        conditionaloccurance.clear()
        condProb.clear()
        FinalResults.clear()
        query.clear()
        f.seek(0)
        self.close()
        self.open.show()

class Sixth(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Sixth, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form6()
        self.ui.setupUi(self)
        self.ui.Button9.clicked.connect(self.TrendSuggest)
        self.ui.Button10.clicked.connect(self.OpenWindow8)
        self.dialog = Seventh(self)
    def TrendSuggest(self):
        self.ui.textEdit.setPlainText('The most important thing is to analyze the trend and select topics for which you can rank.Here are a few suggestions which will help you in the process of topic selection.' '/n' '1. Tools:' '/n' 'To select Topics, the most helpful tool is Google Trends. https://ahrefs.com/blog/how-to-use-google-trends-for-keyword-research/. Another tool by google is Keyword Planner. Also for competitor research, you can use  similarweb.com, ahrefs.com, semrush.com, etc.' '/n' '2.Gap Analysis:' '/n' 'Gap Analysis is another technique used for finding the exact topic for which your website can perform well in terms of ranking and traffic from the vast pool of trending topics. You can get the information on gap analysis over here https://www.businessesgrow.com/2018/01/10/content-gap-analysis/')
    def OpenWindow8(self):
        self.close()
        self.dialog.show()

class Fifth(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Fifth, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form5()
        self.ui.setupUi(self)
        self.ui.Button7.clicked.connect(self.TechSuggest)
        self.ui.Button8.clicked.connect(self.OpenWindow7)
        self.dialog = Sixth(self)
    def OpenWindow7(self):
        self.close()
        self.dialog.show()
    def TechSuggest(self):
        if query['Domain Authority'] == 'Low':
            self.ui.textEdit.setPlainText('You have a very Low Domain Authority. Inorder to Improve your Domain Authority, you can visit https://seopressor.com/blog/how-to-increase-domain-authority/')
        elif query['Domain Authority'] == 'Medium':
            self.ui.textEdit.setPlainText('Your Domain Authority is average. Inorder to Improve your Domain Authority, you can visit https://seopressor.com/blog/how-to-increase-domain-authority/')
        elif query['Domain Authority'] == 'High':
            self.ui.textEdit.setPlainText('You have a good Domain Authority.')
        if query['SSL Certificate'] == 'No':
            self.ui.textEdit_2.setPlainText('You do not have a secure website. Google gives an edge to websites which are certified to be secure. You can purchase an SSL certificate at https://in.godaddy.com/help/request-an-ssl-certificate-562')
        if query['Schema Implementation'] == 'No':
            self.ui.textEdit_3.setPlainText('Your website doesnt have a proper schema.It becomes easier for the search engine to index your articles if you have implemented schema.Implementation of schema is done according to the guidelines of schema.org')
        if query['AMP implementation'] == 'No':
            self.ui.textEdit_4.setPlainText('Your website does not have an AMP version. The Accelerated Mobile Pages Project (AMP) is an open-source website publishing technology designed to improve the performance of web content and advertisements. It is necessary to create an AMP version of your website to improve your rankings on Mobile devices.')
        if query['Static Pages'] == 'No':
            self.ui.textEdit_5.setPlainText('You need to provide basic information about your company via static pages such as About us,   Contact us etc. Also it is necessary to provide information about your privacy policy, DMCA and Terms of Use for legality issues. Google considers websites without this information as Unauthentic.')
        if query['Mobile Optimization'] == 'No':
            self.ui.textEdit_6.setPlainText('Google updated its algorithm to provide mobile first searching. It is extremely necessary that your website is mobile optimized if you want to rank on mobile devices.')
        if query['SSL Certificate'] == 'Yes':
            self.ui.textEdit_2.setPlainText(
                'You have a secure website. Google gives an edge to websites which are certified to be secure. You can purchase an SSL certificate at https://in.godaddy.com/help/request-an-ssl-certificate-562')
        if query['Schema Implementation'] == 'Yes':
            self.ui.textEdit_3.setPlainText(
                'Your website has a proper schema.It becomes easier for the search engine to index your articles if you have implemented schema.Implementation of schema is done according to the guidelines of schema.org')
        if query['AMP implementation'] == 'Yes':
            self.ui.textEdit_4.setPlainText('Your website has an AMP version. The Accelerated Mobile Pages Project (AMP) is an open-source website publishing technology designed to improve the performance of web content and advertisements. It is necessary to create an AMP version of your website to improve your rankings on Mobile devices.')
        if query['Static Pages'] == 'Yes':
            self.ui.textEdit_5.setPlainText('You have provided basic information about your company via static pages such as About us,   Contact us etc. Also it is necessary to provide information about your privacy policy, DMCA and Terms of Use for legality issues. Google considers websites without this information as Unauthentic.')
        if query['Mobile Optimization'] == 'Yes':
            self.ui.textEdit_6.setPlainText('Google updated its algorithm to provide mobile first searching. It is extremely necessary that your website is mobile optimized if you want to rank on mobile devices.')
        if query['Alexa'] == 'Medium':
            self.ui.textEdit_7.setPlainText('A Low Alexa rank means you have Low traffic numbers compared to other websites in your niche. You can visit this website for further details on improving alexa https://blog.alexa.com/improving-your-alexa-rank/')
        elif query['Alexa'] == 'Low':
            self.ui.textEdit_7.setPlainText('You have an average Alexa rank means you have Low traffic numbers compared to other websites in your niche. You can visit this website for further details on improving alexa https://blog.alexa.com/improving-your-alexa-rank/')
        elif query['Alexa'] == 'High':
            self.ui.textEdit_7.setPlainText('Your have a great Alexa rank. No improvements required for that')
        if query['Content Update Frequency'] == 'High':
            self.ui.textEdit_9.setPlainText('Regular content updation helps to improve idexing speed. You have a great frequency.')
        elif query['Content Update Frequency'] == 'Low':
            self.ui.textEdit_9.setPlainText('Regular content updation helps to improve idexing speed. You need to improve the rate at which you post articles.')
        elif query['Content Update Frequency'] == 'Medium':
            self.ui.textEdit_9.setPlainText('Regular content updation helps to improve idexing speed. You need to improve the rate at which you post articles')
        if query['Interface'] == 'High':
            self.ui.textEdit_10.setPlainText('Google aims at giving the users what they want. The Interface and user Experience are one of the major factors that affect the Website Ratings by users which directly affect your rankings. According to your inputs you have a good interface so no need to worry about that.')
        elif query['Interface'] == 'Low':
            self.ui.textEdit_10.setPlainText('Google aims at giving the users what they want. The Interface and user Experience are one of the major factors that affect the Website Ratings by users which directly affect your rankings. According to your inputs you have a poor interface so you need to improve a lot.')
        elif query['Interface'] == 'Medium':
            self.ui.textEdit_10.setPlainText('Google aims at giving the users what they want. The Interface and user Experience are one of the major factors that affect the Website Ratings by users which directly affect your rankings. According to your inputs you have an average interface so you need to work on it.')
        if query['User Experience'] == 'Medium':
            self.ui.textEdit_11.setPlainText('According to your inputs you have an average User Experience so you need to work on it.')
        elif query['User Experience'] == 'Low':
            self.ui.textEdit_11.setPlainText(
                'According to your inputs you have a poor User Experience so you need to improve a lot.')
        elif query['User Experience'] == 'High':
            self.ui.textEdit_11.setPlainText('According to your inputs you have a User Experience so no need to worry about that.')
        if query['Ad optimization'] == 'Medium':
            self.ui.textEdit_8.setPlainText('Ad Optimzation refers to the number and placement of ads on your webpage. Ad crowding is not too user friendly and hence is a factor based on which google evaluates the website usability which affects the rank. According to your input you have an average Ad optimization. You should visit the folLowing link to get more insights on ad optimization http://monetizepros.com/ad-serving-and-optimization/guide-to-ad-serving-optimization/')
        elif query['Ad optimization'] == 'Low':
            self.ui.textEdit_8.setPlainText('Ad Optimzation refers to the number and placement of ads on your webpage. Ad crowding is not too user friendly and hence is a factor based on which google evaluates the website usability which affects the rank. According to your input you have a poor Ad optimization. You should visit the folLowing link to get more insights on ad optimization http://monetizepros.com/ad-serving-and-optimization/guide-to-ad-serving-optimization/')
        elif query['Ad optimization'] == 'High':
            self.ui.textEdit_8.setPlainText('Ad Optimzation refers to the number and placement of ads on your webpage. Ad crowding is not too user friendly and hence is a factor based on which google evaluates the website usability which affects the rank. According to your input you have an very good Ad optimization. You should try to improve the conversion rate (Click Through Rate) through heat map studies.')

class Fourth(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Fourth, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form4()
        self.ui.setupUi(self)
        self.ui.Button6.clicked.connect(self.OpenWindow6)
        self.ui.pushButton.clicked.connect(QtWidgets.QApplication.instance().quit)
        self.ui.Button5.clicked.connect(self.OpenWindow5)
        self.dialog = Fifth(self)
    def OpenWindow5(self):
        self.open = First(self)
        column.clear()
        freq.clear()
        Probability.clear()
        occurance_counts.clear()
        conditionaloccurance.clear()
        condProb.clear()
        FinalResults.clear()
        query.clear()
        f.seek(0)
        self.close()
        self.open.show()
    def OpenWindow6(self):
        self.close()
        self.dialog.show()

class Third(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Third, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form3()
        self.ui.setupUi(self)
        self.ui.Button3.clicked.connect(self.prediction)
        self.ui.Button4.clicked.connect(self.OpenWindow4)
        self.dialog = Fourth(self)

    def OpenWindow4(self):
        self.close()
        self.dialog.show()

    def prediction(self):
        Init_total = 1.0
        query['Rank Prediction'] = '?'
        e = int(self.ui.KOpt.text())
        if 3 < e < 8:
            query['Keyword Optimization'] = 'Medium'
        elif e < 4:
            query['Keyword Optimization'] = 'Low'
        elif e > 7:
            query['Keyword Optimization'] = 'High'
        f = int(self.ui.Link.text())
        if 3 < f < 8:
            query['Internal Linking'] = 'Medium'
        elif f < 4:
            query['Internal Linking'] = 'Low'
        elif f > 7:
            query['Internal Linking'] = 'High'
        g = int(self.ui.wordcount.text())
        if 300 < g < 500:
            query['Word Count'] = 'Medium'
        elif g < 301:
            query['Word Count'] = 'Low'
        elif g > 500:
            query['Word Count'] = 'High'
        h = int(self.ui.grammar.text())
        if 3 < h < 8:
            query['Grammar and Language'] = 'Medium'
        elif h > 7:
            query['Grammar and Language'] = 'High'
        elif h < 4:
            query['Grammar and Language'] = 'Low'
        k = int(self.ui.Categ.text())
        if 3 < k < 8:
            query['Categorization'] = 'Medium'
        elif k < 4:
            query['Categorization'] = 'Low'
        elif k > 7:
            query['Categorization'] = 'High'

        def condProbfun(queryattribute_val, classlabel):
            value = 0.0
            counter = 0.0
            occure = 0.0
            result = 0.0
            f = open('datastr.csv', 'r')
            reader = csv.reader(f)
            for row in reader:
                if queryattribute_val in row and classlabel in row:
                    value = value + 1
            occure = occurance_counts[classlabel]
            result = value / occure
            return result

        for h in headers:
            column[h] = []
        for row in reader:
            for h, v in zip(headers, row):
                column[h].append(v)

        for h in headers:
            word_list = column[h]
            # Get a set of unique words from the list
            word_set = set(word_list)
            # create frequency dictionary

            for word in word_set:
                occurance_counts[word] = word_list.count(word)  # Get occurance count
                freq[word] = word_list.count(word) / float(len(word_list))  # Get frequency count
                Probability[word] = freq[word]  # prior probability
        # -----------------------------------------------
        for name, item in query.items():  # which class
            if item == '?':
                classname = name
        # -----------------------------------------------
        word_list = column[classname]
        word_set = set(word_list)

        for word in word_set:
            classlabel = word  # {Consultancy,Service,Research}
            total = Init_total
            for queryattribute in query:
                if not queryattribute == classname:d
                    queryattribute_val = query[queryattribute]
                    # Get Every other attribute than classlabel print query[queryattribute]
                    ans = condProbfun(queryattribute_val, classlabel)
                    print('\n conditional probability  P(',queryattribute_val ,'|',classlabel,')=',ans)
                    total = total * ans
                    condProb[classlabel] = total
            # print 'Total', total

            TotalProbability = total * freq[classlabel]
            FinalResults[classlabel] = TotalProbability
        list = FinalResults.values()
        # -----------------------------------------------
        # Predict Classname
        maxprob = max(list)
        for name, item in FinalResults.items():
            if item == maxprob:
                classpredicted = name
                self.ui.textEdit.setPlainText(classpredicted)


class Second(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form2()
        self.ui.setupUi(self)
        self.ui.Button2.clicked.connect(self.OpenWindow3)
        self.dialog = Third(self)

    def OpenWindow3(self):
        query['Wikipedia page'] = self.ui.Wikipedia.text()
        d = int(self.ui.Trend.text())
        if 3 < d < 8:
            query['Trend level'] = 'Medium'
        elif d < 4:
            query['Trend level'] = 'Low'
        elif d > 7:
            query['Trend level'] = 'High'
        self.close()
        self.dialog.show()

class First(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form1()
        self.ui.setupUi(self)
        self.ui.Button1.clicked.connect(self.OpenWindow2)
        self.dialog = Second(self)

    def OpenWindow2(self):
        number = int(self.ui.DA.text())
        if number <= 30:
            query['Domain Authority'] = 'Low'
        elif 30 < number < 61:
            query['Domain Authority'] = 'Medium'
        elif number > 60:
            query['Domain Authority'] = 'High'
        query['SSL Certificate'] = self.ui.SSL.text()
        query['Schema Implementation'] = self.ui.Schema.text()
        query['AMP implementation'] = self.ui.AMP.text()
        query['Static Pages'] = self.ui.Static.text()
        query['Mobile Optimization'] = self.ui.Mobile.text()
        num = int(self.ui.Alexa.text())
        if 10000 < num < 100001:
            query['Alexa'] = 'Medium'
        elif num > 100000:
            query['Alexa'] = 'Low'
        elif num < 10000:
            query['Alexa'] = 'High'
        val = int(self.ui.Frequency.text())
        if val > 140:
            query['Content Update Frequency'] = 'High'
        elif val <= 30:
            query['Content Update Frequency'] = 'Low'
        elif 30 < val < 141:
            query['Content Update Frequency'] = 'Medium'
        a = int(self.ui.Interface.text())
        if a > 7:
            query['Interface'] = 'High'
        elif a < 4:
            query['Interface'] = 'Low'
        elif 3 < a < 8:
            query['Interface'] = 'Medium'
        b = int(self.ui.Exp.text())
        if 3 < b < 8:
            query['User Experience'] = 'Medium'
        elif b < 4:
            query['User Experience'] = 'Low'
        elif b > 7:
            query['User Experience'] = 'High'
        c = int(self.ui.Ad.text())
        if 3 < c < 8:
            query['Ad optimization'] = 'Medium'
        elif c < 4:
            query['Ad optimization'] = 'Low'
        elif c > 7:
            query['Ad optimization'] = 'High'
        self.close()
        self.dialog.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.OpenWindow1)
        self.dialog = First(self)
    def OpenWindow1(self):
        self.close()
        self.dialog.show()


file = 'datastr.csv'
f = open(file, "rt")
reader = csv.reader(f)
headers = next(reader)
column = {}
freq = {}
Probability = {}
occurance_counts = {}
conditionaloccurance = {}
condProb = {}
FinalResults = {}
query = {}

def main():
    app = QtWidgets.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    app.exec_()

if __name__ == '__main__':
    main()


