INTEGRANTES
Juliana Villalobos
Andres Franco

CODIGO 1
from machine import Pin as pin

from utime import sleep, sleep_ms

led1 = pin(13,pin.OUT)

led2 = pin(14,pin.OUT)

led3 = pin(26,pin.OUT)

led4 = pin(25,pin.OUT)

led5 = pin(32,pin.OUT)

led6 = pin(23,pin.OUT)

led7 = pin(22,pin.OUT)

led8 = pin(21,pin.OUT)



pausa = 0.5

while True:

    led1.value(1)

    sleep(pausa)

    led1.value(0)

    sleep(pausa)

    led2.value(1)

    sleep(pausa)

    led2.value(0)

    sleep(pausa)

    led3.value(1)

    sleep(pausa)

    led3.value(0)

    sleep(pausa)

    led4.value(1)

    sleep(pausa)

    led4.value(0)

    sleep(pausa)

    led5.value(1)

    sleep(pausa)

    led5.value(0)

    sleep(pausa)

    led6.value(1)

    sleep(pausa)

    led6.value(0)

    sleep(pausa)

    led7.value(1)

    sleep(pausa)

    led7.value(0)

    sleep(pausa)

    led8.value(1)

    sleep(pausa)

    led8.value(0)

    sleep(pausa)


    CODIGO 2
    from machine import Pin as pin

from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

led1 = pin(13,pin.OUT)

led2 = pin(14,pin.OUT)

led3 = pin(26,pin.OUT)

led4 = pin(25,pin.OUT)

led5 = pin(32,pin.OUT)

led6 = pin(23,pin.OUT)

led7 = pin(22,pin.OUT)

led8 = pin(21,pin.OUT)

def print_led(a,b,c,d,e,f,g,h):

    led1.value(a)

    led2.value(b)

    led3.value(c)

    led4.value(d)

    led5.value(e)

    led6.value(f)

    led7.value(g)

    led8.value(h)

    pausam(200)

while True:

    print_led(1,1,0,0,0,0,0,0,0,0)

    print_led(0,0,1,1,0,0,0,0,0,0)

    print_led(0,0,0,0,1,1,0,0,0,0)

    print_led(0,0,0,0,0,0,1,1,0,0)

    print_led(0,0,0,0,0,0,0,0,1,1)

    print_led(0,0,0,0,0,0,1,1,0,0)

    print_led(0,0,0,0,1,1,0,0,0,0)

    print_led(0,0,1,1,0,0,0,0,0,0)





    CODIGO 3
    from machine import Pin as pin

from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

led1 = pin(13,pin.OUT)

led2 = pin(14,pin.OUT)

led3 = pin(26,pin.OUT)

led4 = pin(25,pin.OUT)

led5 = pin(32,pin.OUT)

led6 = pin(23,pin.OUT)

led7 = pin(22,pin.OUT)

led8 = pin(21,pin.OUT)

def print_led(a,b,c,d,e,f,g,h,):

    led1.value(a)

    led2.value(b)

    led3.value(c)

    led4.value(d)

    led5.value(e)

    led6.value(f)

    led7.value(g)

    led8.value(h)



 pausam(350)

while True:

    print_led(1,1,0,0,0,0,0,0,0,0)

    print_led(0,0,1,1,0,0,0,0,0,0)

    print_led(0,0,0,0,1,1,0,0,0,0)

    print_led(0,0,0,0,0,0,1,1,0,0)

    print_led(0,0,0,0,0,0,0,0,1,1)

    print_led(0,0,0,0,0,0,1,1,0,0)

    print_led(0,0,0,0,1,1,0,0,0,0)

    print_led(0,0,1,1,0,0,0,0,0,0)

    print_led(1,1,0,0,0,0,0,0,0,0)

    print_led(1,1,1,1,1,1,1,1,1,1)

    print_led(1,0,0,0,0,0,0,0,0,0)

    print_led(0,1,0,0,0,0,0,0,0,0)

    print_led(0,0,1,0,0,0,0,0,0,0)

    print_led(0,0,0,1,0,0,0,0,0,0)

    print_led(0,0,0,0,1,0,0,0,0,0)

    print_led(0,0,0,0,0,1,0,0,0,0)

    print_led(0,0,0,0,0,0,1,0,0,0)

    print_led(0,0,0,0,0,0,0,1,0,0)




    CODIGO 4
    from machine import Pin as pin

import utime

led1 = pin(13,pin.OUT)

led2 = pin(14,pin.OUT)

led3 = pin(26,pin.OUT)

led4 = pin(25,pin.OUT)

led5 = pin(32,pin.OUT)

led6 = pin(23,pin.OUT)

led7 = pin(22,pin.OUT)

led8 = pin(21,pin.OUT)

todos = [led1,led2,led3,led4,led5,led6,led7,led8]

def derecha():

    for elemento in todos:

        elemento.value(1)

        utime.sleep_ms(50)

        elemento.value(0)

        utime.sleep(0.05)



def izquierda():

    for elemento in reversed(todos):

        elemento.value(1)

        utime.sleep_ms(0.05)

        elemento.value(0)

        utime.sleep(0.05)



while True:

    derecha()

    izquierda()


    CODIGO 5from machine import Pin as pin

from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau

led1 = pin(13,pin.OUT)

led2 = pin(14,pin.OUT)

led3 = pin(26,pin.OUT)

led4 = pin(25,pin.OUT)

led5 = pin(32,pin.OUT)

led6 = pin(23,pin.OUT)

led7 = pin(22,pin.OUT)

led8 = pin(21,pin.OUT)


ledt = [led1,led2,led3,led4,led5,led6,led7,led8]

def derecha():

    for i in ledt:

        for j in range (2):

            i.value(not i.value())

            pausam(150)

def izquierda():

    for i in reversed(ledt):

        for j in range (2):

            i.value(not i.value())

            pausam(150)

while True:

    derecha()

    # izquierda()



    CODIGO 6
    from machine import Pin as pin

from utime import sleep as pausa, sleep_ms

pins = [13, 14, 26, 25, 32, 23, 22, 21, ]

leds = []

for i in pins:

    leds.append (pin(i, pin.OUT))

def derecha():

    for i in leds:

        for j in range(2):

            i.value(not i.value())

            sleep_ms(200)

def izquierda():

    for i in reversed (leds):

        for j in range(2):

            i.value(not i.value())

            sleep_ms(200)

while True:

    derecha()

    izquierda()


  