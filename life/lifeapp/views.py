from django.shortcuts import render
import smtplib
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
# Create your views here.
def life(request):
    if request.method =='POST':
        print('hai')
        context={}
        html_data=""
        Name=""
        PhoneNum=""
        Day=""
        Time=""
        CoachNum=""
        cut_name=request.POST['name']
        phoneNum=request.POST['phone_num']
        # day = request.POST['day']
        # time = request.POST['time']
        coachNum = request.POST['coach_name']
        meetingtime = request.POST['meetingdate']
        print(meetingtime)
        # message = request.POST['message']
        emails = ['rajitha.alluri003@gmail.com']
        # send_mail('otp', 'hello', 'rajitha.alluri003@gmail.com',emails )

        html_data+="<html>" \
                   "<head>" \
                   "<body>" \
                    "<table border="+str(1)+">"\
                    "<tr>" \
                    "<td>" +cut_name+ "</td>" \
                     "<td>" + phoneNum + "</td>" \
                    "<td>" + coachNum + "</td>" \
                    "<td>" + meetingtime + "</td>" \
                    "</tr>"\
                    "</table>"\
                   "</body>" \
                   "</head>" \
                   "</html>"

        # mail_content = '''Hello,
        # This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
        # Thank You
        # '''
        # html = """\
        # <html>
        #   <head></head>
        #   <body>
        #   <table>
        #   <tr>
        #   <td>
        #   Rajitha
        #   </td>
        #   <td>
        #   9100525605
        #   </td>
        #   </tr>
        #   </table>
        #     <p>Hi!<br>
        #        How are you?<br>
        #        Here is the <a href="http://www.python.org">link</a> you wanted.
        #     </p>
        #   </body>
        # </html>
        # """
        # The mail addresses and password
        sender_address = 'rajithaalluri7@gmail.com'
        sender_pass = 'python@2021'
        receiver_address = 'rajithaalluri7@gmail.com'
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A test mail sent by Python. It has an attachment.'  # The subject line
        # The body and the attachments for the mail
        # message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(html_data, 'html'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    return render(request, 'index.html')