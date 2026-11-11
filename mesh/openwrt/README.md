# OpenWrt + BATMAN-adv mesh
Uses licence-free Wi-Fi (2.4/5 GHz, respect power limits).
1. Flash OpenWrt on supported routers (check the OpenWrt Table of Hardware).
2. Install packages: `opkg update && opkg install kmod-batman-adv batctl-full wpad-mesh-openssl`
3. Copy `config/*` to `/etc/config/`, edit the SSID/key/IP, `reboot`.
4. One node with fibre/upstream = gateway: run `scripts/gateway_mode.sh` on it.
5. Check neighbours: `batctl n`, `batctl o`.
