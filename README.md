# open-community-net

Open source toolkit for building a **community-owned network**: socket-level code,
a lab 4G/5G stack (srsRAN + Open5GS), an OpenWrt mesh, a gateway, and monitoring.

> ⚠️ **Legal first.** In India, transmitting on mobile bands (700/900/1800/2100/2300/2500 MHz, 3.3 GHz)
> without a DoT/WPC licence is illegal and interferes with real networks.
> Everything in `lab-4g5g/` is for **cable-connected or shielded-box testing only**, using the
> test PLMN 001/01 at minimal power. See `docs/01-legal-india.md`.

## Layout
| Folder | What it is |
|---|---|
| `docs/` | Overview, legal notes, architecture, roadmap, community model |
| `sockets/` | TCP chat, UDP echo, simple file transfer (Python) |
| `lab-4g5g/` | Open5GS core + srsRAN eNB/UE configs, docker-compose, SIM provisioning |
| `mesh/openwrt/` | OpenWrt + BATMAN-adv mesh configs and node setup script |
| `gateway/` | NAT/firewall (nftables), WireGuard uplink, captive portal (CoovaChilli) |
| `monitoring/` | Prometheus + Grafana stack |

## Quick start
```bash
make sockets-demo     # run the TCP chat server locally
make lab-up           # start Open5GS core in docker (lab only)
make monitoring-up    # Prometheus + Grafana on :3000
```

## Honest note
Code is free. Fibre, towers, spectrum and electricity are not. See `docs/04-community-model.md`
for how communities share those costs (panchayat, K-FON, CSR, membership).

Licence: MIT (see LICENSE).
