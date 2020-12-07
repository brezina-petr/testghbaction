# fakesmtpserver
python cmd app smtp server receives emails and save them to filesystem - utility for smtp emails developers 

Received email is stored to output directory ( default is ./receivedemails/ ). One email is stored in 2 versions(in txt and eml) for own developing analyse. Name of files is datetime of received email. Next info about received email is added as row to common.log (datetime, from, to).

![alt text](https://github.com/brezina-petr/fakesmtpserver/blob/main/doc/a1.png)

Running:
main.py -n <hostname> -p <port> -o <outputdirectory>

Example:
main.py -n 0.0.0.0 -p 2555 -o ./receivedemails/
