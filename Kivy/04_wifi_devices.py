# Source: https://pypi.org/project/pywifi/ (accessed on 15th April, 2022)

import pywifi, time
from pywifi import const


wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()
time.sleep(1)
assert iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)

iface.connect(tmp_profile)
time.sleep(2)
# assert iface.status() == const.IFACE_CONNECTED
result = iface.status() == const.IFACE_CONNECTED
print(result)

iface.disconnect()
time.sleep(1)
# assert iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
result =  iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
print(result)