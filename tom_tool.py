import esptool
import requests
import serial
import sys

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
    if item.vid == 0xCAFE and (result == "" or result == "Y" or result == "Yes" or result == "yes"):    
        r = requests.get(url, allow_redirects=True)
        if r.ok:
            open('firmware.bin', 'wb').write(r.content)
            esptool.main(["--baud", "115200", "--port", item.device, "erase_flash"])
            esptool.main(["--baud", "460800", "--port", item.device, "--before", "default_reset", "--after", "hard_reset", "write_flash", "-z", "--flash_mode", "dio", "--flash_freq", "80m", "--flash_size", "detect", "0x1e1000", "initial_fs.zip", "0xd000", "ota_data_initial.bin", "0x1000", "bootloader.bin", "0x10000", "firmware.bin", "0x8000", "campzone2020_16MB.bin"])
            print("""
Flash succes!
Further instructions:
Initially 3 buttons light up, wait until the whole display is dimly lit.
Press diagonal from top left to bottom right afterwhich the buttons will turn green.
Press the home button to reboot into you brand new badge!           
""")            
            input("Press enter to exit")
            sys.exit()
        else:
            input("Download failed ;(, press enter to exit")
            sys.exit()
input("Badge not detected :(, press enter to exit")
