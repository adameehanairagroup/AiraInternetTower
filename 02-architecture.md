# Architecture
```
 Phones --(4G/5G radio)--> srsRAN eNB/gNB --S1/NG--> Open5GS core --SGi/N6--> Gateway --> Upstream (fibre)
 Homes  --(Wi-Fi mesh, BATMAN-adv)--> Gateway node -----------------------------------^
```
- RAN: srsRAN (lab) or licensed small cell.
- Core: Open5GS (MME/AMF, SMF, UPF, HSS/UDM).
- Gateway: nftables NAT, WireGuard to a VPS/ISP, optional CoovaChilli captive portal.
- Monitoring: Prometheus + Grafana.
