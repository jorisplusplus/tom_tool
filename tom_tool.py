import esptool
import requests
import serial

url = 'https://ota.cz20.hackz.one/campzone2020.bin'

print(""" ______________________________________
/ Seems like you want to reflash your   \\
| badge. Are you sure? this will delete |
\ everything on the badge               /
 --------------------------------------
 \\
  \\
     __
    /  \\
    |  |
    @  @
    |  |
    || |/
    || ||
    |\_/|
    \___/""")

result = input("Reflash? [Y/n]")
for item in serial.tools.list_ports.comports():
    if item.manufacturer == "HackZone" and (result == "" or result == "Y" or result == "Yes" or result == "yes"):    
        r = requests.get(url, allow_redirects=True)
        open('firmware.bin', 'wb').write(r.content)
        esptool.main(["-b", "115200", "-p", item.device, "erase_flash"])
        esptool.main(["--baud", "2000000", "--port", item.device, "--before", "default_reset", "--after", "hard_reset", "write_flash", "-z", "--flash_mode", "dio", "--flash_freq", "80m", "--flash_size", "detect", "0xd000", "ota_data_initial.bin", "0x1000", "bootloader.bin", "0x10000", "firmware.bin", "0x8000", "debug_4MB.bin"])

