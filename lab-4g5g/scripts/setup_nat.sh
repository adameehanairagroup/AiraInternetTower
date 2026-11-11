#!/usr/bin/env bash
# Enables forwarding + NAT for the Open5GS UE subnet.
set -euo pipefail
WAN_IF=${WAN_IF:-eth0}
sysctl -w net.ipv4.ip_forward=1
iptables -t nat -C POSTROUTING -s 10.45.0.0/16 -o "$WAN_IF" -j MASQUERADE 2>/dev/null || \
  iptables -t nat -A POSTROUTING -s 10.45.0.0/16 -o "$WAN_IF" -j MASQUERADE
iptables -C FORWARD -i ogstun -j ACCEPT 2>/dev/null || iptables -I FORWARD 1 -i ogstun -j ACCEPT
echo "NAT ready on $WAN_IF"
