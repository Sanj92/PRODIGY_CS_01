from scapy.all import sniff, IP, TCP, UDP, raw

def packet_callback(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst

        # Determine protocol type
        if TCP in packet:
            protocol = "TCP"
            payload = raw(packet[TCP].payload).decode(errors='ignore')
        elif UDP in packet:
            protocol = "UDP"
            payload = raw(packet[UDP].payload).decode(errors='ignore')
        else:
            protocol = "Other"
            payload = raw(packet.payload).decode(errors='ignore')

        # Print packet information
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        print(f"Payload: {payload}")
        print("-" * 50)

def main():
    # Start sniffing packets on the network
    print("Starting packet capture. Press Ctrl+C to stop.")
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
