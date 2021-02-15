import subprocess
import optparse
import re
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Mac Changer")
print(ascii_banner)

def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface")
    parse_object.add_option("-m","--mac",dest="mac_address")

    return parse_object.parse_args()

def change_mac_address(user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def control_new_mac(interface):
    ifconfig= subprocess.check_output(["ifconfig",interface])
    new_mac=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))

    if new_mac:
        return new_mac.group(0)

print("MacChanger started...")
(user_input,arguments)=get_user_input()
change_mac_address(user_input.interface,user_input.mac_address)
last_mac_adress=control_new_mac(str(user_input.interface))


if last_mac_adress==user_input.mac_address:
    print("Your mac adress has been successfully changed...")

else:
    print("Error...")