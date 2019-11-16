from django.core.mail import send_mail,EmailMultiAlternatives


def mail_sending(reciver_mail,task_list):
    def message(task_list):
        msglist = []
        for i in range(len(task_list)):
            msg = str((task_list[i]) + "\n")
            msglist.append(msg)
        return ("".join(msglist))
    subject = "Your pending Task in To Do List"
    from_email = "To Do App"
    to_email = [reciver_mail]
    task= message(task_list)
    message = """Welcome To the To Do App
Hey dear user some of your task is pending in To Do List.
please complete these task\n\n"""
    mail_message=message+task+"\n\n\n Thank You"
    #text_content = 'Welcome to To Do App'

    # message=EmailMultiAlternatives(subject=subject,body=text_content,from_email=from_email,to=to_email)
    # html_template=get_template('message.html').render()
    # message.attach_alternative(html_template,"text/html")
    # message.send()
    send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=mail_message,fail_silently=False)