import smtpd
from datetime import datetime
import logging

class FakeSMTPServer(smtpd.SMTPServer):
    __outputdir__ = "./receivedemails/"

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        email_filename = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
        try:
            f = open(f'{self.__outputdir__}common.log', "a")
            f.write(f'{email_filename},{mailfrom},{rcpttos}\n')
            f.close()
            f = open(f'{self.__outputdir__}{email_filename}.txt', "w")
            f.write(f'Peer From: {peer}\n')
            f.write(f'Mail From: {mailfrom}\n')
            f.write(f'To: {rcpttos}\n')
            f.write(f'Content:\n{data}\n')
            f.close()
            logging.info(f'Email received and stored to {email_filename}')
            f = open(f'{self.__outputdir__}{email_filename}.eml', "wb")
            f.write(data)
            f.close()
        except Exception as e:
            logging.error(f'Email received {email_filename} + {e}')
        return

    def setoutputdir(self, outputdir):
        self.__outputdir__ = outputdir


