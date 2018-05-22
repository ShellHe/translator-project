#!/usr/bin/env python

"""Here we load a .TTF font file, and display it in
a basic pygame window. It demonstrates several of the
Font object attributes. Nothing exciting in here, but
it makes a great example for basic window, event, and
font management."""

import pygame
from pygame.locals import *
from pygame.compat import unichr_, unicode_
import sys
import locale

if sys.version_info >= (3,):
    def print_unicode(s):
        e = locale.getpreferredencoding()
        print(s.encode(e, 'backslashreplace').decode())
else:
    def print_unicode(s):
        e = locale.getpreferredencoding()
        print(s.encode(e, 'backslashreplace'))


def main():
    # initialize
    pygame.init()
    resolution = 400, 200
    screen = pygame.display.set_mode(resolution)

    ##    pygame.mouse.set_cursor(*pygame.cursors.diamond)

    fg = 250, 240, 230
    bg = 5, 5, 5
    wincolor = 40, 40, 90

    # fill background
    screen.fill(wincolor)

    # load font, prepare values
    font = pygame.font.Font(None, 80)
    text = u"黒澤 明"


    a_sys_font = pygame.font.Font("Cyberbit.ttf", 60)


    ren = a_sys_font.render(text, 1, fg)
    screen.blit(ren, (30 , 40 ))





    # show the surface and await user quit
    pygame.display.flip()
    while 1:
        # use event.wait to keep from polling 100% cpu
        if pygame.event.wait().type in (QUIT, KEYDOWN):
            break


if __name__ == '__main__': main()

