
#!/usr/bin/env python
import subprocess
import optparse

def mac_changer(interface, new_mac):
    print(f"Changing the mac address of {interface} to {new_mac}")
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", "dev", interface,  "up"])
    print("{+} MAC address changed successfully!")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to show the MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Plese enter the interface or reffer to --help")
    elif not options.new_mac:
        parser.error("Plese enter the mac address or reffer to --help")

    return options

options =get_arguments()
mac_changer(options.interface, options.new_mac)
