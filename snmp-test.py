import subprocess
import getpass

host_list = input("Enter your filename: ")
community_string = getpass.getpass(prompt='Enter Community String: ', stream=None)
# Assumes the text file contains a single column of IP addresses, one per line.
with open(host_list) as f:
  addrs = f.readlines()

for i in addrs:
  i = i.strip() # Remove the newline character from the IP address string.
  print("\n--- Starting SNMP Walk on", i, "---") #Start marker
  # SNMPWALK COMMAND = snmpwalk -r2 -c community_string -v2c <HOST> sysDescr.0
  snmp_test = subprocess.run(["snmpwalk", "-r1", "-c", community_string, "-v2c", i, "sysDescr.0"])
  print("--- Done ---\n") #End Marker
