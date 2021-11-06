import asyncio
from aiosmtpd.controller import Controller
import sys


class UCDAVIS_Handler:

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):

        if not address.endswith('@ucdavis.edu'):
            return 'untrusted sender'
        envelope.rcpt_tos.append(address)

        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        """
        mo: Here we can put the filteration/processing
        """

        print(f"""
        sender: "{envelope.mail_from}"
        recipient: "{envelope.rcpt_tos}"

        ----------------
        message data:
        {envelope.content.decode('utf8', errors='replace').replace(chr(10), chr(10) + chr(9))}
        ----------------

        END OF MESSAGE!
        """, file=sys.stderr)

        print('End of message')
        return '250 Message accepted for delivery'


if __name__ == '__main__':
    handler = UCDAVIS_Handler()
    controller = Controller(handler, hostname='127.0.0.1', port=10025)
    # Run the event loop in a separate thread.
    controller.start()
    # Wait for the user to press Return.
    input('SMTP server running. Press Return to stop server and exit.')
    controller.stop()
