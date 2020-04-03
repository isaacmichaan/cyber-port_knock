from scapy.all import *
from random import randint

dst = "10.0.2.4"
ports_flags = [[8080, "RA"], [8834, "SA"], [8840, "R"]]
for pf in ports_flags:
	srp1(Ether()/IP(dst=dst)/TCP(sport=randint(1000,65000), dport=pf[0], flags=pf[1])/Raw(load=''), timeout=1)

# Source IP XOR key... -> load
# load XOR key (check if source ip == decrypted(load))
