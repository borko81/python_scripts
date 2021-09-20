# Import modues
import requests                 # Outside module, need to isntall :pip install requests !!!!!!!!!!!!!!!!
from typing import List         # Typehinting
from datetime import datetime   # Data for message
import time                     # For sleep function
import threading                # For make threading
import random                   # generate random sleep
# Use for email functionality
import smtplib

# Hard code param is here
# Email credential
# unreal
gmail_user = 'user'
gmail_password = 'password'

# List with addresses
URLS_LIST = {
    'testing': {
        'url': 'http://127.0.0.1:8000/todos/check/', 'responsibles': ['forone@abv.bg'], 'bound': 0
    },
    'productions': {
        'url': 'http://127.0.0.1:8000/prod/todos/check/', 'responsibles': ['korea60@abv.bg', 'b_stoilov@abv.bg'], 'bound': 0
    }
}


def send_email(list_with_users, server, message):
    sent_from = gmail_user
    to = list_with_users
    subject = f'Super Important Message server {server} is down'
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        # For 587 use this
        # server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo()
        # server.starttls()

        # For 465 use this
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        print('That is good, connection is ok')
        server.login(gmail_user, gmail_password)
        print('Login is good, credential is good')
        server.sendmail(sent_from, to, email_text)
        server.close()
        print('Email sent successfully!')
    except:
        print('Something went wrong...')


class GenerateData:
    """
        Generata data from URLS_LIST
    """
    bound: int = 0

    def __init__(self, check_url: str, response_people: List[str], test_site: str):
        self.check_url = check_url
        self.response_people = response_people
        self.test_site = test_site

    @property
    def show_url(self) -> str:
        """ Return site url """
        return self.check_url

    @property
    def show_response_people(self) -> List[str]:
        """ Return list with email for people responsible for site"""
        return self.response_people


class CheckSiteEnable:
    """
        After get needed data, return function wich check status for site
    """
    def __init__(self, data: GenerateData):
        self.data = data

    def message_when_site_is_down(self):
        """ Generat emessage to user """
        print(self.data.show_response_people)
        print(self.data.show_url)
        send_email(self.data.show_response_people, self.data.show_url, f'Server {self.data.show_url} looked be down')

    def check_site_is_down(self):
        """
            Check site is down or not,
            cikle spins while refused <= counter or get success result
        """
        site = ''
        counter = 0
        status = False
        while site == '' and not counter == 3:
            try:
                site = requests.get(self.data.show_url)
            except:
                print(f'Connection to site {self.data.show_url} refused for {counter + 1} time')
                time.sleep(random.randrange(2, 5))
                counter += 1
            else:
                status = site.status_code == 200
        return status

    def __repr__(self):
        return str(self.data)


def all_in_one(check: CheckSiteEnable):
    """
        Black magic, all in one,
        change status in URLS_LIST, to prevent spam user get already seen message's
    :param check: CheckSiteEnable
    :return:
    """
    result = check.check_site_is_down()
    if URLS_LIST[check.data.test_site]['bound'] == 0:
        if not result:
            URLS_LIST[check.data.test_site]['bound'] = 1
            check.message_when_site_is_down()

    elif URLS_LIST[check.data.test_site]['bound'] == 1 and result:
        URLS_LIST[check.data.test_site]['bound'] = 0


def main():
    """ Main function """
    for num, site in enumerate(URLS_LIST, start=1):
        human_read = URLS_LIST[site]
        check_url = human_read['url']
        response_people = human_read['responsibles']
        test_site = site

        data = GenerateData(check_url, response_people, test_site)
        check = CheckSiteEnable(data)
        t_num = threading.Thread(target=all_in_one, args=(check,))
        t_num.start()
        t_num.join()


if __name__ == '__main__':
    while True:
        main()
        time.sleep(random.randrange(60, 100))
