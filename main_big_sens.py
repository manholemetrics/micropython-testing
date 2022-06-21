
def big():
    import utime
    from network import LTE
    import time
    import ssl
    import socket

    import machine
    from machine import Pin
    enable = Pin("P11", mode=Pin.OUT)
    enable.value(1)


    lte = LTE()
    lte.attach(band = 20, apn="simbase")
    print("attaching..",end='')
    while not lte.isattached():
        time.sleep(0.25)

        print('.',end='')
        print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
    print("attached!")

    lte.connect()
    print("connecting [##",end='')
    while not lte.isconnected():
        time.sleep(0.25)
        print('#',end='')
        #print(lte.send_at_cmd('AT!="showphy"'))
        print(lte.send_at_cmd('AT!="fsm"'))
    print("] connected!")

    try:
        print(socket.getaddrinfo('www.google.com', 80))  
    except:
        print("fail")
    import urequests

    start_time = int(time.time())

    adc = machine.ADC()             # create an ADC object
    apin = adc.channel(pin='P20')   # c
    val = apin()

    #while(True):
    #    print(apin())

    while(True):
        print("Running")
        try:
            try:
                distance = 0
                s = int(time.time())
                while apin() < 1000:
                    #print((s - int(time.time())))
                    if (int(time.time())) -s > 3:
                        raise Exception
                    continue
                start = utime.ticks_us()
                while apin() > 1000:
                    #print("b")
                    if int(time.time()) - s> 3:
                        raise Exception
                    continue
                finish = utime.ticks_us()
                distance = ((utime.ticks_diff(finish, start)))/58
                print("D",distance)
            except:
                distance = 0
                print("D",distance)

            userdata = {"distance_mm":int(distance*10), "device_id":"1"}
            url = 'http://178.128.174.134:8080/data'
            res = urequests.post(url, headers={"Content-Type": "application/json", "Accept": "application/json"}, data= str(userdata))
            print(res.text)
            res.close()
        except:
            print("exception")