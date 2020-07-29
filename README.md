# tom_tool
T.O.M. Tool (Total overhaul maintenance tool)

Last-resort recovery for the campzone 2020 badge. Use this when your badge won't boot anymore due to filesystem errors. This tool flashes the latest firmware and the stock fs on the badge with a single press on your enter key. Note that this tool in current form is very experimental and should only be used as last resort.

!! Before you can run this tool, you will need to update the STM32 chip on your badge here: https://webupdate.hackz.one. !!

## Linux / Mac
Run `pip3 install esptool pyserial requests; python3 tom_tool.py`.

## Windows
Download the latest release zip of this repository (e.g. https://github.com/jorisplusplus/tom_tool/releases/latest), unpack it completely, and run tom_tool.exe.


