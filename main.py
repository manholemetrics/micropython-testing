# from make_measurement import distance_measure
# import utime
# from network import LTE
# import time
# import ssl
# import socket

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
# x = 0
# while(True):
#     try:
#         x += 1
#         try:
#             distance = distance_measure()
#         except:
#             distance = 0
#         userdata = {"time":time.time() - start_time,"distance":distance}
#         url = 'http://178.128.174.134:8080/data'
#         res = urequests.post(url, headers={"Content-Type": "application/json", "Accept": "application/json"}, data= str(userdata))
#         print(res.text)
#         res.close()
#     except:
#         print("exception")


# # # setup socket for connection
# # # s = socket.socket()
# # # ssl.wrap_socket(s)
# # # host = 'test-server-jh8nn.ondigitalocean.app/data'
# # # addr = socket.getaddrinfo(host, 443)[0][-1]
# # # print(addr)
# # # s.connect(addr)
# # # print('socket connected')
# # # # # it is possible to attach additional HTTP headers in the line below, but note to always close with \r\n\r\n
# # # httpreq = 'GET / HTTP/1.1 \r\nHOST: '+ host + '\r\nConnection: close \r\n\r\n'
# # # print('http request: \n', httpreq)
# # # s.send(httpreq)
# # # time.sleep(1)
# # # rec_bytes = s.recv(10000)
# # # print(rec_bytes)
# # # print('end')

# # lte.deinit() 

