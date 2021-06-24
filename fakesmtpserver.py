import smtpd
from datetime import datetime
import codecs
import logging


class FakeSMTPServer(smtpd.SMTPServer):
    __outputdir__ = "./receivedemails/"

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        email_filename = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
        try:
            # insert row to common.log
            f = open(f'{self.__outputdir__}common.log', "a")
            f.write(f'{email_filename},{mailfrom},{rcpttos}\n')
            f.close()
            # storing message as text
            # f = open(f'{self.__outputdir__}{email_filename}.txt', "w")
            # f.write(f'Peer From: {peer}\n')
            # f.write(f'Mail From: {mailfrom}\n')
            # f.write(f'To: {rcpttos}\n')
            # str = data.decode()
            # f.write(f'Content:\n{str}\n')
            # f.close()
            with codecs.open(f'{self.__outputdir__}{email_filename}.txt', "w", "utf-8") as temp:
                temp.write(f'Peer From: {peer}\n')
                temp.write(f'Mail From: {mailfrom}\n')
                temp.write(f'To: {rcpttos}\n')
                str = data.decode("utf-8")
                temp.write(f'Content:\n')
                temp.write(f'{str}\n')
                temp.close()
            # message as eml
            logging.info(f'Email received and stored to {email_filename}')
            f = open(f'{self.__outputdir__}{email_filename}.eml', "wb")
            f.write(data)
            f.close()
        except Exception as e:
            logging.error(f'Email received {email_filename} + {e}')
        return

    def setoutputdir(self, outputdir):
        self.__outputdir__ = outputdir


