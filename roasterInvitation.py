#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from getpass import getpass
from argparse import ArgumentParser

import slixmpp


class EchoBot(slixmpp.ClientXMPP):
    
    def __init__(self, jid, password, nameClient):
        slixmpp.ClientXMPP.__init__(self, jid, password)

        self.client = nameClient
        self.add_event_handler("session_start", self.start)

    def start(self, event):
        
        self.send_presence()
        self.get_roster()
        #self.update_roster('testpython@alumchat.xyz', name='Romeo', groups=['General'])
        #self.update_roster('testpython@alumchat.xyz', subscription='remove', groups=['General'])
        xmpp.send_presence(pto=self.client, ptype='subscribe')


if __name__ == '__main__':
    # Setup the command line arguments.
    parser = ArgumentParser(description=EchoBot.__doc__)

    # Output verbosity options.
    parser.add_argument("-q", "--quiet", help="set logging to ERROR",
                        action="store_const", dest="loglevel",
                        const=logging.ERROR, default=logging.INFO)
    parser.add_argument("-d", "--debug", help="set logging to DEBUG",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.INFO)

    # JID and password options.
    parser.add_argument("-j", "--jid", dest="jid",
                        help="JID to use")
    parser.add_argument("-p", "--password", dest="password",
                        help="password to use")
    parser.add_argument("-t", "--to", dest="to",
                        help="JID to send the suscripcion")

    args = parser.parse_args()

    # Setup logging.
    logging.basicConfig(level=args.loglevel,
                        format='%(levelname)-8s %(message)s')

    if args.jid is None:
        args.jid = input("Username: ")
    if args.password is None:
        args.password = getpass("Password: ")
    if args.to is None:
        args.to = input("Add To: ")
    xmpp = EchoBot(args.jid, args.password, args.to)
    xmpp.register_plugin('xep_0030') # Service Discovery
    xmpp.register_plugin('xep_0004') # Data Forms
    xmpp.register_plugin('xep_0060') # PubSub
    xmpp.register_plugin('xep_0199') # XMPP Ping

    xmpp.connect()
    xmpp.process()
