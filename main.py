#!/bin/python

#scapy is a python library that allows more control over packets sent
import socks
import socket
import scapy.all as scapy


#choose a scan profile, this could be a useful feature to avoid detection by failed connection attempts let me know what you think
scan_profile = ["web", "database", "mail", "workstation"]

#dictionary of top ports as keys and associated services as values
top_ports = {7:"Echo", 20:"FTP Data", 21:"FTP Service", 22:"SSH", 23:"Telnet", 25:"SMTP", 42:"WINS", 43:"WHOIS", 53:"DNS", 67:"DHCP", \
68:"DHCP", 69:"TFTP", 80:"HTTP", 88:"Kerberos", 110:"POP3", 123:"NTP", 135:"RPC", 137:"NetBIOS", 138:"NetBIOS", 139:"NetBIOS", 161:"SNMP", 162:"SNMP", 389:"LDAP", \
443:"SSL", 445:"Microsoft DS", 513:"rlogin", 514:"syslog", 520:"RIP", 546:"DHCPv6", 547:"DHCPv6", 587:"SMTP", 636:"LDAP over SSL", 989:"FTP over SSL", 990:"FTP over SSL", \
 993:"IMAP4 over SSL", 995:"POP3 over SSL", 1194:"OpenVPN", 1080:"SOCKS Proxy", 1241:"Nessus", 1812:"RADIUS", 1813:"RADIUS", 2483:"Oracle DB", 3306:"MySQL"}
 
 other_ports = [1..65535]
 
 #remove top ports from other ports list
 for x in top_ports.keys():
	other_ports.remove(x)
 
 def choose_port():
	
def connect(scapSstr, ip, hostn=""):
	port = choose_port()
	if hostn != "":
		try:	#send SYN packet and get the response, this is where the meat of the scanner will be where we send the spoofed packets
			syn = IP(dst=hostn) / TCP(dport=port), flags='S')
			syn_ack = sr1(syn)

#set proxy for python to use, this will be a tor proxy so tor must be setup for it to work
def main():
	target_socket = socks.socksocket()
	target_socket.setproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 9050)

	target = input("Please enter the IP address of the target you want to scan: ")
	#gets the hostname of the IP address, this will make the traffic look more normal since the connections will use a hostname and not an IP address
	named_target = socket.gethostbyaddr(target)[0]
	scapStream = StreamSocket(target_socket)
	
