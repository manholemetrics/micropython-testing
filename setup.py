import pycom
from network import WLAN
import machine

pycom.pybytes_on_boot(False) #we do not want Pybytes using the WLAN
pycom.smart_config_on_boot(False) #we also do not want smart config
pycom.wifi_on_boot(False)
machine.reset()