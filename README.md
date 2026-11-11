# 📡 Aira Internet Tower (AIT)
### Sovereign Open-Source Community Cellular & Wireless Mesh Telecommunications Blueprint

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Core: Open5GS](https://img.shields.io/badge/Core-Open5GS-008080.svg)](https://open5gs.org/)
[![RAN: srsRAN](https://img.shields.io/badge/RAN-srsRAN-orange.svg)](https://www.srsran.com/)
[![Mesh: OpenWrt](https://img.shields.io/badge/Mesh-OpenWrt%20%7C%20B.A.T.M.A.N.--adv-0099e5.svg)](https://openwrt.org/)
[![Security: WireGuard](https://img.shields.io/badge/Tunnel-WireGuard-88171a.svg)](https://www.wireguard.com/)
[![Telemetry: Prometheus%20%2B%20Grafana](https://img.shields.io/badge/Telemetry-Prometheus%20%2B%20Grafana-F46800.svg)](https://grafana.com/)
[![Founder & Architect: Er. Adam Eehan](https://img.shields.io/badge/Architect-Er.%20Adam%20Eehan-gold.svg)](https://github.com/adameehanairagroup)
[![Organization: Aira Group of Technology](https://img.shields.io/badge/Organization-Aira%20Group%20of%20Technology-blueviolet.svg)](https://airaaigroup.in)

---

## 🌟 Executive Overview

**Aira Internet Tower (AIT)** is a complete, sovereign telecommunications architecture designed to eliminate the digital divide in rural, island, and community clusters. Built from the ground up by **Aira Group of Technology**, AIT provides a modular, production-ready framework combining:

1. **Rooftop-to-Rooftop Wireless Mesh** (OpenWrt + B.A.T.M.A.N.-adv Layer 2 routing)
2. **Private Lab 4G/LTE & 5G SA Cellular Stack** (Open5GS + srsRAN SDR Core)
3. **Hardened Sovereign Edge Gateway** (nftables firewall, WireGuard backhaul tunnels, CoovaChilli captive portal)
4. **Telecom Telemetry & Network Operations Center (NOC)** (Prometheus + Grafana)
5. **Low-Level Socket Communication Primitives** (TCP/UDP, chat relays, packet-level transfer)

Designed specifically for emerging community models (such as **K-FON / BharatNet** integration in Kerala/India, Panchayat-backed village Wi-Fi grids, and university testbeds), this repository contains the complete hardware schematics, software configurations, and deployment scripts necessary to operate a community-owned ISP.

---

> ⚖️ **Important Regulatory & Legal Compliance Note (India / DoT / WPC):**  
> Transmitting on cellular licensed spectrum (700 MHz, 800 MHz, 900 MHz, 1800 MHz, 2100 MHz, 2300 MHz, 2500 MHz, and 3.3–3.6 GHz) without an explicit DoT/WPC license or experimental trial authorization is illegal under the Indian Telegraph Act.  
> The 4G/5G components in `lab-4g5g/` are strictly designed for **cable-connected RF attenuators or Faraday shielded enclosure testing** using the non-interfering test PLMN `001/01` at sub-milliwatt power. For public unlicenced community transmission, always utilize Wi-Fi unlicenced bands (2.4 GHz & 5.8 GHz) via `mesh/openwrt/`. See [`docs/01-legal-india.md`](docs/01-legal-india.md).

---

## 🏗️ End-to-End System Architecture

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      AIRA INTERNET TOWER TOPOLOGY                      │
 └────────────────────────────────────────────────────────────────────────┘

    [ COMMUNITY SUBSCRIBERS ]               [ TOWER ACCESS & RADIO LAYER ]
  ┌───────────────────────────┐           ┌────────────────────────────────┐
  │ Smartphones & Laptops     │ ◄-Wi-Fi-► │ Outdoor APs / Directional Ant. │
  │ (Unlicensed 2.4/5.8 GHz)  │           │ OpenWrt + B.A.T.M.A.N.-adv Mesh│
  └───────────────────────────┘           └──────────────┬─────────────────┘
                                                         │
  ┌───────────────────────────┐                          │ Layer 2 Mesh
  │ LTE / 5G Test Devices     │ ◄--RF---► ┌──────────────▼─────────────────┐
  │ (Shielded / Lab Box)      │ (SMA/Att) │ srsRAN eNB/gNB (SDR Transceiver│
  └───────────────────────────┘           └──────────────┬─────────────────┘
                                                         │ S1-MME / N2-N3
                                          ┌──────────────▼─────────────────┐
                                          │ Open5GS 4G/5G Cellular Core    │
                                          │ (MME / SGW / SMF / UPF / HSS)  │
                                          └──────────────┬─────────────────┘
                                                         │ SGi / N6 Interface
                                          ┌──────────────▼─────────────────┐
                                          │ Aira Sovereign Edge Gateway    │
                                          │ • nftables NAT / Security      │
                                          │ • CoovaChilli Captive Portal   │
                                          │ • WireGuard Uplink Tunnel      │
                                          └──────────────┬─────────────────┘
                                                         │
                                  ┌──────────────────────┴─────────────────┐
                                  ▼                                        ▼
                   ┌─────────────────────────────┐       ┌─────────────────┴───────┐
                   │ Upstream Backhaul           │       │ Sovereign Telecom NOC   │
                   │ (K-FON / BharatNet / Fibre) │       │ (Prometheus + Grafana)  │
                   └─────────────────────────────┘       └─────────────────────────┘
```

---

## 📂 Repository Module Breakdown

| Directory | Component | Purpose & Technologies |
|---|---|---|
| [`gateway/`](gateway/) | **Sovereign Edge Gateway** | Production `nftables` stateful NAT, WireGuard encrypted backhaul overlay (`wg0`), and CoovaChilli captive portal authentication. |
| [`lab-4g5g/`](lab-4g5g/) | **Private 4G/5G Cellular Core** | Full Open5GS containerized core (MME, AMF, SMF, UPF, PCRF, HSS) + srsRAN SDR configurations and automated SIM provisioning scripts. |
| [`mesh/openwrt/`](mesh/openwrt/) | **Decentralized Rooftop Mesh** | OpenWrt router configurations utilizing B.A.T.M.A.N.-adv for self-healing, multi-hop community Wi-Fi backhaul without single points of failure. |
| [`monitoring/`](monitoring/) | **Telemetry & NOC Dashboard** | Automated Prometheus metrics scrapers and Grafana dashboards tracking packet loss, SNR, active subscribers, and gateway bandwidth. |
| [`sockets/`](sockets/) | **Low-Level Network Primitives** | Pure Python socket engines demonstrating raw TCP state machines, UDP telemetry echoes, and resilient chunked file transmission. |
| [`docs/`](docs/) | **Engineering & Legal Blueprints** | In-depth technical documentation covering Indian telecom regulations, architecture designs, roadmaps, and community funding models. |

---

## ⚡ Hardware Bill of Materials (Recommended Specs)

To deploy an Aira Internet Tower station for a village or campus hub, the following standard off-the-shelf hardware is recommended:

| Subsystem | Recommended Hardware | Approximate Cost (INR) |
|---|---|---|
| **Tower Edge Gateway & Core** | Raspberry Pi 5 (8GB) or Intel N100 Mini PC | ₹7,500 – ₹14,000 |
| **Mesh Distribution Nodes** | GL.iNet / TP-Link Archer running OpenWrt | ₹2,500 – ₹4,500 / node |
| **Long-Range Outdoor APs** | Ubiquiti NanoStation Loco M5 / TP-Link Pharos | ₹4,000 – ₹6,000 / link |
| **SDR Radio (Lab 4G/5G)** | LimeSDR USB / BladeRF x40 / HackRF One (Shielded) | Research bench |
| **Power Autonomy** | 100W Monocrystalline Solar Panel + 12V 30Ah LiFePO4 Battery + MPPT | ₹9,000 – ₹12,000 |
| **Enclosure & Antennas** | IP67 Weatherproof Outdoor Box + Lightning Surge Protector | ₹3,000 |

---

## 🚀 Quick Start Guide

### 1. Run Socket Foundations Demo
Test the low-level socket server locally:
```bash
# Clone the repository
git clone https://github.com/adameehanairagroup/AiraInternetTower.git
cd AiraInternetTower

# Launch TCP Chat Relay
make sockets-demo
```
In another terminal, connect as a client:
```bash
python3 sockets/python/tcp_chat_client.py 127.0.0.1 5000
```

### 2. Deploy Containerized 4G/5G Open5GS Core (Lab)
Start the complete 4G EPC and 5G Core network stack:
```bash
make lab-up
```
Provision a test SIM into MongoDB HSS/UDR:
```bash
./lab-4g5g/scripts/provision_sim.sh 001010000000001 465B5CE8B199B49FAA5F0A2EE238A6BC
```

### 3. Spin up Telecom Telemetry & NOC Dashboard
Launch Prometheus and Grafana for real-time bandwidth and signal tracking:
```bash
make monitoring-up
```
* **Grafana Dashboard:** Visit `http://localhost:3000` (Default login: `admin` / `admin`).
* **Prometheus Targets:** Visit `http://localhost:9090`.

### 4. Deploy OpenWrt B.A.T.M.A.N.-adv Mesh Node
On your OpenWrt wireless node, copy and apply the mesh configuration:
```bash
scp -r mesh/openwrt/config/* root@192.168.1.1:/etc/config/
ssh root@192.168.1.1 "/etc/init.d/network restart"
```

---

## 🤝 Community Ownership & Governance Model

The **Aira Internet Tower** architecture is rooted in sustainable community participation:

* **Panchayat & Rural Fiber Tie-ups:** Connecting community towers to State and Central high-speed backhauls (**K-FON** in Kerala, **BharatNet** nationwide).
* **Zero-Rated Civic Tier:** Unlimited free access to government services (e-District, DigiLocker, educational resources, Kiwix offline Wikipedia).
* **Student Network Engineers:** Empowering local polytechnic and engineering students to maintain and audit their own community nodes.
* **Cooperative Cost Sharing:** Transparent maintenance funds pooled through local resident associations or CSR grants.

---

## 👨‍💻 Founder, Principal Architect & Leadership

* **Er. Adam Eehan**  
  *Founder & CEO, Aira Group of Technology*  
  *Google Student Ambassador 2026*  
  *Website:* [airaaigroup.in](https://airaaigroup.in)  
  *Email:* [adameehan34@gmail.com](mailto:adameehan34@gmail.com) • [noreply@airaaigroup.in](mailto:noreply@airaaigroup.in)  
  *GitHub:* [@adameehanairagroup](https://github.com/adameehanairagroup)

---

## 📜 License & Acknowledgments

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for full details.  
Built with deep appreciation for the open-source telecom pioneers behind **Open5GS**, **srsRAN**, **OpenWrt**, **B.A.T.M.A.N.-adv**, and the **Linux Kernel Networking Subsystem**.
