import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change the mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="Enter the new mac address")
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("Please enter the interface")
    elif not options.new_mac:
        parser.error("Please enter the new MAC address")
    return options


def mac_changer(interface, new_mac):
    subprocess.call(["ip", "link", "set", "dev", interface, "down"])
    subprocess.call(["ip", "link", "set", "dev", interface, "address", new_mac])
    subprocess.call(["ip", "link", "set", "dev", interface, "up"])


options= get_arguments()
def get_current_mac(interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface], text=True)
    ifconfig_mac_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_output)
    if ifconfig_mac_output:
        return ifconfig_mac_output.group(0)
    else:
        print("No MAC Adress was found...")

current_mac = get_current_mac(options.interface)
print(f"Current MAC {str(current_mac)}")
mac_changer(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"Mac address successfully changed to {current_mac}")
else:
    print("Mac address did not get changed")
