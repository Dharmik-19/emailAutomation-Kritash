import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

conn = smtplib.SMTP('smtp.gmail.com', 25)
conn.ehlo()
conn.starttls()

email = input('Enter your Email Id: ')
password = input('Enter your Email-ids password: ')

conn.login(email, password)

name = input("Please enter your name: ")
designation = input("Please enter your designmation in outreach team: ")
phno = int(input("Please enter your phone number: "))

filename = input("Enter the absolute file path of attachment: ")

X = name

recipients = input("Enter E-mail IDs of recipients (space seperated): ")

text1 = '''Dear Sir/Ma’am,
	            \tGreeting for the day, Hope you are having a great time amidst these unprecedented times of COVID-19. On behalf of Kritash, The social welfare body of IIT Jammu; I am ''' + X + ''', ''' + designation + ''' of the outreach division of Kritash.

	            \tWe are a team of enthusiastic students with an aim in mind to work towards the welfare of society, so we conduct various workshops and events. We have established a subdivision named Aksharshala under which we educate the unprivileged and needy students round the clock. We also run plantation events in our college and even in local areas such as Jagti, Jammu. Our events team enthusiastically organises events which in turn helps hundreds of people. We run a blog site on WordPress, educating hundreds of people.

	            \tWe love to see smiles on children and needy people’s faces, that’s what drives and motivates us to work towards social welfare. So as you might have anticipated, we share mutual interests; we aspire to have an opportunity to contribute with you and work as a team for social welfare. As you and your team are citizens of Jammu & Kashmir so you have the experience of the difficulties and we think that information will be helpful for us to proceed further.  So I, on behalf of Kritash, present our willingness to collaborate with you. 

	            \tThank you very much for your time and consideration. We are looking forward to hearing from you and wishing you a great day ahead. Please visit our website to know more about us:  https://kritashiitjammu.org/

Yours sincerely,\n'''
text2 = '''\n'''
text3 = ''', Outreach Team, Kritash
M: +91 '''
text4 = '''| W: https://kritashiitjammu.org/'''

message = u''.join((text1, name, text2, designation, text3, str(phno), text4)).encode('utf-8')

sender = email
receiver = recipients.split(' ')

sseq = 0;

print("\n\n***Process Initiated***\n")

for i in receiver:
    print("Processing email number", sseq + 1, "of ", len(receiver))
    sseq += 1

    Epaper = MIMEMultipart()
    Epaper['From'] = name + ' <' + email + '>'
    Epaper['To'] = i
    Epaper['CC'] = 'Kritash IIT Jammu <kritash@iitjammu.ac.in>, Head Outreach Kritash <dharmik.kritash@gmail.com>'
    Epaper['Subject'] = 'Greetings from Kritash, the social welfare body of IIT Jammu'

    Epaper.attach(MIMEText(message.decode(), 'plain'))

    fo = open(filename, 'rb')
    attachment = "Kritash.pdf"
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((fo).read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attachment)
    Epaper.attach(payload)

    text = Epaper.as_string()

    recipent = [i] + ['kritash@iitjammu.ac.in', 'dharmik.kritash@gmail.com']

    conn.sendmail(sender, recipent, text)

    print("Email sent to", i + "\n")

print("***Process Terminated***")
conn.quit()



