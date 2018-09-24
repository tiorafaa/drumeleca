#!/usr/bin/env python
# ----------------------------------------------------------------------------
# DRUMELECA
# Desenvolvido por Rafael Amaral Salgueiroza
# Voce pode alterar e/ou redistribuir este codigo-fonte.
# Voce pode entrar em contato comigo em rafael@salgueiroza.com.br
# Este projeto foi desenvolvido entre 2016 e 2018.
# ----------------------------------------------------------------------------

'''
'''

__docformat__ = 'restructuredtext'


import pyglet
# pyglet.options['audio'] = ('openal', 'pulse', 'silent')
import threading
import time
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()
caixa = pyglet.resource.media('caixab.wav', streaming=False)
cimbal = pyglet.resource.media('cimbala.wav', streaming=False)
opencimbal = pyglet.resource.media('cimbalb.wav', streaming=False)
bumbo = pyglet.resource.media('bumboa.wav', streaming=False)
stick = pyglet.resource.media('stick.wav', streaming=False)
stickb = pyglet.resource.media('stickb.wav', streaming=False)

# Metronomo
@window.event
def funcaometronomo(bpm = 80, bpb = 4):

    sleep = 60.0 / bpm
    counter = 0
    while True:
        counter += 1
        if counter % bpb:
            stick.play()
        else:
            stickb.play()
        time.sleep(sleep)
metronomo = threading.Thread(target=funcaometronomo)

# Capturador de teclas
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        if modifiers & key.MOD_CTRL:
            opencimbal.play()
            print ('CIMBAL ABERTO')
        else:
            cimbal.play()
            print ('CIMBAL FECHADO')
    elif symbol == key.ENTER:
        caixa.play()
        print ('CAIXA')
    elif symbol == key.SPACE:
        bumbo.play()
        print ('BUMBO')
    elif symbol == key.M:
        # tratar o caso do metronomo ja ter iniciado
        metronomo.start()
        print ('Metronomo iniciou')

# Capturador do mouse (?)
@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print ('The left mouse button was pressed.')

pyglet.app.run()
