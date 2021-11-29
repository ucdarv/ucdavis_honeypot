from smtplib import SMTP as Client

client = Client('127.0.0.1', 10025)

r = client.sendmail('mahussien@ucdavis.edu', ['bishop@ucdavis.edu'], """\
From: Mohamed Hussien <mahussien@ucdavis.edu>
To: Matt Bishop <bishop@ucdavis.edu>
Subject: A test
Message-ID: <TEST>
...
Hi Matt, this is Mo.
""")