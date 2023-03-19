import argparse
import scapy.all as scapy

class ARPPinger():
  def __init__(self):
    print("ARPPinger has started!")

  def userInputCheckAll(self):
      parser = argparse.ArgumentParser()
      parser.add_argument("-i", "--ipadress", type=str, help="Please write IP Adress")
      args = parser.parse_args()
      if args.ipadress == None:
          print("IP Adress not found!")
      else:
          return args

  def arp_request(self, ip):
      print("IP Range: " + ip)
      arp_request_packet= scapy.ARP(pdst=ip)
      broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

      ansList, unansList = scapy.srp(broadcast_packet / arp_request_packet, timeout=2)
      ansList.summary()

if __name__ == "__main__":
    arp_pinger = ARPPinger()
    arp_pinger.arp_request(arp_pinger.userInputCheckAll().ipadress)




