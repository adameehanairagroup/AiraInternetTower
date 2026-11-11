#!/bin/sh
# OpenWrt BATMAN-adv Gateway Mode Configuration
# Engineered for Aira Internet Tower (AIT)
# Run on the node connected to upstream backhaul (Fibre / K-FON / ISP)

set -e

echo "[*] Configuring B.A.T.M.A.N.-adv Gateway Server Mode..."
if command -v batctl >/dev/null 2>&1; then
    batctl gw_mode server 50mbit/10mbit || true
fi

if command -v uci >/dev/null 2>&1; then
    uci set batman-adv.bat0.gw_mode='server'
    uci set batman-adv.bat0.gw_bandwidth='50mbit/10mbit'
    uci commit batman-adv
fi

echo "[*] Enabling IPv4 packet forwarding in kernel..."
sysctl -w net.ipv4.ip_forward=1 >/dev/null 2>&1 || echo "1" > /proc/sys/net/ipv4/ip_forward

echo "[+] Gateway mode active. Mesh client nodes will automatically route through this uplink."
