#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$...........................................................................$$
$$..........................$$$$$$$$$$$$$....................................$$
$$.......................$$$$$$$$$$$$$$$$$$$.................................$$
$$.....................$$$$$$$$$$$$$$$$$$$$$$$...............................$$
$$....................$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$.$$...............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$...$$..............................$$
$$...................$$$$$$$$$$$$$$$$$$.$$...$$$.............................$$
$$...................$$$$$$$$$$$$$$$$$$$$$$$$$$..............................$$
$$....................$$$$$$$$$$$$$.....$$$$$$$$$............................$$
$$......................$$$$$$$$$$$$$$$$..$$$$$$$............................$$
$$...................................$$$.....................................$$
$$.................$$................$$$$ $$$$$$$........$...................$$
$$...............$$$$$$..............$$$$$$$$$$$$$...$$$$$$..................$$
$$............$$$$..$$$$$.........................$$$$$$$$$..................$$
$$............$$$$...$$$$$$$....................$$$$$$.$$.$$.................$$
$$...............$$$$$$$$$$$$$$............$$$$$$$$..........................$$
$$.........................$$$$$$$$$...$$$$$$$...............................$$
$$..............................$$$$$$$$$$...................................$$
$$..........................$$$$$....$$$$$$$$$...............................$$
$$............$$.$$$$$$$$$$$$$............$$$$$$$$$$$$$$$$$..................$$
$$............$$.$$..$$$$.....................$$$$$$$$$$$$$$.................$$
$$..............$$$$$$............................$$.$$$$$$$.................$$
$$..................                                   ......................$$
$$.................. @@@  @@@  @@@@@@@        @@@@@@@ .......................$$
$$.................. @@@  @@@  @@@   @@@@     @@@   @@@@.....................$$
$$.................. @@!  @@@  @@!   !@@      @@!   !@@......................$$
$$.................. !@!  @!@  !@!   !@!      !@!   !@!......................$$
$$.................. @!@  !@!  !!@!@!!@@!     !!@!@!!@@!.....................$$
$$.................. !@!  !!!  !!!      !!!   !!!     !!!....................$$
$$.................. :!:  !!:  !!:      :!!   !!:     :::....................$$
$$................... ::!!:!   :!:      :!:   :!:     :::....................$$
$$.................... ::::    :::      :::   :::     :::....................$$
$$...................... :      :        :      :::::::  ....................$$
$$...........................................................................$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$***************************************************************************$$
$$      ChatBotServer.py  Created by  Durodola Opemipo 2018                  $$
$$            Personal Email : <opemipodurodola@gmail.com>                   $$
$$                 Telephone Number: +2348182104309                          $$
$$***************************************************************************$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
import sys
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol
from twisted.internet import reactor
from twisted.python import log

#
from ip_utils import get_pub_IP

port = 3000


class ChatBotServerProtocol(WebSocketServerProtocol):
    def __init__(self):
        super().__init__()
        self.driver = []
        self.company = {}
        self.process = "REGISTER"
        self.form_field = None
        self.previous_process = None

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        self.factory.register(self)
        print("Client connected: {0}".format(self.peer))

    def connectionLost(self, reason):
        self.factory.unregister(self)
        print("Client disconnected: {0}".format(self.peer))

    def onMessage(self, payload, isBinary):
        payload = payload.decode('utf-8')
        client = self
        print("Client {0} sending message: {1}".format(self.peer, payload))
        # self.factory.communicate(self, "Hello world!!", True)

        print(" State of Server ", self.process)


class ChatBotRouletteFactory(WebSocketServerFactory):

    def __init__(self, *args, **kwargs):
        super(ChatBotRouletteFactory, self).__init__(*args)
        self.clients = []

    def register(self, client):
        self.clients.append({'client-peer': client.peer, 'client': client})

    def unregister(self, client):
        for c in self.clients:
            if c['client-peer'] == client.peer: self.clients.remove(c)

    def broadcast_communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c['client'] == client:
                print("I am the client ", client)
                id = i
                break
        for c in self.clients:
            print("This are the present clients   -->", c)
            try:
                msg = '{0}'.format(payload.decode('utf-8'))
            except AttributeError:
                msg = '{0}'.format(payload)
            c['client'].sendMessage(str.encode(msg))

    def communicate(self, client, payload, isBinary):
        for i, c in enumerate(self.clients):
            if c['client'] == client:
                id = i
                break
        for c in self.clients:
            print("This are the present clients   -->", c)
            if c['client'] == client:
                print("Sending message to ", client)
                try:
                    msg = '{0}'.format(payload.decode('utf-8'))
                except AttributeError:
                    msg = '{0}'.format(payload)
                c['client'].sendMessage(str.encode(msg))


if __name__ == "__main__":
    log.startLogging(sys.stdout)
    ip_add = get_pub_IP()
    print("This is IP", ip_add)

    factory = ChatBotRouletteFactory(u"ws://" + ip_add + ":3000")
    factory.protocol = ChatBotServerProtocol

    reactor.listenTCP(port, factory)
    print("ChatBot Server started on port %s" % (port,))

reactor.run()
