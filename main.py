# # from network import LTE
# # import machine
# # import time
# # import socket

# # from machine import SD
# # import os

# # sd = SD()
# # os.mount(sd, '/sd')     # mount it
# # os.fsformat('/sd')    # format SD card
# # fs = os.mkfat(sd)
# # print(os.listdir('/sd'))     

# # import sqnsupgrade
# # print(sqnsupgrade.info())

# # import sqnsupgrade
# # sqnsupgrade.run('/sd/NB1-41019.dup')
# # lte = LTE()
# # lte.attach(band = 20, apn="simbase")
# # print("attaching..",end='')
# # while not lte.isattached():
# #     time.sleep(0.25)

# #     print('.',end='')
# #     print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
# # print("attached!")

# # lte.connect()
# # print("connecting [##",end='')
# # while not lte.isconnected():
# #     time.sleep(0.25)
# #     print('#',end='')
# #     #print(lte.send_at_cmd('AT!="showphy"'))
# #     print(lte.send_at_cmd('AT!="fsm"'))
# # print("] connected!")

# # try:import machine

# ################Test

# # adc = machine.ADC()             # create an ADC object
# # apin = adc.channel(pin='P16')   # create an analog pin on P16
# # val = apin()
# # #     print(socket.getaddrinfo('www.google.com', 80))  
# # # except:
# # #     print("fail")
# # # lte.deinit(detach=False, reset=False)
# # # machine.deepsleep(60000)

# # from make_measurement import distance_measure

# # while(True):
# #     try:
# #         print(distance_measure())
# #     except:
# #         pass



# ################Test
# # import machine
# # import time
# # import utime

# # adc = machine.ADC()             # create an ADC object
# # apin = adc.channel(pin='P16')   # create an analog pin on P16
# # val = apin()

# # while(True):
# #     while apin() < 1000:
# #         continue
# #     start = utime.ticks_us()
# #     while apin() > 1000:
# #         continue
# #     finish = utime.ticks_us()
# #     distance = ((utime.ticks_diff(finish, start)))/58
# #     print(distance)


# ################Test

# # import wifi_test

# # print("hello")



# ###########################################################

# from make_measurement import distance_measure
# import utime
# from network import LTE
# import time
# import ssl
# import socket

# import machine
# from machine import Pin
# enable = Pin("P11", mode=Pin.OUT)
# enable.value(1)

# # from network import WLAN
# # # configure the WLAN subsystem in station mode (the default is AP)
# # wlan = WLAN(mode=WLAN.STA)
# # wlan.disconnect()
# lte = LTE()
# lte.attach(band = 20, apn="simbase")
# print("attaching..",end='')
# while not lte.isattached():
#     time.sleep(0.25)

#     print('.',end='')
#     print(lte.send_at_cmd('AT!="fsm"'))         # get the System FSM
# print("attached!")

# lte.connect()
# print("connecting [##",end='')
# while not lte.isconnected():
#     time.sleep(0.25)
#     print('#',end='')
#     #print(lte.send_at_cmd('AT!="showphy"'))
#     print(lte.send_at_cmd('AT!="fsm"'))
# print("] connected!")

# try:
#     print(socket.getaddrinfo('www.google.com', 80))  
# except:
#     print("fail")
# import urequests

# start_time = int(time.time())

# adc = machine.ADC()             # create an ADC object
# apin = adc.channel(pin='P20')   # create an analog pin on P16
# val = apin()


# x = 0
# while(True):
#     print("Running")
#     try:
#         x += 1
#         try:
#             distance = 0
#             s = int(time.time())
#             while apin() < 1000:
#                 #print((s - int(time.time())))
#                 if (int(time.time())) -s > 3:
#                     raise Exception
#                 continue
#             start = utime.ticks_us()
#             while apin() > 1000:
#                 #print("b")
#                 if int(time.time()) - s> 3:
#                     raise Exception
#                 continue
#             finish = utime.ticks_us()
#             distance = ((utime.ticks_diff(finish, start)))/58
#             print("D",distance)
#         except:
#             distance = 0
#         # except:
#         #     distance = 0
#         userdata = {"time":time.time() - start_time,"distance":int(distance)}
#         url = 'http://178.128.174.134:8080/data'
#         res = urequests.post(url, headers={"Content-Type": "application/json", "Accept": "application/json"}, data= str(userdata))
#         print(res.text)
#         res.close()
#     except:
#         print("exception")


# # setup socket for connection
# # s = socket.socket()
# # ssl.wrap_socket(s)
# # host = 'test-server-jh8nn.ondigitalocean.app/data'
# # addr = socket.getaddrinfo(host, 443)[0][-1]
# # print(addr)
# # s.connect(addr)
# # print('socket connected')
# # # # it is possible to attach additional HTTP headers in the line below, but note to always close with \r\n\r\n
# # httpreq = 'GET / HTTP/1.1 \r\nHOST: '+ host + '\r\nConnection: close \r\n\r\n'
# # print('http request: \n', httpreq)
# # s.send(httpreq)
# # time.sleep(1)
# # rec_bytes = s.recv(10000)
# # print(rec_bytes)
# # print('end')

# lte.deinit() 



from main_big_sens import big

big()